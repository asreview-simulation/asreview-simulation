from asreview_simulation._private.pyll.get_pyll_bal_double import get_pyll_bal_double
from asreview_simulation._private.pyll.get_pyll_bal_simple import get_pyll_bal_simple
from asreview_simulation._private.pyll.get_pyll_bal_undersample import get_pyll_bal_undersample
from asreview_simulation._private.pyll.get_pyll_cls_logistic import get_pyll_cls_logistic
from asreview_simulation._private.pyll.get_pyll_cls_nb import get_pyll_cls_nb
from asreview_simulation._private.pyll.get_pyll_cls_nn_2_layer import get_pyll_cls_nn_2_layer
from asreview_simulation._private.pyll.get_pyll_cls_rf import get_pyll_cls_rf
from asreview_simulation._private.pyll.get_pyll_cls_svm import get_pyll_cls_svm
from asreview_simulation._private.pyll.get_pyll_fex_doc2vec import get_pyll_fex_doc2vec
from asreview_simulation._private.pyll.get_pyll_fex_sbert import get_pyll_fex_sbert
from asreview_simulation._private.pyll.get_pyll_fex_tfidf import get_pyll_fex_tfidf
from asreview_simulation._private.pyll.get_pyll_qry_cluster import get_pyll_qry_cluster
from asreview_simulation._private.pyll.get_pyll_qry_max import get_pyll_qry_max
from asreview_simulation._private.pyll.get_pyll_qry_max_random import get_pyll_qry_max_random
from asreview_simulation._private.pyll.get_pyll_qry_max_uncertainty import get_pyll_qry_max_uncertainty
from asreview_simulation._private.pyll.get_pyll_qry_random import get_pyll_qry_random
from asreview_simulation._private.pyll.get_pyll_qry_uncertainty import get_pyll_qry_uncertainty
from asreview_simulation._private.pyll.get_pyll_sam_handpicked import get_pyll_sam_handpicked
from asreview_simulation._private.pyll.get_pyll_sam_random import get_pyll_sam_random
from asreview_simulation._private.pyll.get_pyll_stp_min import get_pyll_stp_min
from asreview_simulation._private.pyll.get_pyll_stp_none import get_pyll_stp_none
from asreview_simulation._private.pyll.get_pyll_stp_nq import get_pyll_stp_nq


def get_pyll(name):
    funcmap = {
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
        "qry-max-random": get_pyll_qry_max_random,
        "qry-max-uncertainty": get_pyll_qry_max_uncertainty,
        "qry-random": get_pyll_qry_random,
        "qry-uncertainty": get_pyll_qry_uncertainty,
        "sam-handpicked": get_pyll_sam_handpicked,
        "sam-random": get_pyll_sam_random,
        "stp-min": get_pyll_stp_min,
        "stp-none": get_pyll_stp_none,
        "stp-nq": get_pyll_stp_nq,
    }
    try:
        func = funcmap[name]
    except KeyError as e:
        names = "\n".join(list(funcmap.keys()))
        print(f"'{name}' is not a valid name for a model. Valid names are:\n{names}")
        raise e
    return func()
