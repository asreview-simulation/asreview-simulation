from .writers import CsvWriter
from .writers import RisWriter
from .writers import TsvWriter
from .writers import XlsWriter


def list_writers():
    writers = [
        CsvWriter,
        RisWriter,
        TsvWriter,
        XlsWriter
    ]
    return {b.name: b for b in writers}
