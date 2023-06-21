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

TODO

### `tests/unit`

TODO

### `tests/mocked`

TODO

### `tests/it`

TODO

## Publishing

The software is published to various platforms, for details see the sections below.

### Preparation

TODO

- unit tests pass
- mocked tests pass
- integration tests pass
- citation metadata is up to date
- version is consistent across the repository
- source dist can be built
- wheel dist can be built

### Zenodo

The repository has a GitHub action `zenodraft.yml` which can be triggered manually to publish a snapshot
of the current repository contents (`main` branch) to Zenodo as a zipped archive. The workflow does not
finalize the resulting deposition on Zenodo, so that the repository admin has a chance to review the draft
deposition before making it final by pressing the "Publish" button on Zenodo.

### GitHub

Click the "Draft a new release" button on the releases page
[https://github.com/asreview-tuning/asreview-simulation/releases](https://github.com/asreview-tuning/asreview-simulation/releases).
Making a release is not set up to also trigger the zenodraft workflow.

### PyPI

TODO

# notes

- https://stackoverflow.com/questions/70984166/why-naive-bayes-gives-results-and-on-training-and-test-but-gives-error-of-negati
- provides a standalone CLI command `asreview-simulation`
- provides a plugin to `asreview` where it will show up as the subcommand `simulation` so users can call `asreview simulation` (i.e. without the dash)
- its functionality can be extended by plugins:
    - new balancer subcommands via entry point group `"asreview_simulation.balancers"`
    - new classifier subcommands via entry point group `"asreview_simulation.classifiers"`
    - new extractor subcommands via entry point group `"asreview_simulation.extractors"`
    - new querier subcommands via entry point group `"asreview_simulation.queriers"`
