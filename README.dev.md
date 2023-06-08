# Developer notes

## Dependencies

There are various sets of dependencies that you should install depending on the work you're planning to do. 

```shell
pip install .[testing]
```

```shell
pip install .[linting]
```

```shell
pip install .[doc2vec]
```

```shell
pip install .[sbert]
```

```shell
pip install .[tensorflow]
```

You can combine these into one command like so, e.g.:
```shell
pip install .[linting,testing]
```

## Running pre-commit on unstaged files

```
pip install --editable .[linting]
pre-commit run --all-files
```


## Publishing releases to Zenodo

TODO:

- get a personal access token from Zenodo specifically for this project
- add it to the repo secrets as ZENODO_ACCESS_TOKEN
- use the zenodraft workflow to make the release
- check the draft on zenodo, click publish there
- update the workflow with the collection doi
