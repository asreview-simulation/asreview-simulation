from .datasets import FirstDataset
from .datasets import SecondDataset
from importlib.metadata import entry_points


def list_datasets():
    my_datasets = {d.name: d for d in [
        FirstDataset,
        SecondDataset
    ]}
    try:
        other_datasets = {e.name: e.load() for e in entry_points(group="asreviewlib.datasets")}
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreviewlib.datasets'. The error message was: {e}\nContinuing...")
        other_datasets = {}
    d = dict()
    d.update(my_datasets)
    d.update(other_datasets)
    return dict(sorted(d.items()))
