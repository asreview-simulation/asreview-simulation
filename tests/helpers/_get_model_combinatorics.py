import itertools
from asreview.models.classifiers import list_classifiers
from asreview.models.feature_extraction import list_feature_extraction


def get_model_combinatorics():
    fexs = [fex.name for fex in list_feature_extraction()]
    clss = [cls.name for cls in list_classifiers()]
    return [",".join(combo) for combo in itertools.product(*[fexs, clss])]
