# Developer notes

## Install

```shell
mkdir <a directory>
git clone https://github.com/asreview-tuning/asreview-simulation .
python3 -m venv venv
source venv/bin/activate
pip install --editable .
```

There are various sets of dependencies that you should install depending on the work you're planning to do. 

```shell
pip install --editable .[testing]
```

```shell
pip install --editable .[linting]
```

```shell
pip install --editable .[publishing]
```

```shell
pip install --editable .[doc2vec]
```

```shell
pip install --editable .[sbert]
```

```shell
pip install --editable .[tensorflow]
```

You can combine these into one command like so, e.g.:

```shell
pip install --editable .[linting,testing]
```

## Linting

Running pre-commit on unstaged files

```
pip install --editable .[linting]
pre-commit run --all-files
```

## Testing

There are various types of test: unit, mocked and it, each with their respective subdirectory. They can be run locally (requires `pip install .[testing]`), but can can also be run on GitHub via a GitHub action workflow `.github/workflows/testing.yml`. The workflow tests whether the tests pass for all combinations of operating system, asreview version, and python version.   

### `tests/unit`

These tests are simlpe, quick to run, and mostly focus on whether the `asreview-simulation` subcommands manipulate the state (`obj`) in the correct way. The idea of the "unit" in unit testing is that when the test fails, there is just one thing that could have gone wrong. This is in contrast to other types of test, e.g. integration testing (see below).  

### `tests/mocked`

The mocked tests verifies whether the arguments that `SimulateReview` receives inside `asreview`'s `SimulateEntrypoint` module are the same arguments as what `SimulateReview` in `asreview_simulate` receives. The simulation inside these tests just do the setting up of a simulation, but they do not run. This makes them faster than the integration tests (see below), but naturally, the simulation does not generate output files, so there are no results to compare.

### `tests/it`

These are the most extensive type of tests, that set up a simulation using `asreview simulate`, then set up the same simulation using `asreview simulation [options] start`, then compare the resulting files (`project.json`, `data/<dataset>.csv`, `reviews/<id>/results.sql`, and `reviews/<id>/settings_metadata.json`, but not feature_matrices/<extractor-method>_feature_matrix.npz at the moment).

## Publishing: Preparation

TODO

- unit tests pass
- mocked tests pass
- integration tests pass
- citation metadata is up to date
- version is consistent across the repository
- source dist can be built
- wheel dist can be built

## Publishing: Zenodo

The repository has a GitHub action `zenodraft.yml` which can be triggered manually to publish a snapshot
of the current repository contents (`main` branch) to Zenodo as a zipped archive. The workflow does not
finalize the resulting deposition on Zenodo, so that the repository admin has a chance to review the draft
deposition before making it final by pressing the "Publish" button on Zenodo.

## Publishing: GitHub

Click the "Draft a new release" button on the releases page
[https://github.com/asreview-tuning/asreview-simulation/releases](https://github.com/asreview-tuning/asreview-simulation/releases).
Making a release is not set up to also trigger the zenodraft workflow.

## Publishing: PyPI

TODO

## notes

- https://stackoverflow.com/questions/70984166/why-naive-bayes-gives-results-and-on-training-and-test-but-gives-error-of-negati
- provides a standalone CLI command `asreview-simulation`
- provides a plugin to `asreview` where it will show up as the subcommand `simulation` so users can call `asreview simulation` (i.e. without the dash)
- its functionality can be extended by plugins:
    - new balancer subcommands via entry point group `"asreview_simulation.balancers"`
    - new classifier subcommands via entry point group `"asreview_simulation.classifiers"`
    - new extractor subcommands via entry point group `"asreview_simulation.extractors"`
    - new querier subcommands via entry point group `"asreview_simulation.queriers"`
