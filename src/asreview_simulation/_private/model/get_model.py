from asreview_simulation._private.model.balancers.double import bal_double
from asreview_simulation._private.model.balancers.simple import bal_simple
from asreview_simulation._private.model.balancers.undersample import bal_undersample
from asreview_simulation._private.model.classifiers.logistic import cls_logistic
from asreview_simulation._private.model.classifiers.nb import cls_nb
from asreview_simulation._private.model.classifiers.nn_2_layer import cls_nn_2_layer
from asreview_simulation._private.model.classifiers.rf import cls_rf
from asreview_simulation._private.model.classifiers.svm import cls_svm
from asreview_simulation._private.model.extractors.doc2vec import fex_doc2vec
from asreview_simulation._private.model.extractors.sbert import fex_sbert
from asreview_simulation._private.model.extractors.tfidf import fex_tfidf
from asreview_simulation._private.model.queriers.cluster import qry_cluster
from asreview_simulation._private.model.queriers.max import qry_max
from asreview_simulation._private.model.queriers.max_random import qry_max_random
from asreview_simulation._private.model.queriers.max_uncertainty import qry_max_uncertainty
from asreview_simulation._private.model.queriers.random import qry_random
from asreview_simulation._private.model.queriers.uncertainty import qry_uncertainty
from asreview_simulation._private.model.samplers.handpicked import sam_handpicked
from asreview_simulation._private.model.samplers.random import sam_random
from asreview_simulation._private.model.stopping.none import stp_none
from asreview_simulation._private.model.stopping.nq import stp_nq
from asreview_simulation._private.model.stopping.rel import stp_rel


def get_model(name):
    funcmap = {
        "bal-double": bal_double,
        "bal-simple": bal_simple,
        "bal-undersample": bal_undersample,
        "cls-logistic": cls_logistic,
        "cls-nb": cls_nb,
        "cls-nn-2-layer": cls_nn_2_layer,
        "cls-rf": cls_rf,
        "cls-svm": cls_svm,
        "fex-doc2vec": fex_doc2vec,
        "fex-sbert": fex_sbert,
        "fex-tfidf": fex_tfidf,
        "qry-cluster": qry_cluster,
        "qry-max": qry_max,
        "qry-max-random": qry_max_random,
        "qry-max-uncertainty": qry_max_uncertainty,
        "qry-random": qry_random,
        "qry-uncertainty": qry_uncertainty,
        "sam-handpicked": sam_handpicked,
        "sam-random": sam_random,
        "stp-none": stp_none,
        "stp-nq": stp_nq,
        "stp-rel": stp_rel,
    }
    try:
        func = funcmap[name]
    except KeyError as e:
        names = "\n".join(list(funcmap.keys()))
        print(f"'{name}' is not a valid name for a model. Valid names are:\n{names}")
        raise e
    return func()
