import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_embedding_idf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_embedding_idf_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex-embedding-idf",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["abbr"] == "embedding-idf"
    params = extractor["params"].keys()
    expected_pairs = [
        ("embedding_fp", ""),
        ("split_ta", 0),
        ("use_keywords", 0),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of feature extractor."
        assert extractor["params"][param] == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
