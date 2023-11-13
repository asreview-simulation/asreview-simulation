from asreview.models.classifiers.logistic import LogisticClassifier


def instantiate_unwrapped_cls_logistic(params, random_state):
    mapped_params = {
        "C": params["c"],
        "class_weight": params["class_weight"],
    }
    return LogisticClassifier(**mapped_params, random_state=random_state)
