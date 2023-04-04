from .balancers import DoubleBalancer
from .balancers import NoneBalancer
from .balancers import TripleBalancer
from .balancers import UndersampleBalancer
from importlib.metadata import entry_points as entrypoints


def list_balancers():
    my_balancers = {b.name: b for b in [
        DoubleBalancer,
        NoneBalancer,
        TripleBalancer,
        UndersampleBalancer
    ]}
    try:
        other_balancers = {e.name: e.load() for e in entrypoints(group="asreviewlib.balancers")}
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreviewlib.balancers'. The error message was: {e}\nContinuing...")
        other_balancers = {}
    rv = dict()
    rv.update(my_balancers)
    rv.update(other_balancers)
    return rv
