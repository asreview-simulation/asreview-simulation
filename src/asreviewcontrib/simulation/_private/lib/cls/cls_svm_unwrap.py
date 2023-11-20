from asreview.models.classifiers.svm import SVMClassifier


def instantiate_unwrapped_cls_svm(params, random_state):
    mapped_params = {
        "C": params["c"],
        "class_weight": params["class_weight"],
        "gamma": params["gamma"],
        "kernel": params["kernel"],
    }
    return SVMClassifier(**mapped_params, random_state=random_state)
