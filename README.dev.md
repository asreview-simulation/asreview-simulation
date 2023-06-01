# Developer notes

## Running pre-commit on unstaged files

```
pip install --editable .[dev]
pre-commit run --all-files
```

## Publishing releases to Zenodo

TODO:

- get a personal access token from Zenodo specifically for this project
- add it to the repo secrets as ZENODO_ACCESS_TOKEN
- use the zenodraft workflow to make the release
- check the draft on zenodo, click publish there
- update the workflow with the collection doi


