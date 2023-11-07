from pathlib import Path
from asreview.data import load_data
from asreview.project import ASReviewProject


def prep_project_directory(benchmark: str | None, input_file: Path | None, output_file: Path):
    # Prepare an *.asreview.tmp directory which will contain the log / state / configuration
    # of the ASReview analysis. The directory will be zipped later and renamed to *.asreview
    if benchmark is not None:
        assert isinstance(benchmark, str), "expected input argument 'benchmark' to be of type str"
    if input_file is not None:
        assert isinstance(input_file, Path), "expected input argument 'input_file' to be of type pathlib.Path"
    assert isinstance(output_file, Path), "expected input argument 'output_file' to be of type pathlib.Path"
    assert output_file.suffix == ".asreview", "OUTPUT_FILE should have '.asreview' filename extension."
    assert not output_file.exists(), f"Output file '{output_file}'  already exists."
    output_file_tmp = output_file.with_suffix(".asreview.tmp")
    assert not output_file_tmp.exists(), f"Temporary file '{output_file_tmp}'  already exists."

    case = input_file is None, benchmark is None
    if case == (True, True):
        raise ValueError("Neither '--in' nor '--benchmark' was specified.")
    elif case == (True, False):
        # Use --benchmark as the source
        as_data = load_data(benchmark)
        if benchmark.startswith("benchmark:"):
            dataset_path = f"{benchmark[10:]}.csv"
        else:
            dataset_path = f"{benchmark}.csv"
        if len(as_data) == 0:
            raise ValueError("Choose a benchmark dataset with at least one record.")
    elif case == (False, True):
        # Use --in as the source
        as_data = load_data(input_file)
        dataset_path = str(Path(input_file).with_suffix(".csv").name)
        if len(as_data) == 0:
            raise ValueError("Supply data with at least one record.")
    elif case == (False, False):
        msg = "Expected either '--in' or '--benchmark' to be specified, found both."
        raise ValueError(msg)
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
