from asreviewcontrib.simulation.api import Config


def test_flattened():
    config = Config()
    actual = config.flattened()
    assert isinstance(actual, dict)
    expected = {
        "bal-double/a": 2.155,
        "bal-double/alpha": 0.94,
        "bal-double/b": 0.789,
        "bal-double/beta": 1.0,
        "cls-nb/alpha": 3.822,
        "fex-tfidf/ngram_max": 1,
        "fex-tfidf/split_ta": False,
        "fex-tfidf/stop_words": "english",
        "fex-tfidf/use_keywords": False,
        "qry-max/n_instances": 1,
        "sam-random/init_seed": None,
        "sam-random/n_excluded": 1,
        "sam-random/n_included": 1,
    }
    assert actual == expected
