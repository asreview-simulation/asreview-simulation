from pathlib import Path
from asreview.data import load_data
from asreview.project import ASReviewProject


def prep_project_directory(data, dataset, output_file):
    # Prepare an *.asreview.tmp directory which will contain the log / state / configuration
    # of the ASReview analysis. The directory will be zipped later and renamed to *.asreview

    assert output_file.endswith(
        ".asreview"
    ), "OUTPUT_FILE should have '.asreview' filename extension."

    case = data is None, dataset is None
    if case == (True, True):
        raise ValueError("Neither '--data' nor '--dataset' was specified.")
    elif case == (True, False):
        # Use --dataset as the source
        as_data = load_data(dataset)
        if dataset.startswith("benchmark:"):
            dataset_path = f"{dataset[10:]}.csv"
        else:
            dataset_path = f"{dataset}.csv"
    elif case == (False, True):
        # Use --data as the source
        as_data = load_data(data)
        dataset_path = str(Path(data).name)
    elif case == (False, False):
        msg = "Expected either '--data' or '--dataset' to be specified, found both."
        raise ValueError(msg)
    else:
        raise ValueError("Unexpected case.")

    if len(as_data) == 0:
        raise ValueError("Supply at least one dataset with at least one record.")

    # Create the .asreview.tmp directory
    name = Path(output_file).stem
    project_path = Path(output_file).with_suffix(".asreview.tmp")
    project = ASReviewProject.create(
        project_path,
        project_id=name,
        project_name=name,
        project_mode="simulate",
        project_description="Simulation created via ASReview command line interface",
    )

    # Include a copy of the input data in the .asreview.tmp directory
    as_data.to_file(project_path / "data" / dataset_path)

    # Include the settings in the .asreview.tmp directory
    project.update_config(dataset_path=dataset_path)

    return project, as_data
