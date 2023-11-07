import numpy
from asreview.state.sqlstate import SQLiteState
from tests.helpers.get_review_id import get_review_id


def compare_results_sql(p1, p2, test_metadata=False, test_prior_records=False, test_queried_records=False):
    state1 = SQLiteState(read_only=True)
    state1._restore(p1, get_review_id(p1))
    df1 = state1.get_dataset()

    state2 = SQLiteState(read_only=True)
    state2._restore(p2, get_review_id(p2))
    df2 = state2.get_dataset()

    columns = [
        "record_id",
        "label",
        "classifier",
        "query_strategy",
        "balance_strategy",
        "feature_extraction",
        "training_set",
    ]

    if test_metadata is True:
        assert state1.version == state2.version, "version not the same in results.sql metadata"
        assert state1.n_records == state2.n_records, "number of records not the same in results.sql metadata"
        assert state1.n_priors == state2.n_priors, "number of priors not the same in results.sql metadata"
    if test_prior_records is True:
        results1 = df1.loc[df1.query_strategy == "prior", columns].values
        results2 = df2.loc[df2.query_strategy == "prior", columns].values
        assert numpy.array_equal(results1, results2), "prior records not the same in results.sql"
    if test_queried_records is True:
        results1 = df1.loc[df1.query_strategy != "prior", columns].values
        results2 = df2.loc[df2.query_strategy != "prior", columns].values
        assert numpy.array_equal(results1, results2), "queried records not the same in results.sql"
    if test_metadata is False and test_prior_records is False and test_queried_records is False:
        raise "You probably wanted to test at least some aspects of the SQL file."
