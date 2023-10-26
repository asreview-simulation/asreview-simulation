import json
import pytest
from click.testing import CliRunner
from asreview_simulation.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_svm
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_svm_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "cls-svm",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "svm"
    params = classifier["params"].keys()
    assert "C" in params
    assert classifier["params"]["C"] == 15.4
    assert "class_weight" in params
    assert classifier["params"]["class_weight"] == 0.249
    assert "gamma" in params
    assert classifier["params"]["gamma"] == "auto"
    assert "kernel" in params
    assert classifier["params"]["kernel"] == "linear"
