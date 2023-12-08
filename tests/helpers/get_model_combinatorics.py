import itertools
import pytest
from asreview.models.classifiers import list_classifiers
from asreview.models.feature_extraction import list_feature_extraction


def get_model_combinatorics():
    marks = {
        "doc2vec": pytest.mark.fex_doc2vec,
        "embedding-idf": pytest.mark.fex_embedding_idf,
        "embedding-lstm": pytest.mark.fex_embedding_lstm,
        "sbert": pytest.mark.fex_sbert,
        "tfidf": pytest.mark.fex_tfidf,
        "logistic": pytest.mark.clr_logistic,
        "lstm-base": pytest.mark.clr_lstm_base,
        "lstm-pool": pytest.mark.clr_lstm_pool,
        "nb": pytest.mark.clr_nb,
        "nn-2-layer": pytest.mark.clr_nn_2_layer,
        "rf": pytest.mark.clr_rf,
        "svm": pytest.mark.clr_svm,
        "cluster": pytest.mark.qry_cluster,
        "max": pytest.mark.qry_max,
        "max-random": pytest.mark.qry_max_random,
        "max-uncertainty": pytest.mark.qry_max_uncertainty,
        "random": pytest.mark.qry_random,
        "uncertainty": pytest.mark.qry_uncertainty,
        "double": pytest.mark.bal_double,
        "simple": pytest.mark.bal_simple,
        "undersample": pytest.mark.bal_undersample,
    }
    fexs = [fex.name for fex in list_feature_extraction()]
    clrs = [clr.name for clr in list_classifiers()]
    combos = [(fex, clr) for (fex, clr) in itertools.product(*[fexs, clrs])]
    return [pytest.param(",".join([fex, clr]), marks=[marks.get(fex), marks.get(clr)]) for (fex, clr) in combos]
