import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_with_default_settings():
    runner = CliRunner()
    args = [
        "print-settings",
        "--pretty",
    ]
    result = runner.invoke(cli, args)
    assert result.exit_code == 0
    assert (
        result.output
        == """{
    "bal": {
        "abbr": "bal-double",
        "params": {
            "a": 2.155,
            "alpha": 0.94,
            "b": 0.789,
            "beta": 1.0
        }
    },
    "cls": {
        "abbr": "cls-nb",
        "params": {
            "alpha": 3.822
        }
    },
    "fex": {
        "abbr": "fex-tfidf",
        "params": {
            "ngram_max": 1,
            "split_ta": false,
            "stop_words": "english",
            "use_keywords": false
        }
    },
    "qry": {
        "abbr": "qry-max",
        "params": {
            "n_instances": 1
        }
    },
    "sam": {
        "abbr": "sam-random",
        "params": {
            "init_seed": null,
            "n_excluded": 1,
            "n_included": 1
        }
    },
    "stp": {
        "abbr": "stp-rel",
        "params": {}
    }
}
"""
    )
