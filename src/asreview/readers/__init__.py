from ._csv_reader import CSVReader
from ._ris_reader import RISReader
from ._tsv_reader import TSVReader
from ._xls_reader import XLSReader


def list_readers():
    readers = [
        CSVReader,
        RISReader,
        TSVReader,
        XLSReader
    ]
    return {r.name: r for r in readers}


del _csv_reader
del _ris_reader
del _tsv_reader
del _xls_reader
