from .balancers import DoubleBalancer
from .balancers import SimpleBalancer
from .balancers import TripleBalancer
from .balancers import UndersampleBalancer


def list_balancers():
    balancers = [
        DoubleBalancer,
        SimpleBalancer,
        TripleBalancer,
        UndersampleBalancer
    ]
    return {b.name: b for b in balancers}
