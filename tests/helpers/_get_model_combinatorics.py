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
        "logistic": pytest.mark.cls_logistic,
        "lstm-base": pytest.mark.cls_lstm_base,
        "lstm-pool": pytest.mark.cls_lstm_pool,
        "nb": pytest.mark.cls_nb,
        "nn-2-layer": pytest.mark.cls_nn_2_layer,
        "rf": pytest.mark.cls_rf,
        "svm": pytest.mark.cls_svm,
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
    clss = [cls.name for cls in list_classifiers()]
    combos = [(fex, cls) for (fex, cls) in itertools.product(*[fexs, clss])]
    return [pytest.param(",".join([fex, cls]), marks=[marks.get(fex), marks.get(cls)]) for (fex, cls) in combos]
