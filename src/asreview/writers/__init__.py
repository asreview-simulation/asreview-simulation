from ._csv_writer import CSVWriter
from ._ris_writer import RISWriter
from ._tsv_writer import TSVWriter
from ._xls_writer import XLSWriter


def list_writers():
    writers = [
        CSVWriter,
        RISWriter,
        TSVWriter,
        XLSWriter
    ]
    return {w.name: w for w in writers}


del _csv_writer

del _ris_writer
del _tsv_writer
del _xls_writer
