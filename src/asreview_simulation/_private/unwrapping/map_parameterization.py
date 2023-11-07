from asreview.models.balance.double import DoubleBalance
from asreview.models.balance.simple import SimpleBalance
from asreview.models.balance.undersample import UndersampleBalance
from asreview.models.classifiers.logistic import LogisticClassifier
from asreview.models.classifiers.lstm_base import LSTMBaseClassifier
from asreview.models.classifiers.lstm_pool import LSTMPoolClassifier
from asreview.models.classifiers.nb import NaiveBayesClassifier
from asreview.models.classifiers.nn_2_layer import NN2LayerClassifier
from asreview.models.classifiers.rf import RandomForestClassifier
from asreview.models.classifiers.svm import SVMClassifier
from asreview.models.feature_extraction.doc2vec import Doc2Vec
from asreview.models.feature_extraction.embedding_idf import EmbeddingIdf
from asreview.models.feature_extraction.embedding_lstm import EmbeddingLSTM
from asreview.models.feature_extraction.sbert import SBERT
from asreview.models.feature_extraction.tfidf import Tfidf
from asreview.models.query.cluster import ClusterQuery
from asreview.models.query.max import MaxQuery
from asreview.models.query.random import RandomQuery
from asreview.models.query.uncertainty import UncertaintyQuery


def map_parameterization(model, random_state):
    mapping = {
        "bal-double": map_parameterization_bal_double,
        "bal-simple": map_parameterization_bal_simple,
        "bal-undersample": map_parameterization_bal_undersample,
        "cls-logistic": map_parameterization_cls_logistic,
        "cls-lstm-base": map_parameterization_cls_lstm_base,
        "cls-lstm-pool": map_parameterization_cls_lstm_pool,
        "cls-nb": map_parameterization_cls_nb,
        "cls-nn-2-layer": map_parameterization_cls_nn_2_layer,
        "cls-rf": map_parameterization_cls_rf,
        "cls-svm": map_parameterization_cls_svm,
        "fex-doc2vec": map_parameterization_fex_doc2vec,
        "fex-embedding-idf": map_parameterization_fex_embedding_idf,
        "fex-embedding-lstm": map_parameterization_fex_embedding_lstm,
        "fex-sbert": map_parameterization_fex_sbert,
        "fex-tfidf": map_parameterization_fex_tfidf,
        "qry-cluster": map_parameterization_qry_cluster,
        "qry-max": map_parameterization_qry_max,
        # "qry-max-random": map_parameterization_qry_max_random,
        # "qry-max-uncertainty": map_parameterization_qry_max_uncertainty,
        "qry-random": map_parameterization_qry_random,
        "qry-uncertainty": map_parameterization_qry_uncertainty,
    }
    try:
        return mapping[model.abbr](model.params, random_state)
    except KeyError as e:
        abbrs = "\n".join([key for key in mapping.keys()])
        raise f"Undefined behavior for model name f{model.abbr}. Valid model names are: f{abbrs}" from e


def map_parameterization_bal_double(params, random_state):
    mapped_params = {
        "a": params["a"],
        "alpha": params["alpha"],
        "b": params["b"],
        "beta": params["beta"],
    }
    return DoubleBalance(**mapped_params, random_state=random_state)


def map_parameterization_bal_simple(_params, _random_state):
    return SimpleBalance()


def map_parameterization_bal_undersample(params, random_state):
    mapped_params = {
        "ratio": params["ratio"],
    }
    return UndersampleBalance(**mapped_params, random_state=random_state)


def map_parameterization_cls_logistic(params, random_state):
    mapped_params = {
        "C": params["c"],
        "class_weight": params["class_weight"],
    }
    return LogisticClassifier(**mapped_params, random_state=random_state)


def map_parameterization_cls_lstm_base(params, _random_state):
    mapped_params = {
        "backwards": not params["forward"],
        "batch_size": params["batch_size"],
        "class_weight": params["class_weight"],
        "dense_width": params["dense_width"],
        "dropout": params["dropout"],
        "epochs": params["epochs"],
        "optimizer": params["optimizer"],
        "learn_rate": params["learn_rate"],
        "lstm_out_width": params["lstm_out_width"],
        "shuffle": params["shuffle"],
    }
    return LSTMBaseClassifier(**mapped_params)


