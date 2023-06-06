import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_cluster_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qer:cluster",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["model"] == "cluster"
    params = querier["params"].keys()
    assert "cluster_size" in params
    assert querier["params"]["cluster_size"] == 350
    assert "update_interval" in params
    assert querier["params"]["update_interval"] == 200
