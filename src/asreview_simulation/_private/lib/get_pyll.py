import hyperopt
from asreview_simulation._private.lib.bal.bal_double_pyll import bal_double_pyll
from asreview_simulation._private.lib.bal.bal_simple_pyll import bal_simple_pyll
from asreview_simulation._private.lib.bal.bal_undersample_pyll import bal_undersample_pyll
from asreview_simulation._private.lib.cls.cls_logistic_pyll import cls_logistic_pyll
from asreview_simulation._private.lib.cls.cls_lstm_base_pyll import cls_lstm_base_pyll
from asreview_simulation._private.lib.cls.cls_lstm_pool_pyll import cls_lstm_pool_pyll
from asreview_simulation._private.lib.cls.cls_nb_pyll import cls_nb_pyll
from asreview_simulation._private.lib.cls.cls_nn_2_layer_pyll import cls_nn_2_layer_pyll
from asreview_simulation._private.lib.cls.cls_rf_pyll import cls_rf_pyll
from asreview_simulation._private.lib.cls.cls_svm_pyll import cls_svm_pyll
from asreview_simulation._private.lib.fex.fex_doc2vec_pyll import fex_doc2vec_pyll
from asreview_simulation._private.lib.fex.fex_embedding_idf_pyll import fex_embedding_idf_pyll
from asreview_simulation._private.lib.fex.fex_embedding_lstm_pyll import fex_embedding_lstm_pyll
from asreview_simulation._private.lib.fex.fex_sbert_pyll import fex_sbert_pyll
from asreview_simulation._private.lib.fex.fex_tfidf_pyll import fex_tfidf_pyll
from asreview_simulation._private.lib.qry.qry_cluster_pyll import qry_cluster_pyll
from asreview_simulation._private.lib.qry.qry_max_pyll import qry_max_pyll
from asreview_simulation._private.lib.qry.qry_max_random_pyll import qry_max_random_pyll
from asreview_simulation._private.lib.qry.qry_max_uncertainty_pyll import qry_max_uncertainty_pyll
from asreview_simulation._private.lib.qry.qry_random_pyll import qry_random_pyll
from asreview_simulation._private.lib.qry.qry_uncertainty_pyll import qry_uncertainty_pyll
from asreview_simulation._private.lib.sam.sam_handpicked_pyll import sam_handpicked_pyll
from asreview_simulation._private.lib.sam.sam_random_pyll import sam_random_pyll
from asreview_simulation._private.lib.stp.stp_none_pyll import stp_none_pyll
from asreview_simulation._private.lib.stp.stp_nq_pyll import stp_nq_pyll
from asreview_simulation._private.lib.stp.stp_rel_pyll import stp_rel_pyll


def bal_star_pyll():
    return hyperopt.hp.choice(
        "bal",
        [
            get_pyll("bal-double"),
            get_pyll("bal-simple"),
            get_pyll("bal-undersample"),
        ],
    )


def cls_star_pyll():
    return hyperopt.hp.choice(
        "cls",
        [
            get_pyll("cls-logistic"),
            get_pyll("cls-lstm-base"),
            get_pyll("cls-lstm-pool"),
            get_pyll("cls-nb"),
            get_pyll("cls-nn-2-layer"),
            get_pyll("cls-rf"),
            get_pyll("cls-svm"),
        ],
    )


def fex_star_pyll():
    return hyperopt.hp.choice(
        "fex",
        [
            get_pyll("fex-doc2vec"),
            get_pyll("fex-embedding-idf"),
            get_pyll("fex-embedding-lstm"),
            get_pyll("fex-sbert"),
            get_pyll("fex-tfidf"),
        ],
    )


def qry_star_pyll():
    return hyperopt.hp.choice(
        "qry",
        [
            get_pyll("qry-cluster"),
            get_pyll("qry-max"),
            get_pyll("qry-max-random"),
            get_pyll("qry-max-uncertainty"),
            get_pyll("qry-random"),
            get_pyll("qry-uncertainty"),
        ],
    )


def sam_star_pyll():
    return hyperopt.hp.choice(
        "sam",
        [
            get_pyll("sam-handpicked"),
            get_pyll("sam-random"),
        ],
    )


def stp_star_pyll():
    return hyperopt.hp.choice(
        "stp",
        [
            get_pyll("stp-none"),
            get_pyll("stp-nq"),
            get_pyll("stp-rel"),
        ],
    )


def star_pyll():
    return {
        "bal": get_pyll("bal-*"),
        "cls": get_pyll("cls-*"),
        "fex": get_pyll("fex-*"),
        "qry": get_pyll("qry-*"),
        "sam": get_pyll("sam-*"),
        "stp": get_pyll("stp-*")
    }


def get_pyll(name):
    funcmap = {
        "*": star_pyll,
        "bal-*": bal_star_pyll,
        "bal-double": bal_double_pyll,
        "bal-simple": bal_simple_pyll,
        "bal-undersample": bal_undersample_pyll,
        "cls-*": cls_star_pyll,
        "cls-logistic": cls_logistic_pyll,
        "cls-lstm-base": cls_lstm_base_pyll,
        "cls-lstm-pool": cls_lstm_pool_pyll,
        "cls-nb": cls_nb_pyll,
        "cls-nn-2-layer": cls_nn_2_layer_pyll,
        "cls-rf": cls_rf_pyll,
        "cls-svm": cls_svm_pyll,
        "fex-*": fex_star_pyll,
        "fex-doc2vec": fex_doc2vec_pyll,
        "fex-embedding-idf": fex_embedding_idf_pyll,
        "fex-embedding-lstm": fex_embedding_lstm_pyll,
        "fex-sbert": fex_sbert_pyll,
        "fex-tfidf": fex_tfidf_pyll,
        "qry-*": qry_star_pyll,
        "qry-cluster": qry_cluster_pyll,
        "qry-max": qry_max_pyll,
        "qry-max-random": qry_max_random_pyll,
        "qry-max-uncertainty": qry_max_uncertainty_pyll,
        "qry-random": qry_random_pyll,
        "qry-uncertainty": qry_uncertainty_pyll,
        "sam-*": sam_star_pyll,
        "sam-handpicked": sam_handpicked_pyll,
        "sam-random": sam_random_pyll,
        "stp-*": stp_star_pyll,
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
