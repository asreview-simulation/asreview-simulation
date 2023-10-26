import json
from click.testing import CliRunner
from asreview_simulation.cli import cli
import pytest


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_lstm_base
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_lstm_base_classifier_default_parameterization(tmp_path):
    runner = CliRunner()
    args = [
        "cls-lstm-base",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "lstm-base"
    params = classifier["params"].keys()
    assert len(params) == 0
