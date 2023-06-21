import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_embedding_idf_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex-embedding-idf",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["abbr"] == "embedding-idf"
    params = extractor["params"].keys()
    assert len(params) == 0
