from ._get_pyll_bal_double import get_pyll_bal_double
from ._get_pyll_bal_simple import get_pyll_bal_simple
from ._get_pyll_bal_undersample import get_pyll_bal_undersample
from ._get_pyll_cls_logistic import get_pyll_cls_logistic
from ._get_pyll_cls_nb import get_pyll_cls_nb
from ._get_pyll_cls_nn_2_layer import get_pyll_cls_nn_2_layer
from ._get_pyll_cls_rf import get_pyll_cls_rf
from ._get_pyll_cls_svm import get_pyll_cls_svm
from ._get_pyll_fex_doc2vec import get_pyll_fex_doc2vec
from ._get_pyll_fex_sbert import get_pyll_fex_sbert
from ._get_pyll_fex_tfidf import get_pyll_fex_tfidf
from ._get_pyll_qry_cluster import get_pyll_qry_cluster
from ._get_pyll_qry_max import get_pyll_qry_max
from ._get_pyll_qry_mixed import get_pyll_qry_mixed
from ._get_pyll_qry_random import get_pyll_qry_random
from ._get_pyll_qry_uncertainty import get_pyll_qry_uncertainty


def get_pyll(name):
    return {
        "bal-double": get_pyll_bal_double,
        "bal-simple": get_pyll_bal_simple,
        "bal-undersample": get_pyll_bal_undersample,
        "cls-logistic": get_pyll_cls_logistic,
        "cls-nb": get_pyll_cls_nb,
        "cls-nn-2-layer": get_pyll_cls_nn_2_layer,
        "cls-rf": get_pyll_cls_rf,
        "cls-svm": get_pyll_cls_svm,
        "fex-doc2vec": get_pyll_fex_doc2vec,
        "fex-sbert": get_pyll_fex_sbert,
        "fex-tfidf": get_pyll_fex_tfidf,
        "qry-cluster": get_pyll_qry_cluster,
        "qry-max": get_pyll_qry_max,
        "qry-mixed": get_pyll_qry_mixed,
        "qry-random": get_pyll_qry_random,
        "qry-uncertainty": get_pyll_qry_uncertainty,
    }[name]()
