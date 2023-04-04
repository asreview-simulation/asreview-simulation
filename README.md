# A fresh take on ASReview's project layout

## `asreviewlib` API

```text
# See `asreviewlib/test/test_api.py` for the complete programming interface.

asreviewlib.balancers.BaseBalancer
asreviewlib.balancers.DoubleBalancer
asreviewlib.balancers.NoneBalancer
asreviewlib.balancers.TripleBalancer
asreviewlib.balancers.UndersampleBalancer
asreviewlib.balancers
asreviewlib.BaseModel
asreviewlib.classifiers.BaseClassifier
asreviewlib.classifiers.LogisticClassifier
asreviewlib.classifiers.LstmBaseClassifier
asreviewlib.classifiers.LstmPoolClassifier
asreviewlib.classifiers.NaiveBayesClassifier
asreviewlib.classifiers.NN2LayerClassifier
asreviewlib.classifiers.RandomForestClassifier
asreviewlib.classifiers.SvmClassifier
asreviewlib.classifiers
asreviewlib.Data
asreviewlib.demo_d.fun
asreviewlib.demo_d
asreviewlib.exceptions.ASReviewProjectExistsError
asreviewlib.exceptions.ASReviewProjectNotFoundError
asreviewlib.exceptions
asreviewlib.extractors.BaseExtractor
asreviewlib.extractors.Doc2VecExtractor
asreviewlib.extractors.EmbeddingIdfExtractor
asreviewlib.extractors.EmbeddingLstmExtractor
asreviewlib.extractors.SbertExtractor
asreviewlib.extractors.TfidfExtractor
asreviewlib.extractors
asreviewlib.list_balancers
asreviewlib.list_classifiers
asreviewlib.list_extractors
asreviewlib.list_projects
asreviewlib.list_queriers
asreviewlib.list_readers
asreviewlib.list_writers
asreviewlib.Project
asreviewlib.queriers.BaseQuerier
asreviewlib.queriers.ClusterQuerier
asreviewlib.queriers.MaxQuerier
asreviewlib.queriers.MaxRandomQuerier
asreviewlib.queriers.MaxUncertaintyQuerier
asreviewlib.queriers.MixedQuerier
asreviewlib.queriers.RandomQuerier
asreviewlib.queriers.UncertaintyQuerier
asreviewlib.queriers
asreviewlib.readers.CsvReader
asreviewlib.readers.RisReader
asreviewlib.readers.TsvReader
asreviewlib.readers.XlsReader
asreviewlib.readers
asreviewlib.state.create_database
asreviewlib.state.create_event
asreviewlib.state.create_record
asreviewlib.state.delete_database
asreviewlib.state.delete_event
asreviewlib.state.delete_record
asreviewlib.state.read_database
asreviewlib.state.read_event
asreviewlib.state.read_record
asreviewlib.state.update_database
asreviewlib.state.update_event
asreviewlib.state.update_record
asreviewlib.state
asreviewlib.writers.CsvWriter
asreviewlib.writers.RisWriter
asreviewlib.writers.TsvWriter
asreviewlib.writers.XlsWriter
asreviewlib.writers

```

## Avoiding unintentional reexports with private module pattern

```shell
python3 -m venv venv
source venv/bin/activate
pip install --editable ./asreviewlib/[test]
python3
>>> import asreviewlib
>>> asreviewlib.demo_d  # works
>>> asreviewlib.demo_d.fun()
module demo/_demo.py imports built-in module 'sys': <module 'sys' (built-in)>
>>> dir(asreviewlib.demo_d)  # has fun, but not sys
Ctrl-D
pytest asreviewlib # all tests pass 
```

Let's change it so `asreviewlib` uses `fun` from `demo_f` instead of from `demo_d/_demo.py`:

- `asreviewlib.__init__.py` update `import` and `__all__`
- `tests.test_api.py` update references to `demo_f`.

```shell
python3 -m venv venv
source venv/bin/activate
pip install --editable ./asreviewlib/[test]
python3
>>> import asreviewlib
>>> asreviewlib.demo_f  # works
>>> asreviewlib.demo_f.fun()
module demo.py imports built-in module 'sys': <module 'sys' (built-in)>
>>> dir(asreviewlib.demo_f)  # has fun, as well as sys 
Ctrl-D
pytest asreviewlib # should fail with messages about sys
```

## Extending `asreviewlib`

The `list_*` functions from `asreviewlib` can be extended in a few predefined ways using plugins:

1. `list_balancers` looks for balancers added by entrypoint group `'asreviewlib.balancers'`
2. `list_classifiers` looks for classifiers added by entrypoint group `'asreviewlib.classifiers'`
3. `list_extractors` looks for extractors added by entrypoint group `'asreviewlib.extractors'`
4. `list_queriers` looks for queriers added by entrypoint group `'asreviewlib.queriers'`
5. `list_readers` looks for readers added by entrypoint group `'asreviewlib.readers'`
6. `list_writers` looks for writers added by entrypoint group `'asreviewlib.writers'`

