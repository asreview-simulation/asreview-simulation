from typing import Any
from typing import Dict
from typing import TypeAlias
from asreviewcontrib.simulation._private.lib.bal.bal_double_params import get_bal_double_params
from asreviewcontrib.simulation._private.lib.bal.bal_simple_params import get_bal_simple_params
from asreviewcontrib.simulation._private.lib.bal.bal_undersample_params import get_bal_undersample_params
from asreviewcontrib.simulation._private.lib.clr.clr_logistic_params import get_clr_logistic_params
from asreviewcontrib.simulation._private.lib.clr.clr_lstm_base_params import get_clr_lstm_base_params
from asreviewcontrib.simulation._private.lib.clr.clr_lstm_pool_params import get_clr_lstm_pool_params
from asreviewcontrib.simulation._private.lib.clr.clr_nb_params import get_clr_nb_params
from asreviewcontrib.simulation._private.lib.clr.clr_nn_2_layer_params import get_clr_nn_2_layer_params
from asreviewcontrib.simulation._private.lib.clr.clr_rf_params import get_clr_rf_params
from asreviewcontrib.simulation._private.lib.clr.clr_svm_params import get_clr_svm_params
from asreviewcontrib.simulation._private.lib.fex.fex_doc2vec_params import get_fex_doc2vec_params
from asreviewcontrib.simulation._private.lib.fex.fex_embedding_idf_params import get_fex_embedding_idf_params
from asreviewcontrib.simulation._private.lib.fex.fex_embedding_lstm_params import get_fex_embedding_lstm_params
from asreviewcontrib.simulation._private.lib.fex.fex_sbert_params import get_fex_sbert_params
from asreviewcontrib.simulation._private.lib.fex.fex_tfidf_params import get_fex_tfidf_params
from asreviewcontrib.simulation._private.lib.ofn.ofn_none_params import get_ofn_none_params
from asreviewcontrib.simulation._private.lib.ofn.ofn_wss_params import get_ofn_wss_params
from asreviewcontrib.simulation._private.lib.qry.qry_cluster_params import get_qry_cluster_params
from asreviewcontrib.simulation._private.lib.qry.qry_max_params import get_qry_max_params
from asreviewcontrib.simulation._private.lib.qry.qry_max_random_params import get_qry_max_random_params
from asreviewcontrib.simulation._private.lib.qry.qry_max_uncertainty_params import get_qry_max_uncertainty_params
from asreviewcontrib.simulation._private.lib.qry.qry_random_params import get_qry_random_params
from asreviewcontrib.simulation._private.lib.qry.qry_uncertainty_params import get_qry_uncertainty_params
from asreviewcontrib.simulation._private.lib.sam.sam_handpicked_params import get_sam_handpicked_params
from asreviewcontrib.simulation._private.lib.sam.sam_random_params import get_sam_random_params
from asreviewcontrib.simulation._private.lib.stp.stp_none_params import get_stp_none_params
from asreviewcontrib.simulation._private.lib.stp.stp_nq_params import get_stp_nq_params
from asreviewcontrib.simulation._private.lib.stp.stp_rel_params import get_stp_rel_params


TGenericParams: TypeAlias = Dict[str, Any]


def get_default_params(name: str) -> TGenericParams:
    funcmap = {
        "bal-double": get_bal_double_params,
        "bal-simple": get_bal_simple_params,
        "bal-undersample": get_bal_undersample_params,
        "clr-logistic": get_clr_logistic_params,
        "clr-lstm-base": get_clr_lstm_base_params,
        "clr-lstm-pool": get_clr_lstm_pool_params,
        "clr-nb": get_clr_nb_params,
        "clr-nn-2-layer": get_clr_nn_2_layer_params,
        "clr-rf": get_clr_rf_params,
        "clr-svm": get_clr_svm_params,
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
