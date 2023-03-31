from ._csv_reader import CsvReader
from ._ris_reader import RisReader
from ._tsv_reader import TsvReader
from ._xls_reader import XlsReader


del _csv_reader
del _ris_reader
del _tsv_reader
del _xls_reader

__all__ = [
    "CsvReader",
    "RisReader",
    "TsvReader",
    "XlsReader"
]

for _item in dir():
    if not _item.endswith('__'):
        assert _item in __all__, f"Named export {_item} missing from __all__ in {__package__}"
for _item in __all__:
    assert _item in dir(), f"__all__ includes unknown item {_item} in {__package__}"
del _item
