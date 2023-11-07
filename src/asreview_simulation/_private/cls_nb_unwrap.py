from asreview.models.classifiers.nb import NaiveBayesClassifier


def cls_nb_unwrap(params, _random_state):
    mapped_params = {
        "alpha": params["alpha"],
    }
    return NaiveBayesClassifier(**mapped_params)
