from asreview.models.classifiers.nn_2_layer import NN2LayerClassifier


def instantiate_unwrapped_cls_nn_2_layer(params, random_state):
    mapped_params = {
        "batch_size": params["batch_size"],
        "class_weight": params["class_weight"],
        "dense_width": params["dense_width"],
        "epochs": params["epochs"],
        "learn_rate": params["learn_rate"],
        "optimizer": params["optimizer"],
        "regularization": params["regularization"],
        "shuffle": params["shuffle"],
    }
    return NN2LayerClassifier(**mapped_params)
