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

import numpy as np
from scipy.io import loadmat

configuration = config.get_plugin_entry_point(
    'nomad_mwe12345.parsers:myparser'
)


class MyParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
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
        #   * just prints out the restructured data, in lieu of populating the EntryArchive
        schema_dict = dict()
        schema_dict["data_block"] = dict()
        schema_dict["data_block"]["vector_int"]  = Inputs["data"]["arr"]
        schema_dict["data_block"]["one_float"]   = Inputs["data"]["float"]
        schema_dict["metadata_block"] = dict()
        schema_dict["metadata_block"]["comment"] = Inputs["data"]["arr"]
        print(schema_dict)
        # }

        archive.results = Results(material=Material(elements=['H', 'O']))
        # TODO How to populate the EntryArchive with the contents of my `schema_dict`?
