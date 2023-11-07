from asreview_simulation._private.bal_double_pyll import bal_double_pyll
from asreview_simulation._private.bal_simple_pyll import bal_simple_pyll
from asreview_simulation._private.bal_undersample_pyll import bal_undersample_pyll
from asreview_simulation._private.cls_logistic_pyll import cls_logistic_pyll
from asreview_simulation._private.cls_nb_pyll import cls_nb_pyll
from asreview_simulation._private.cls_nn_2_layer_pyll import cls_nn_2_layer_pyll
from asreview_simulation._private.cls_rf_pyll import cls_rf_pyll
from asreview_simulation._private.cls_svm_pyll import cls_svm_pyll
from asreview_simulation._private.fex_doc2vec_pyll import fex_doc2vec_pyll
from asreview_simulation._private.fex_sbert_pyll import fex_sbert_pyll
from asreview_simulation._private.fex_tfidf_pyll import fex_tfidf_pyll
from asreview_simulation._private.qry_cluster_pyll import qry_cluster_pyll
from asreview_simulation._private.qry_max_pyll import qry_max_pyll
from asreview_simulation._private.qry_max_random_pyll import qry_max_random_pyll
from asreview_simulation._private.qry_max_uncertainty_pyll import qry_max_uncertainty_pyll
from asreview_simulation._private.qry_random_pyll import qry_random_pyll
from asreview_simulation._private.qry_uncertainty_pyll import qry_uncertainty_pyll
from asreview_simulation._private.sam_handpicked_pyll import sam_handpicked_pyll
from asreview_simulation._private.sam_random_pyll import sam_random_pyll
from asreview_simulation._private.stp_none_pyll import stp_none_pyll
from asreview_simulation._private.stp_nq_pyll import stp_nq_pyll
from asreview_simulation._private.stp_rel_pyll import stp_rel_pyll


def get_pyll(name):
    funcmap = {
        "bal-double": bal_double_pyll,
        "bal-simple": bal_simple_pyll,
        "bal-undersample": bal_undersample_pyll,
        "cls-logistic": cls_logistic_pyll,
        "cls-nb": cls_nb_pyll,
        "cls-nn-2-layer": cls_nn_2_layer_pyll,
        "cls-rf": cls_rf_pyll,
        "cls-svm": cls_svm_pyll,
        "fex-doc2vec": fex_doc2vec_pyll,
        "fex-sbert": fex_sbert_pyll,
        "fex-tfidf": fex_tfidf_pyll,
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