```shell
python3 -m venv venv
source venv/bin/activate
pip install --editable ./asreviewlib
python3
>>> import asreviewlib
>>> for k, v in asreviewlib.list_classifiers().items(): print(v)
... 
<class 'asreviewlib.classifiers._logistic_classifier.LogisticClassifier'>
<class 'asreviewlib.classifiers._lstm_base_classifier.LstmBaseClassifier'>
<class 'asreviewlib.classifiers._lstm_pool_classifier.LstmPoolClassifier'>
<class 'asreviewlib.classifiers._naive_bayes_classifier.NaiveBayesClassifier'>
<class 'asreviewlib.classifiers._nn_2_layer_classifier.NN2LayerClassifier'>
<class 'asreviewlib.classifiers._random_forest_classifier.RandomForestClassifier'>
<class 'asreviewlib.classifiers._svm_classifier.SvmClassifier'>
Ctrl-D
pip install --editable ./asreviewlib-plugin-classifier
python3
>>> import asreviewlib
>>> for k, v in asreviewlib.list_classifiers().items(): print(v)
... 
<class 'asreviewlib.classifiers._logistic_classifier.LogisticClassifier'>
<class 'asreviewlib.classifiers._lstm_base_classifier.LstmBaseClassifier'>
<class 'asreviewlib.classifiers._lstm_pool_classifier.LstmPoolClassifier'>
<class 'asreviewlib.classifiers._naive_bayes_classifier.NaiveBayesClassifier'>
<class 'asreviewlib.classifiers._nn_2_layer_classifier.NN2LayerClassifier'>
<class 'asreviewlib.classifiers._random_forest_classifier.RandomForestClassifier'>
<class 'asreviewlib.classifiers._svm_classifier.SvmClassifier'>
<class 'asreviewlib_plugin_classifier._new_classifier.NewClassifier'>
```

## `asreview-cli`

Print the help:

```shell
$ asreview-cli --help
Usage: asreview-cli [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

  Example usage:

    $ asreview-cli print-settings

    $ asreview-cli start labeled-records.db

  Commands can be chained together, e.g.

    $ asreview-cli load-config thefile.cfg start labeled-records.db

    $ asreview-cli bal:double --alpha 1.23 print-settings --pretty

    $ asreview-cli bal:none c-nb e-tfidf q-mixed start labeled-records.db

    $ asreview-cli sam:random --n_included 10 --n_excluded 15                      \
                   ext:tfidf --ngram_max 2                                         \
                   cls:nb --alpha 3.823                                            \
                   qer:mixed --strategy1 max --strategy2 random --mix_ratio 0.95   \
                   bal:double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1           \
                   start labeled-records.db

  Chained commands are evaluated left to right; make sure to end the chain
  with either a 'start' command or a 'print-settings' command, otherwise it
  appears like nothing is happening.

Options:
  --help  Show this message and exit.

Commands:
  bal:double          Use double balancer
  bal:none            Use no balancer
  bal:triple          Use triple balancer
  bal:undersample     Use undersample balancer
  cls:logistic        Use Logistic Regression classifier
  cls:lstm-base       Use LSTM Base classifier
  cls:lstm-pool       Use LSTM Pool classifier
  cls:nb              Use Naive Bayes classifier
  cls:nn-2-layer      Use 2-layer Neural Net classifier
  cls:rf              Use Random Forest classifier
  cls:svm             Use Support Vector Machine classifier
  ext:doc2vec         Use Doc2Vec extractor
  ext:embedding-idf   Use Embedding IDF extractor
  ext:embedding-lstm  Use Embedding LSTM extractor
  ext:sbert           Use SBERT extractor
  ext:tfidf           Use TF-IDF extractor
  load-config         Load config
  print-settings      Print settings
  qer:cluster         Use Cluster querier
  qer:mixed           Use Mixed querier
  sam:handpicked      Use handpicked prior sampler
  sam:random          Use random prior sampler
  start               Start the simulation and exit; terminates parsing
```

Print the default settings:

```shell
$ asreview-cli print-settings --pretty
{
    "balancer": {
        "model": "double",
        "params": {
            "a": 2.155,
            "alpha": 0.94,
            "b": 0.789,
            "beta": 1.0
        }
    },
    "classifier": {
        "model": "nb",
        "params": {
            "alpha": 3.822
        }
    },
    "extractor": {
        "model": "tfidf",
        "params": {
            "ngrams_max": 1,
            "stop_words": "english"
        }
    },
    "sampler": {
        "model": "random",
        "params": {
            "n_excluded": 1,
            "n_included": 1
        }
    },
    "querier": {
        "model": "max",
        "params": {}
    }
}
```

Print the help for a subcommand, e.g. for triple balancer:

```shell
$ asreview-cli bal:triple --help

Usage: asreview-cli bal:triple [OPTIONS]

  Use triple balancer

Options:
  --a FLOAT      hyperparameter 'a'.  [default: 2.155]
  --alpha FLOAT  hyperparameter 'alpha'.  [default: 0.94]
  --b FLOAT      hyperparameter 'b'.  [default: 0.789]
  --beta FLOAT   hyperparameter 'beta'.  [default: 1.0]
  --c FLOAT      hyperparameter 'c'.  [default: 0.835]
  -f, --force    Force setting the querier configuration, even if that means
                 overwriting a previous configuration.
  --gamma FLOAT  hyperparameter 'gamma'.  [default: 2.0]
  --shuffle      hyperparameter 'shuffle'.
  --help         Show this message and exit.

  This command is chainable with other commands. Chained commands are
  evaluated left to right; make sure to end the chain with either a 'start'
  command or a 'print-settings' command, otherwise it appears like nothing is
  happening.
```

Change the settings by chaining subcommands and printing them at the end:

```shell
$ asreview-cli bal:undersample --ratio 0.5 c-rf --class_weight 1.0001 print-settings --pretty
{
    "balancer": {
        "model": "undersample",
        "params": {
            "ratio": 0.5
        }
    },
    "classifier": {
        "model": "rf",
        "params": {
            "class_weight": 1.0001,
            "max_features": 10,
            "n_estimators": 100,
        }
    },
    "extractor": {
        "model": "tfidf",
        "params": {
            "n_gram_max": 1,
            "stop_words": "english"
        }
    },
    "sampler": {
        "model": "random",
        "params": {
            "n_excluded": 1,
            "n_included": 1
        }
    },
    "querier": {
        "model": "max",
        "params": {}
    }
}
```