def map_parameterization_cls_lstm_pool(params, _random_state):
    mapped_params = {
        "backwards": not params["forward"],
        "batch_size": params["batch_size"],
        "class_weight": params["class_weight"],
        "dropout": params["dropout"],
        "epochs": params["epochs"],
        "learn_rate": params["learn_rate"],
        "lstm_out_width": params["lstm_out_width"],
        "lstm_pool_size": params["lstm_pool_size"],
        "optimizer": params["optimizer"],
        "shuffle": params["shuffle"],
    }
    return LSTMPoolClassifier(**mapped_params)


def map_parameterization_cls_nb(params, _random_state):
    mapped_params = {
        "alpha": params["alpha"],
    }
    return NaiveBayesClassifier(**mapped_params)


def map_parameterization_cls_nn_2_layer(params, random_state):
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


def map_parameterization_cls_rf(params, _random_state):
    mapped_params = {
        "class_weight": params["class_weight"],
        "max_features": params["max_features"],
        "n_estimators": params["n_estimators"],
    }
    return RandomForestClassifier(**mapped_params)


def map_parameterization_cls_svm(params, random_state):
    mapped_params = {
        "C": params["c"],
        "class_weight": params["class_weight"],
        "gamma": params["gamma"],
        "kernel": params["kernel"],
    }
    return SVMClassifier(**mapped_params, random_state=random_state)


def map_parameterization_fex_doc2vec(params, _random_state):
    mapped_params = {
        "dbow_words": {True: 1, False: 0}[params["dbow_words"]],
        "dm": {"dbow": 0, "dm": 1, "both": 2}[params["dm"]],
        "dm_concat": {True: 1, False: 0}[params["dm_concat"]],
        "epochs": params["epochs"],
        "min_count": params["min_count"],
        "split_ta": {True: 1, False: 0}[params["split_ta"]],
        "use_keywords": {True: 1, False: 0}[params["use_keywords"]],
        "vector_size": params["vector_size"],
        "window": params["window"],
    }
    return Doc2Vec(**mapped_params)


def map_parameterization_fex_embedding_idf(params, random_state):
    mapped_params = {
        "split_ta": {False: 0, True: 1}[params["split_ta"]],
        "use_keywords": {False: 0, True: 1}[params["use_keywords"]],
    }
    return EmbeddingIdf(**mapped_params, random_state=random_state)


def map_parameterization_fex_embedding_lstm(params, _random_state):
    mapped_params = {
        "loop_sequence": params["loop_sequence"],
        "max_sequence_length": params["max_sequence_length"],
        "num_words": params["num_words"],
        "padding": params["padding"],
        "split_ta": {False: 0, True: 1}[params["split_ta"]],
        "truncating": params["truncating"],
        "use_keywords": {False: 0, True: 1}[params["use_keywords"]],
    }
    return EmbeddingLSTM(**mapped_params)


def map_parameterization_fex_sbert(params, _random_state):
    mapped_params = {
        "split_ta": {False: 0, True: 1}[params["split_ta"]],
        "transformer_model": params["transformer_model"],
        "use_keywords": {False: 0, True: 1}[params["use_keywords"]],
    }
    return SBERT(**mapped_params)


def map_parameterization_fex_tfidf(params, _random_state):
    mapped_params = {
        "ngram_max": params["ngram_max"],
        "split_ta": {False: 0, True: 1}[params["split_ta"]],
        "stop_words": params["stop_words"],
        "use_keywords": {False: 0, True: 1}[params["use_keywords"]],
    }
    return Tfidf(**mapped_params)


def map_parameterization_qry_cluster(params, random_state):
    mapped_params = {
        "cluster_size": params["cluster_size"],
        "update_interval": params["update_interval"],
    }
    return ClusterQuery(**mapped_params, random_state=random_state)


def map_parameterization_qry_max(_params, _random_state):
    return MaxQuery()


# def map_parameterization_qry_max_random(params, random_state):
#     mapped_params = {
#         "mix_ratio": params["fraction_max"],
#     }
#     return get_query_model("max_random", random_state, mapped_params)
# 
# 
# def map_parameterization_qry_max_uncertainty(params, random_state):
#     mapped_params = {
#         "mix_ratio": params["fraction_max"],
#     }
#     return get_query_model("max_uncertainty", random_state, mapped_params)


def map_parameterization_qry_random(_params, random_state):
    return RandomQuery(random_state=random_state)


def map_parameterization_qry_uncertainty(_params, _random_state):
    return UncertaintyQuery()
