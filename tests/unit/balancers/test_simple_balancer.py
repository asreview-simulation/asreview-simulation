import json
import pytest
from click.testing import CliRunner
from asreview_simulation.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_simple
@pytest.mark.stp_min
def test_simple_balancer_default_parameterization():
    runner = CliRunner()
    args = [
        "bal-simple",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    balancer = json.loads(result.output)["balancer"]
    assert balancer["abbr"] == "simple"
    params = balancer["params"].keys()
    assert len(params) == 0
