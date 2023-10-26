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
    assert "C" in params
    assert classifier["params"]["C"] == 1.0
    assert "class_weight" in params
    assert classifier["params"]["class_weight"] == 1.0
