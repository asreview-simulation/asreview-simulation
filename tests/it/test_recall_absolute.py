import os
from tempfile import TemporaryDirectory
from asreview import open_state
from asreviewcontrib.insights.metrics import recall as calc_recall
from asreviewcontrib.simulation.api import AllModelConfig
from asreviewcontrib.simulation.api import prep_project_directory
from asreviewcontrib.simulation.api import run


def test_recall_absolute():
    with TemporaryDirectory(prefix="tmp.ofn-testing.") as tmpdir:
        models = AllModelConfig()
        benchmark = "benchmark:Cohen_2006_ADHD"
        output_file = f"{tmpdir}{os.sep}project.asreview"
        project, as_data = prep_project_directory(benchmark=benchmark, output_file=output_file)
        run(models, project, as_data)

        with open_state(output_file) as s:
            actual = calc_recall(s, 0)
            assert actual is not None
