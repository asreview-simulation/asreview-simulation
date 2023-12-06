import hyperopt
from asreviewcontrib.simulation._private.lib.bal.bal_double_pyll import bal_double_pyll
from asreviewcontrib.simulation._private.lib.bal.bal_simple_pyll import bal_simple_pyll
from asreviewcontrib.simulation._private.lib.bal.bal_undersample_pyll import bal_undersample_pyll
from asreviewcontrib.simulation._private.lib.cls.cls_logistic_pyll import cls_logistic_pyll
from asreviewcontrib.simulation._private.lib.cls.cls_lstm_base_pyll import cls_lstm_base_pyll
from asreviewcontrib.simulation._private.lib.cls.cls_lstm_pool_pyll import cls_lstm_pool_pyll
from asreviewcontrib.simulation._private.lib.cls.cls_nb_pyll import cls_nb_pyll
from asreviewcontrib.simulation._private.lib.cls.cls_nn_2_layer_pyll import cls_nn_2_layer_pyll
from asreviewcontrib.simulation._private.lib.cls.cls_rf_pyll import cls_rf_pyll
from asreviewcontrib.simulation._private.lib.cls.cls_svm_pyll import cls_svm_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_doc2vec_pyll import fex_doc2vec_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_embedding_idf_pyll import fex_embedding_idf_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_embedding_lstm_pyll import fex_embedding_lstm_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_sbert_pyll import fex_sbert_pyll
from asreviewcontrib.simulation._private.lib.fex.fex_tfidf_pyll import fex_tfidf_pyll
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


def get_pyll(name: str) -> hyperopt.base.pyll.Apply:
    """Return the Pyll program `dict` for a given model identified by the input argument
    `name`. Pyll programs define the sample space for a given model or combination of
    models. They are a concept from the `hyperopt` library, refer to
    https://hyperopt.github.io/hyperopt/ for more details."""
    funcmap = {
        "bal-double": bal_double_pyll,
        "bal-simple": bal_simple_pyll,
        "bal-undersample": bal_undersample_pyll,
        "cls-logistic": cls_logistic_pyll,
        "cls-lstm-base": cls_lstm_base_pyll,
        "cls-lstm-pool": cls_lstm_pool_pyll,
        "cls-nb": cls_nb_pyll,
        "cls-nn-2-layer": cls_nn_2_layer_pyll,
        "cls-rf": cls_rf_pyll,
        "cls-svm": cls_svm_pyll,
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
    try:
        func = funcmap[name]
    except KeyError as e:
        names = "\n".join(list(funcmap.keys()))
        print(f"'{name}' is not a valid name for a model. Valid names are:\n{names}")
        raise e
    return func()
