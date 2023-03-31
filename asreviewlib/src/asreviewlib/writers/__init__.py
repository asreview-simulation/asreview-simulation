from ._csv_writer import CsvWriter
from ._ris_writer import RisWriter
from ._tsv_writer import TsvWriter
from ._xls_writer import XlsWriter


del _csv_writer
del _ris_writer
del _tsv_writer
del _xls_writer

__all__ = [
    "CsvWriter",
    "RisWriter",
    "TsvWriter",
    "XlsWriter"
]

for _item in dir():
    if not _item.endswith('__'):
        assert _item in __all__, f"Named export {_item} missing from __all__ in {__package__}"
for _item in __all__:
    assert _item in dir(), f"__all__ includes unknown item {_item} in {__package__}"
del _item
