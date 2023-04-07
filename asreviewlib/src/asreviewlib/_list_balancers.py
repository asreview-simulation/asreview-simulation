from .balancers import DoubleBalancer
from .balancers import NoneBalancer
from .balancers import TripleBalancer
from .balancers import UndersampleBalancer
from importlib.metadata import entry_points


def list_balancers():
    my_balancers = {b.name: b for b in [
        DoubleBalancer,
        NoneBalancer,
        TripleBalancer,
        UndersampleBalancer
    ]}
    try:
        other_balancers = {e.name: e.load() for e in entry_points(group="asreviewlib.balancers")}
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreviewlib.balancers'. The error message was: {e}\nContinuing...")
        other_balancers = {}
    d = dict()
    d.update(my_balancers)
    d.update(other_balancers)
    return dict(sorted(d.items()))
