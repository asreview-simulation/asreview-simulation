import json
import pytest
from click.testing import CliRunner
from asreview_simulation.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_rf
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
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
    assert "class_weight" in params
    assert classifier["params"]["class_weight"] == 1
    assert "max_features" in params
    assert classifier["params"]["max_features"] == 10
    assert "n_estimators" in params
    assert classifier["params"]["n_estimators"] == 100
