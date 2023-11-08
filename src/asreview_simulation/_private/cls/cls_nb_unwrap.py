from asreview.models.classifiers.nb import NaiveBayesClassifier


def instantiate_unwrapped_cls_nb(params, _random_state):
    mapped_params = {
        "alpha": params["alpha"],
    }
    return NaiveBayesClassifier(**mapped_params)
