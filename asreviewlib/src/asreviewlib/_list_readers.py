from .readers import CsvReader
from .readers import RisReader
from .readers import TsvReader
from .readers import XlsReader
from importlib.metadata import entry_points as entrypoints


def list_readers():
    my_readers = {r.name: r for r in [
        CsvReader,
        RisReader,
        TsvReader,
        XlsReader
    ]}
    other_readers = {e.name: e.load() for e in entrypoints(group="asreviewlib.readers")}
    rv = dict()
    rv.update(my_readers)
    rv.update(other_readers)
    return rv
