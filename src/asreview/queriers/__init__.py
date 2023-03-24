from ._base_querier import BaseQuerier
from ._max_querier import MaxQuerier
from ._cluster_querier import ClusterQuerier
from ._max_random_querier import MaxRandomQuerier
from ._max_uncertainty_querier import MaxUncertaintyQuerier
from ._mixed_querier import MixedQuerier
from ._random_querier import RandomQuerier
from ._uncertainty_querier import UncertaintyQuerier


def list_queriers():
    queriers = [
        MaxQuerier,
        ClusterQuerier,
        MaxRandomQuerier,
        MaxUncertaintyQuerier,
        MixedQuerier,
        RandomQuerier,
        UncertaintyQuerier
    ]
    return {q.name: q for q in queriers}


del _base_querier
del _max_querier
del _cluster_querier
del _max_random_querier
del _max_uncertainty_querier
del _mixed_querier
del _random_querier
del _uncertainty_querier
