from tempfile import TemporaryDirectory
from pathlib import Path
from asreview_simulation.api import ModelConfigs
from asreview_simulation.api import run
from asreview_simulation.api import prep_project_directory
from asreview_simulation.api import list_dataset_names


def run_use_case():
    models = ModelConfigs()
    benchmark = list_dataset_names()[4]
    with TemporaryDirectory(prefix="asreview-simulation.") as tmpdir:
        out_file = Path(tmpdir) / "simulate.asreview"
        project, as_data = prep_project_directory(benchmark, input_file=None, output_file=out_file)
        run(models, project, as_data)
        print("done")


if __name__ == "__main__":
    run_use_case()
