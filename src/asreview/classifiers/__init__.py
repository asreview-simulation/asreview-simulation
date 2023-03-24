from ._base_classifier import BaseClassifier
from ._naive_bayes_classifier import NaiveBayesClassifier
from ._logistic_classifier import LogisticClassifier
from ._lstm_base_classifier import LstmBaseClassifier
from ._lstm_pool_classifier import LstmPoolClassifier
from ._nn_2_layer_classifier import NN2LayerClassifier
from ._random_forest_classifier import RandomForestClassifier
from ._svm_classifier import SVMClassifier


def list_classifiers():
    classifiers = [
        NaiveBayesClassifier,
        LogisticClassifier,
        LstmPoolClassifier,
        NN2LayerClassifier,
        RandomForestClassifier,
        SVMClassifier
    ]
    return {c.name: c for c in classifiers}


del _base_classifier
del _naive_bayes_classifier
del _logistic_classifier
del _lstm_base_classifier
del _lstm_pool_classifier
del _nn_2_layer_classifier
del _random_forest_classifier
del _svm_classifier
