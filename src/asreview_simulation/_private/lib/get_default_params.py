from asreview_simulation._private.lib.bal.bal_double_params import get_bal_double_params
from asreview_simulation._private.lib.bal.bal_simple_params import get_bal_simple_params
from asreview_simulation._private.lib.bal.bal_undersample_params import get_bal_undersample_params
from asreview_simulation._private.lib.cls.cls_logistic_params import get_cls_logistic_params
from asreview_simulation._private.lib.cls.cls_lstm_base_params import get_cls_lstm_base_params
from asreview_simulation._private.lib.cls.cls_lstm_pool_params import get_cls_lstm_pool_params
from asreview_simulation._private.lib.cls.cls_nb_params import get_cls_nb_params
from asreview_simulation._private.lib.cls.cls_nn_2_layer_params import get_cls_nn_2_layer_params
from asreview_simulation._private.lib.cls.cls_rf_params import get_cls_rf_params
from asreview_simulation._private.lib.cls.cls_svm_params import get_cls_svm_params
from asreview_simulation._private.lib.fex.fex_doc2vec_params import get_fex_doc2vec_params
from asreview_simulation._private.lib.fex.fex_embedding_idf_params import get_fex_embedding_idf_params
from asreview_simulation._private.lib.fex.fex_embedding_lstm_params import get_fex_embedding_lstm_params
from asreview_simulation._private.lib.fex.fex_sbert_params import get_fex_sbert_params
from asreview_simulation._private.lib.fex.fex_tfidf_params import get_fex_tfidf_params
from asreview_simulation._private.lib.ofn.ofn_none_params import get_ofn_none_params
from asreview_simulation._private.lib.ofn.ofn_wss_params import get_ofn_wss_params
from asreview_simulation._private.lib.qry.qry_cluster_params import get_qry_cluster_params
from asreview_simulation._private.lib.qry.qry_max_params import get_qry_max_params
from asreview_simulation._private.lib.qry.qry_max_random_params import get_qry_max_random_params
from asreview_simulation._private.lib.qry.qry_max_uncertainty_params import get_qry_max_uncertainty_params
from asreview_simulation._private.lib.qry.qry_random_params import get_qry_random_params
from asreview_simulation._private.lib.qry.qry_uncertainty_params import get_qry_uncertainty_params
from asreview_simulation._private.lib.sam.sam_handpicked_params import get_sam_handpicked_params
from asreview_simulation._private.lib.sam.sam_random_params import get_sam_random_params
from asreview_simulation._private.lib.stp.stp_none_params import get_stp_none_params
from asreview_simulation._private.lib.stp.stp_nq_params import get_stp_nq_params
from asreview_simulation._private.lib.stp.stp_rel_params import get_stp_rel_params


def get_default_params(name: str) -> dict:
    funcmap = {
        "bal-double": get_bal_double_params,
        "bal-simple": get_bal_simple_params,
        "bal-undersample": get_bal_undersample_params,
        "cls-logistic": get_cls_logistic_params,
        "cls-lstm-base": get_cls_lstm_base_params,
        "cls-lstm-pool": get_cls_lstm_pool_params,
        "cls-nb": get_cls_nb_params,
        "cls-nn-2-layer": get_cls_nn_2_layer_params,
        "cls-rf": get_cls_rf_params,
        "cls-svm": get_cls_svm_params,
        "fex-doc2vec": get_fex_doc2vec_params,
        "fex-embedding-idf": get_fex_embedding_idf_params,
        "fex-embedding-lstm": get_fex_embedding_lstm_params,
        "fex-sbert": get_fex_sbert_params,
        "fex-tfidf": get_fex_tfidf_params,
        "ofn-none": get_ofn_none_params,
        "ofn-wss": get_ofn_wss_params,
        "qry-cluster": get_qry_cluster_params,
        "qry-max": get_qry_max_params,
        "qry-max-random": get_qry_max_random_params,
        "qry-max-uncertainty": get_qry_max_uncertainty_params,
        "qry-random": get_qry_random_params,
        "qry-uncertainty": get_qry_uncertainty_params,
        "sam-handpicked": get_sam_handpicked_params,
        "sam-random": get_sam_random_params,
        "stp-none": get_stp_none_params,
        "stp-nq": get_stp_nq_params,
        "stp-rel": get_stp_rel_params,
    }
    try:
        func = funcmap[name]
    except KeyError as e:
        names = "\n".join(list(funcmap.keys()))
        print(f"'{name}' is not a valid name for a model. Valid names are:\n{names}")
        raise e
    return func()
