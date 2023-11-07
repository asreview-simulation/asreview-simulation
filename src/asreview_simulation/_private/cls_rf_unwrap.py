from asreview.models.classifiers.rf import RandomForestClassifier


def cls_rf_unwrap(params, _random_state):
    mapped_params = {
        "class_weight": params["class_weight"],
        "max_features": params["max_features"],
        "n_estimators": params["n_estimators"],
    }
    return RandomForestClassifier(**mapped_params)
