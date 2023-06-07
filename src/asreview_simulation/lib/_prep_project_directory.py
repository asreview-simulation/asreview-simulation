from pathlib import Path
from asreview.project import ASReviewProject
from asreview.data import load_data


def prep_project_directory(asreview_file, dataset):
    # Prepare an *.asreview.tmp directory which will contain the log / state / configuration
    # of the ASReview analysis. The directory will be zipped later and renamed to *.asreview
    name = Path(asreview_file).stem
    project_path = Path(asreview_file).with_suffix(".asreview.tmp")
    project = ASReviewProject.create(
        project_path,
        project_id=name,
        project_name=name,
        project_mode="simulate",
        project_description="Simulation created via ASReview command line interface",
    )

    # Add the dataset to the project directory.
    as_data = load_data(dataset)
    if len(as_data) == 0:
        raise ValueError("Supply at least one dataset with at least one record.")
    dataset_path = (
        f"{dataset[10:]}.csv" if dataset.startswith("benchmark:") else f"{dataset}.csv"
    )
    as_data.to_file(project_path / "data" / dataset_path)

    # Write settings to settings.json
    project.update_config(dataset_path=dataset_path)
    return project, as_data
