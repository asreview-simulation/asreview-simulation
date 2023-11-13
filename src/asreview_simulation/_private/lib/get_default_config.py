from asreview_simulation._private.lib.bal.bal_double_config import get_bal_double_config
from asreview_simulation._private.lib.bal.bal_simple_config import get_bal_simple_config
from asreview_simulation._private.lib.bal.bal_undersample_config import get_bal_undersample_config
from asreview_simulation._private.lib.cls.cls_logistic_config import get_cls_logistic_config
from asreview_simulation._private.lib.cls.cls_nb_config import get_cls_nb_config
from asreview_simulation._private.lib.cls.cls_nn_2_layer_config import get_cls_nn_2_layer_config
from asreview_simulation._private.lib.cls.cls_rf_config import get_cls_rf_config
from asreview_simulation._private.lib.cls.cls_svm_config import get_cls_svm_config
from asreview_simulation._private.lib.fex.fex_doc2vec_config import get_fex_doc2vec_config
from asreview_simulation._private.lib.fex.fex_sbert_config import get_fex_sbert_config
from asreview_simulation._private.lib.fex.fex_tfidf_config import get_fex_tfidf_config
from asreview_simulation._private.lib.qry.qry_cluster_config import get_qry_cluster_config
from asreview_simulation._private.lib.qry.qry_max_config import get_qry_max_config
from asreview_simulation._private.lib.qry.qry_max_random_config import get_qry_max_random_config
from asreview_simulation._private.lib.qry.qry_max_uncertainty_config import get_qry_max_uncertainty_config
from asreview_simulation._private.lib.qry.qry_random_config import get_qry_random_config
from asreview_simulation._private.lib.qry.qry_uncertainty_config import get_qry_uncertainty_config
from asreview_simulation._private.lib.sam.sam_handpicked_config import get_sam_handpicked_config
from asreview_simulation._private.lib.sam.sam_random_config import get_sam_random_config
from asreview_simulation._private.lib.stp.stp_none_config import get_stp_none_config
from asreview_simulation._private.lib.stp.stp_nq_config import get_stp_nq_config
from asreview_simulation._private.lib.stp.stp_rel_config import get_stp_rel_config


def get_default_config(name):
    funcmap = {
        "bal-double": get_bal_double_config,
        "bal-simple": get_bal_simple_config,
        "bal-undersample": get_bal_undersample_config,
        "cls-logistic": get_cls_logistic_config,
        "cls-nb": get_cls_nb_config,
        "cls-nn-2-layer": get_cls_nn_2_layer_config,
        "cls-rf": get_cls_rf_config,
        "cls-svm": get_cls_svm_config,
        "fex-doc2vec": get_fex_doc2vec_config,
        "fex-sbert": get_fex_sbert_config,
        "fex-tfidf": get_fex_tfidf_config,
        "qry-cluster": get_qry_cluster_config,
        "qry-max": get_qry_max_config,
        "qry-max-random": get_qry_max_random_config,
        "qry-max-uncertainty": get_qry_max_uncertainty_config,
        "qry-random": get_qry_random_config,
        "qry-uncertainty": get_qry_uncertainty_config,
        "sam-handpicked": get_sam_handpicked_config,
        "sam-random": get_sam_random_config,
        "stp-none": get_stp_none_config,
        "stp-nq": get_stp_nq_config,
        "stp-rel": get_stp_rel_config,
    }
    try:
        func = funcmap[name]
    except KeyError as e:
        names = "\n".join(list(funcmap.keys()))
        print(f"'{name}' is not a valid name for a model. Valid names are:\n{names}")
        raise e
    return func()
