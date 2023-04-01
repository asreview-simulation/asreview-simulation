# A fresh take on ASReview's project layout

## asreviewlib API

```text
# See `asreviewlib/test/test_api.py` for the complete programming interface.

asreviewlib.balancers.BaseBalancer
asreviewlib.balancers.DoubleBalancer
asreviewlib.balancers.SimpleBalancer
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

1. `list_balancers` looks for balancers added by entrypoint group `'balancers'`
2. `list_classifiers` looks for classifiers added by entrypoint group `'classifiers'`
3. `list_extractors` looks for extractors added by entrypoint group `'extractors'`
4. `list_queriers` looks for queriers added by entrypoint group `'queriers'`
5. `list_readers` looks for readers added by entrypoint group `'readers'`
6. `list_writers` looks for writers added by entrypoint group `'writers'`

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
