from .readers import CsvReader
from .readers import RisReader
from .readers import TsvReader
from .readers import XlsReader


def list_readers():
    readers = [
        CsvReader,
        RisReader,
        TsvReader,
        XlsReader
    ]
    return {b.name: b for b in readers}
