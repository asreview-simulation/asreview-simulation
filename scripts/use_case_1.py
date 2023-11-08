import os
from tempfile import TemporaryDirectory
from asreview_simulation.api import list_dataset_names
from asreview_simulation.api import ModelConfigs
from asreview_simulation.api import prep_project_directory
from asreview_simulation.api import run


def run_use_case():
    models = ModelConfigs()
    benchmark = list_dataset_names()[4]
    with TemporaryDirectory(prefix="asreview-simulation.") as tmpdir:
        out_file = f"{tmpdir}{os.sep}simulate.asreview"
        project, as_data = prep_project_directory(benchmark, input_file=None, output_file=out_file)
        run(models, project, as_data)
        print("done")


if __name__ == "__main__":
    run_use_case()
