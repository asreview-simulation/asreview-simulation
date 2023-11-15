from pathlib import Path
from asreview.data import ASReviewData
from asreview.data import load_data
from asreview.project import ASReviewProject


def prep_project_directory(
    benchmark: str | None = None, input_file: str | None = None, output_file: str | None = None
) -> (ASReviewProject, ASReviewData):
    # Prepare an *.asreview.tmp directory which will contain the log / state / configuration
    # of the ASReview analysis. The directory will be zipped later and renamed to *.asreview
    assert (benchmark is None) != (input_file is None), "Need to specify either 'benchmark' or 'input_file'"
    if benchmark is not None:
        assert isinstance(benchmark, str), "expected input argument 'benchmark' to be of type str"
    if input_file is not None:
        assert isinstance(input_file, str), "expected input argument 'input_file' to be of type str"
    if output_file is not None:
        assert isinstance(output_file, str), "expected input argument 'output_file' to be of type str"
    else:
        assert False, "Need to specify an output file"
    assert Path(output_file).suffix == ".asreview", "'output_file' should have '.asreview' filename extension."
    assert not Path(output_file).exists(), f"Output file '{output_file}'  already exists."
    output_file_tmp = Path(output_file).with_suffix(".asreview.tmp")
    assert not Path(output_file_tmp).exists(), f"Temporary file '{output_file_tmp}'  already exists."

    if input_file is None:
        # Use --benchmark as the source
        as_data = load_data(benchmark)
        if benchmark.startswith("benchmark:"):
            dataset_path = f"{benchmark[10:]}.csv"
        else:
            dataset_path = f"{benchmark}.csv"
        if len(as_data) == 0:
            raise ValueError("Choose a benchmark dataset with at least one record.")
    elif benchmark is None:
        # Use --in as the source
        as_data = load_data(input_file)
        dataset_path = str(Path(input_file).with_suffix(".csv").name)
        if len(as_data) == 0:
            raise ValueError("Supply data with at least one record.")
    else:
        raise ValueError("Unexpected case.")

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
