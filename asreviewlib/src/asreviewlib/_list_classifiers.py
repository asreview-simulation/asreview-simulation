from .classifiers import LogisticClassifier
from .classifiers import LstmBaseClassifier
from .classifiers import LstmPoolClassifier
from .classifiers import NaiveBayesClassifier
from .classifiers import NN2LayerClassifier
from .classifiers import RandomForestClassifier
from .classifiers import SvmClassifier
from importlib.metadata import entry_points


def list_classifiers():
    my_classifiers = {c.name: c for c in [
        LogisticClassifier,
        LstmBaseClassifier,
        LstmPoolClassifier,
        NaiveBayesClassifier,
        NN2LayerClassifier,
        RandomForestClassifier,
        SvmClassifier
    ]}
    try:
        other_classifiers = {e.name: e.load() for e in entry_points(group="asreviewlib.classifiers")}
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreviewlib.classifiers'. The error message was: {e}\nContinuing...")
        other_classifiers = {}
    d = dict()
    d.update(my_classifiers)
    d.update(other_classifiers)
    return dict(sorted(d.items()))
