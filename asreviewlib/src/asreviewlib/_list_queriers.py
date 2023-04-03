from .queriers import ClusterQuerier
from .queriers import MaxQuerier
from .queriers import MaxRandomQuerier
from .queriers import MaxUncertaintyQuerier
from .queriers import MixedQuerier
from .queriers import RandomQuerier
from .queriers import UncertaintyQuerier
from importlib.metadata import entry_points as entrypoints


def list_queriers():
    my_queriers = {q.name: q for q in [
        ClusterQuerier,
        MaxQuerier,
        MaxRandomQuerier,
        MaxUncertaintyQuerier,
        MixedQuerier,
        RandomQuerier,
        UncertaintyQuerier
    ]}
    other_queriers = {e.name: e.load() for e in entrypoints(group="asreviewlib.queriers")}
    rv = dict()
    rv.update(my_queriers)
    rv.update(other_queriers)
    return rv
