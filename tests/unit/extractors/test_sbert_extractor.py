import json
import pytest
from click.testing import CliRunner
from asreview_simulation.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_sbert
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_sbert_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex-sbert",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["abbr"] == "sbert"
    params = extractor["params"].keys()
    expected_pairs = [
        ("split_ta", 0),
        ("transformer_model", "all-mpnet-base-v2"),
        ("use_keywords", 0),
    ]
    assert not (len(params) < len(expected_pairs)), "Missing parameter"
    assert not (len(params) > len(expected_pairs)), "Unexpected extra parameter"

    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of feature extractor."
        assert extractor["params"][param] == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
