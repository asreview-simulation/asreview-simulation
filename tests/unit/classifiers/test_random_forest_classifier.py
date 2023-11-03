import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_rf
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_random_forest_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "cls-rf",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "rf"
    params = classifier["params"].keys()
    expected_pairs = [
        ("class_weight", 1.0),
        ("max_features", 10),
        ("n_estimators", 100),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of classifier."
        assert (
            classifier["params"][param] == expected_value
        ), f"Expected key '{param}' to have value '{expected_value}'."
