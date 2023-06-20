import itertools
from asreview.models.classifiers import list_classifiers
from asreview.models.feature_extraction import list_feature_extraction


def get_model_combinatorics():
    clss = [cls.name for cls in list_classifiers()]
    fexs = [fex.name for fex in list_feature_extraction()]
    return [",".join(combo) for combo in itertools.product(*[clss, fexs])]
