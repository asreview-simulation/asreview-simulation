import json
from click.testing import CliRunner
from asreview_simulation.cli import cli
import pytest


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_lstm_pool
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_lstm_pool_classifier_default_parameterization(tmp_path):
    runner = CliRunner()
    args = [
        "cls-lstm-pool",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "lstm-pool"
    params = classifier["params"].keys()
    assert len(params) == 0
