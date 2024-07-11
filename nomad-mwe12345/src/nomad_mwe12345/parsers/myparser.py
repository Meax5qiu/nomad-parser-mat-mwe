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
from nomad.datamodel.results import Material, Results
from nomad.parsing.parser import MatchingParser
from nomad_mwe12345.schema_packages.mypackage import MySchema

import numpy as np
from scipy.io import loadmat

configuration = config.get_plugin_entry_point(
    'nomad_mwe12345.parsers:myparser'
)


class MyParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'MySchema',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        logger.info('MyParser.parse', parameter=configuration.parameter)

        file = loadmat(mainfile, simplify_cells=True)
        Inputs=file["mainstruct"]

        # This section {
        #   * captures the data structure of the mainfile (in this case: one convention of using Matlab binary files)
        #   * implicitly provides a schema (How will the link to the actual schema plugin be established?)
        #   * does a parser's work of mapping input quantities to entries of an ontology
        #   * prints out the restructured data (populating the `archive` shall happen afterwards)
        schema_dict = dict()
        schema_dict["data_block"] = dict()
        schema_dict["data_block"]["vector_int"]  = Inputs["data"]["arr"]
        schema_dict["data_block"]["one_float"]   = Inputs["data"]["float"]
        schema_dict["metadata_block"] = dict()
        schema_dict["metadata_block"]["comment"] = Inputs["meta"]["str"]
        print(schema_dict)
        # }

        # Populate the data archive by instantiation <https://fairmat-nfdi.github.io/fairmat-tutorial-14-computational-plugins/parser_plugins/#via-instantiation>
        archive.data = MySchema(
            data_vector_int = schema_dict["data_block"]["vector_int"],
            data_one_float  = schema_dict["data_block"]["one_float"],
            meta_comment    = schema_dict["metadata_block"]["comment"]
            )
