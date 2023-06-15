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

## Linting

Running pre-commit on unstaged files

```
pip install --editable .[linting]
pre-commit run --all-files
```

## Publishing releases to Zenodo

The reposiotry has a GitHub action `zenodraft.yml` which can be triggered manually to publish a snapshot
of the current repository contents (`main` branch) to Zenodo as a zipped archive. The workflow does not
finalize the resulting deposition on Zenodo, so that the repository admin has a chance to review the draft
deposition before making it final by pressing the "Publish" button on Zenodo.  

# notes

- https://stackoverflow.com/questions/70984166/why-naive-bayes-gives-results-and-on-training-and-test-but-gives-error-of-negati
- provides a standalone CLI command `asreview-simulation`
- provides a plugin to `asreview` where it will show up as the subcommand `simulation` so users can call `asreview simulation` (i.e. without the dash)
- its functionality can be extended by plugins:
    - new balancer subcommands via entry point group `"asreview_simulation.balancers"`
    - new classifier subcommands via entry point group `"asreview_simulation.classifiers"`
    - new extractor subcommands via entry point group `"asreview_simulation.extractors"`
    - new querier subcommands via entry point group `"asreview_simulation.queriers"`
    - new sampler subcommands via entry point group `"asreview_simulation.samplers"`
    - new starter subcommands via entry point group `"asreview_simulation.starters"`
    - new stopping subcommands via entry point group `"asreview_simulation.stopping"` 
    - new terminator subcommands via entry point group `"asreview_simulation.terminators"`
