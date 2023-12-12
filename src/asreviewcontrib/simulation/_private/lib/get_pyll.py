from typing import TypeAlias
import hyperopt
from asreviewcontrib.simulation._private.lib.bal.bal_double_pyll import bal_double_pyll
from asreviewcontrib.simulation._private.lib.bal.bal_simple_pyll import bal_simple_pyll
from asreviewcontrib.simulation._private.lib.bal.bal_undersample_pyll import bal_undersample_pyll
from asreviewcontrib.simulation._private.lib.clr.clr_logistic_pyll import clr_logistic_pyll
from asreviewcontrib.simulation._private.lib.clr.clr_lstm_base_pyll import clr_lstm_base_pyll
from asreviewcontrib.simulation._private.lib.clr.clr_lstm_pool_pyll import clr_lstm_pool_pyll
from asreviewcontrib.simulation._private.lib.clr.clr_nb_pyll import clr_nb_pyll
from asreviewcontrib.simulation._private.lib.clr.clr_nn_2_layer_pyll import clr_nn_2_layer_pyll
from asreviewcontrib.simulation._private.lib.clr.clr_rf_pyll import clr_rf_pyll
from asreviewcontrib.simulation._private.lib.clr.clr_svm_pyll import clr_svm_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_doc2vec_pyll import fex_doc2vec_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_embedding_idf_pyll import fex_embedding_idf_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_embedding_lstm_pyll import fex_embedding_lstm_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_sbert_pyll import fex_sbert_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_tfidf_pyll import fex_tfidf_pyll
from asreviewcontrib.simulation._private.lib.get_quads import get_quads
from asreviewcontrib.simulation._private.lib.ofn.ofn_none_pyll import ofn_none_pyll
from asreviewcontrib.simulation._private.lib.ofn.ofn_wss_pyll import ofn_wss_pyll
from asreviewcontrib.simulation._private.lib.qry.qry_cluster_pyll import qry_cluster_pyll
from asreviewcontrib.simulation._private.lib.qry.qry_max_pyll import qry_max_pyll
from asreviewcontrib.simulation._private.lib.qry.qry_max_random_pyll import qry_max_random_pyll
from asreviewcontrib.simulation._private.lib.qry.qry_max_uncertainty_pyll import qry_max_uncertainty_pyll
from asreviewcontrib.simulation._private.lib.qry.qry_random_pyll import qry_random_pyll
from asreviewcontrib.simulation._private.lib.qry.qry_uncertainty_pyll import qry_uncertainty_pyll
from asreviewcontrib.simulation._private.lib.sam.sam_handpicked_pyll import sam_handpicked_pyll
from asreviewcontrib.simulation._private.lib.sam.sam_random_pyll import sam_random_pyll
from asreviewcontrib.simulation._private.lib.stp.stp_none_pyll import stp_none_pyll
from asreviewcontrib.simulation._private.lib.stp.stp_nq_pyll import stp_nq_pyll
from asreviewcontrib.simulation._private.lib.stp.stp_rel_pyll import stp_rel_pyll


TPyll: TypeAlias = hyperopt.base.pyll.Apply


def get_pyll(abbr: str) -> TPyll:
    """
    Args:
        abbr:
            The model abbreviation.

    Returns:
        The Pyll program `dict` for a given model identified by the input argument
        `abbr`. Pyll programs define the sample space for a given model or combination of
        models. They are a concept from the `hyperopt` library, refer to
        https://hyperopt.github.io/hyperopt/ for more details.
    """
    my_pyll_getters = {
        "bal-double": bal_double_pyll,
        "bal-simple": bal_simple_pyll,
        "bal-undersample": bal_undersample_pyll,
        "clr-logistic": clr_logistic_pyll,
        "clr-lstm-base": clr_lstm_base_pyll,
        "clr-lstm-pool": clr_lstm_pool_pyll,
        "clr-nb": clr_nb_pyll,
        "clr-nn-2-layer": clr_nn_2_layer_pyll,
        "clr-rf": clr_rf_pyll,
        "clr-svm": clr_svm_pyll,
        "fex-doc2vec": fex_doc2vec_pyll,
        "fex-embedding-idf": fex_embedding_idf_pyll,
        "fex-embedding-lstm": fex_embedding_lstm_pyll,
        "fex-sbert": fex_sbert_pyll,
        "fex-tfidf": fex_tfidf_pyll,
        "ofn-none": ofn_none_pyll,
        "ofn-wss": ofn_wss_pyll,
        "qry-cluster": qry_cluster_pyll,
        "qry-max": qry_max_pyll,
        "qry-max-random": qry_max_random_pyll,
        "qry-max-uncertainty": qry_max_uncertainty_pyll,
        "qry-random": qry_random_pyll,
        "qry-uncertainty": qry_uncertainty_pyll,
        "sam-handpicked": sam_handpicked_pyll,
        "sam-random": sam_random_pyll,
        "stp-none": stp_none_pyll,
        "stp-nq": stp_nq_pyll,
        "stp-rel": stp_rel_pyll,
    }
    other_pyll_getters = [{abbr: q.pyll} for abbr, q in get_quads()]

    pyll_getters = my_pyll_getters
    for other_pyll_getter in other_pyll_getters:
        pyll_getters.update(other_pyll_getter)

    try:
        func = pyll_getters[abbr]
    except KeyError as e:
        abbrs = "\n".join(list(pyll_getters.keys()))
        print(f"'{abbr}' is not a valid name for a model. Valid names are:\n{abbrs}")
        raise e
    return func()
