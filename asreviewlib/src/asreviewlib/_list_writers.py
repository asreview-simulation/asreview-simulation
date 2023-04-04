from .writers import CsvWriter
from .writers import RisWriter
from .writers import TsvWriter
from .writers import XlsWriter
from importlib.metadata import entry_points as entrypoints


def list_writers():
    my_writers = {w.name: w for w in [
        CsvWriter,
        RisWriter,
        TsvWriter,
        XlsWriter
    ]}
    try:
        other_writers = {e.name: e.load() for e in entrypoints(group="asreviewlib.writers")}
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreviewlib.writers'. The error message was: {e}\nContinuing...")
        other_writers = {}
    rv = dict()
    rv.update(my_writers)
    rv.update(other_writers)
    return rv
