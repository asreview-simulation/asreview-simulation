import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_doc2vec
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_doc2vec_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex-doc2vec",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["abbr"] == "doc2vec"
    params = extractor["params"].keys()
    expected_pairs = [
        ("dbow_words", 0),
        ("dm", 2),
        ("dm_concat", 0),
        ("epochs", 33),
        ("min_count", 1),
        ("split_ta", 0),
        ("use_keywords", 0),
        ("vector_size", 40),
        ("window", 7),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of feature extractor."
        assert extractor["params"][param] == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
