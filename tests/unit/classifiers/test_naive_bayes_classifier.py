import json
from click.testing import CliRunner
from asreview_simulation.cli import cli
import pytest


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_naive_bayes_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "cls-nb",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "nb"
    params = classifier["params"].keys()
    assert "alpha" in params
    assert classifier["params"]["alpha"] == 3.822
