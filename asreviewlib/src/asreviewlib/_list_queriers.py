from .queriers import ClusterQuerier
from .queriers import MaxQuerier
from .queriers import MaxRandomQuerier
from .queriers import MaxUncertaintyQuerier
from .queriers import MixedQuerier
from .queriers import RandomQuerier
from .queriers import UncertaintyQuerier


def list_queriers():
    queriers = [
        ClusterQuerier,
        MaxQuerier,
        MaxRandomQuerier,
        MaxUncertaintyQuerier,
        MixedQuerier,
        RandomQuerier,
        UncertaintyQuerier
    ]
    return {q.name: q for q in queriers}
