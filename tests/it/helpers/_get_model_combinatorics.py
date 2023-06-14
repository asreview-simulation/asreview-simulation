import itertools


def get_model_combinatorics():
    bals = ["double"]
    clss = ["logistic", "nb", "rf", "svm"]
    fexs = ["doc2vec", "tfidf"]
    qrys = ["max"]
    return [",".join(combo) for combo in itertools.product(*[bals, clss, fexs, qrys])]
