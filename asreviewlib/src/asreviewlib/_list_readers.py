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
    try:
        other_readers = {e.name: e.load() for e in entrypoints(group="asreviewlib.readers")}
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreviewlib.readers'. The error message was: {e}\nContinuing...")
        other_readers = {}
    rv = dict()
    rv.update(my_readers)
    rv.update(other_readers)
    return rv
