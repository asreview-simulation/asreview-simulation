from .classifiers import LogisticClassifier
from .classifiers import LstmBaseClassifier
from .classifiers import LstmPoolClassifier
from .classifiers import NaiveBayesClassifier
from .classifiers import NN2LayerClassifier
from .classifiers import RandomForestClassifier
from .classifiers import SvmClassifier


def list_classifiers():
    classifiers = [
        LogisticClassifier,
        LstmBaseClassifier,
        LstmPoolClassifier,
        NaiveBayesClassifier,
        NN2LayerClassifier,
        RandomForestClassifier,
        SvmClassifier
    ]
    return {c.name: c for c in classifiers}
