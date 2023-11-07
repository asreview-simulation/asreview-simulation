from asreview.models.classifiers.logistic import LogisticClassifier


def cls_logistic_unwrap(params, random_state):
    mapped_params = {
        "C": params["c"],
        "class_weight": params["class_weight"],
    }
    return LogisticClassifier(**mapped_params, random_state=random_state)
