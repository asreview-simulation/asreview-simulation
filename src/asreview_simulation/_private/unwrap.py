from asreview_simulation._private.bal_double_unwrap import bal_double_unwrap
from asreview_simulation._private.bal_simple_unwrap import bal_simple_unwrap
from asreview_simulation._private.bal_undersample_unwrap import bal_undersample_unwrap
from asreview_simulation._private.cls_logistic_unwrap import cls_logistic_unwrap
from asreview_simulation._private.cls_lstm_base_unwrap import cls_lstm_base_unwrap
from asreview_simulation._private.cls_lstm_pool_unwrap import cls_lstm_pool_unwrap
from asreview_simulation._private.cls_nb_unwrap import cls_nb_unwrap
from asreview_simulation._private.cls_nn_2_layer_unwrap import cls_nn_2_layer_unwrap
from asreview_simulation._private.cls_rf_unwrap import cls_rf_unwrap
from asreview_simulation._private.cls_svm_unwrap import cls_svm_unwrap
from asreview_simulation._private.fex_doc2vec_unwrap import fex_doc2vec_unwrap
from asreview_simulation._private.fex_embedding_idf_unwrap import fex_embedding_idf_unwrap
from asreview_simulation._private.fex_embedding_lstm_unwrap import fex_embedding_lstm_unwrap
from asreview_simulation._private.fex_sbert_unwrap import fex_sbert_unwrap
from asreview_simulation._private.fex_tfidf_unwrap import fex_tfidf_unwrap
from asreview_simulation._private.qry_cluster_unwrap import qry_cluster_unwrap
from asreview_simulation._private.qry_max_unwrap import qry_max_unwrap
from asreview_simulation._private.qry_random_unwrap import qry_random_unwrap
from asreview_simulation._private.qry_uncertainty_unwrap import qry_uncertainty_unwrap


def unwrap(model, random_state):
    # TODO qry-max-random, qry-max-uncertainty
    mapping = {
        "bal-double": bal_double_unwrap,
        "bal-simple": bal_simple_unwrap,
        "bal-undersample": bal_undersample_unwrap,
        "cls-logistic": cls_logistic_unwrap,
        "cls-lstm-base": cls_lstm_base_unwrap,
        "cls-lstm-pool": cls_lstm_pool_unwrap,
        "cls-nb": cls_nb_unwrap,
        "cls-nn-2-layer": cls_nn_2_layer_unwrap,
        "cls-rf": cls_rf_unwrap,
        "cls-svm": cls_svm_unwrap,
        "fex-doc2vec": fex_doc2vec_unwrap,
        "fex-embedding-idf": fex_embedding_idf_unwrap,
        "fex-embedding-lstm": fex_embedding_lstm_unwrap,
        "fex-sbert": fex_sbert_unwrap,
        "fex-tfidf": fex_tfidf_unwrap,
        "qry-cluster": qry_cluster_unwrap,
        "qry-max": qry_max_unwrap,
        "qry-random": qry_random_unwrap,
        "qry-uncertainty": qry_uncertainty_unwrap,
    }
    try:
        return mapping[model.abbr](model.params, random_state)
    except KeyError as e:
        abbrs = "\n".join([key for key in mapping.keys()])
        raise f"Undefined behavior for model name f{model.abbr}. Valid model names are: f{abbrs}" from e
