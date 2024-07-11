from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, SchemaPackage

import numpy as np

configuration = config.get_plugin_entry_point(
    'nomad_mwe12345.schema_packages:mypackage'
)

m_package = SchemaPackage()


class MySchema(Schema):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    message = Quantity(type=str)

    # Introducing the quantities that specify the data (core ontology)
    data_vector_int = Quantity(
        type=np.int32, shape=['*'], description='''
        A list of integers with a variable length (to be sanity-checked by some code inside the parser/normalizer)
        ''')
    data_one_float = Quantity(
        type=np.float64, description='''
        Some single floating-point number
        ''')
    meta_comment = Quantity(
        type=str, description='''
        Space for some prose.
        ''')

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        logger.info('MySchema.normalize', parameter=configuration.parameter)
        self.message = f'Hello {self.name}!'


m_package.__init_metainfo__()
