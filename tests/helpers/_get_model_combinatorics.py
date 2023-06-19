import itertools
from asreview.models.classifiers import list_classifiers
from asreview.models.feature_extraction import list_feature_extraction


def get_model_combinatorics():
    bals = ["double"]
    clss = [cls.name for cls in list_classifiers()]
    fexs = [fex.name for fex in list_feature_extraction()]
    qrys = ["max"]
    return [",".join(combo) for combo in itertools.product(*[bals, clss, fexs, qrys])]
