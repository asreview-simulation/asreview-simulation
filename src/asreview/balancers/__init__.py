from ._base_balancer import BaseBalancer
from ._simple_balancer import SimpleBalancer
from ._double_balancer import DoubleBalancer
from ._triple_balancer import TripleBalancer
from ._undersample_balancer import UndersampleBalancer


def list_balancers():
    balancers = [
        DoubleBalancer,
        SimpleBalancer,
        TripleBalancer,
        UndersampleBalancer
    ]
    return {b.name: b for b in balancers}


del _base_balancer
del _simple_balancer
del _double_balancer
del _triple_balancer
del _undersample_balancer
