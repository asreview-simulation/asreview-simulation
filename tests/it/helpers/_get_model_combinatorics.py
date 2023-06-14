import itertools
from asreview.models.balance import list_balance_strategies
from asreview.models.classifiers import list_classifiers
from asreview.models.feature_extraction import list_feature_extraction
from asreview.models.query import list_query_strategies


def get_model_combinatorics():
    bals = ["double"]  # [elem.name for elem in list_balance_strategies()]
    clss = [elem.name for elem in list_classifiers()]
    fexs = [elem.name for elem in list_feature_extraction()]
    qrys = ["max"]  # [elem.name for elem in list_query_strategies()]
    return [",".join(combo) for combo in itertools.product(*[bals, clss, fexs, qrys])]
