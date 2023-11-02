import json
import pytest
from click.testing import CliRunner
from asreview_simulation.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_logistic
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_logistic_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "cls-logistic",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "logistic"
    params = classifier["params"].keys()
    expected_pairs = [
        ("C", 1.0),
        ("class_weight", 1.0),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of classifier."
        assert classifier["params"][param] == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
