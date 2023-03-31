from .balancers import DoubleBalancer
from .balancers import SimpleBalancer
from .balancers import TripleBalancer
from .balancers import UndersampleBalancer
from importlib.metadata import entry_points as entrypoints


def list_balancers():
    my_balancers = {b.name: b for b in [
        DoubleBalancer,
        SimpleBalancer,
        TripleBalancer,
        UndersampleBalancer
    ]}
    other_balancers = {e.name: e.load() for e in entrypoints(group="balancers")}
    rv = dict()
    rv.update(my_balancers)
    rv.update(other_balancers)
    return rv

