from dataclasses import dataclass
import hyperopt
import matplotlib.pyplot as plt
import numpy
from asreview_simulation.api import get_pyll


@dataclass
class Dim:
    lo: int | float
    up: int | float
    name: str


fig, ((ax00, ax01), (ax10, ax11)) = plt.subplots(2, 2)


def generate_samples(pyll, n=100):
    return [hyperopt.pyll.stochastic.sample(pyll) for _ in range(n)]


def run_hyperopt_1d_uniform():
    dim = Dim(lo=-10, up=10, name="x")
    pyll = [
        hyperopt.hp.uniform(dim.name, dim.lo, dim.up),
    ]
    nsamples = 100
    samples = generate_samples(pyll, nsamples)
    nbins = 21
    bin_edges = numpy.linspace(dim.lo, dim.up, nbins)
    counts, bins = numpy.histogram([s[0] for s in samples], bin_edges)
    ax00.stairs(counts, bins)
    ax00.set_xlabel(dim.name)
    ax00.set_ylabel("count")
    ax00.set_title(f"1-D uniform random sampling N={nsamples}")
    plt.draw()


def run_hyperopt_2d_uniform():
    dim0 = Dim(lo=-10, up=10, name="x")
    dim1 = Dim(lo=10, up=30, name="y")
    pyll = [
        hyperopt.hp.uniform(dim0.name, dim0.lo, dim0.up),
        hyperopt.hp.uniform(dim1.name, dim1.lo, dim1.up),
    ]
    nsamples = 100
    samples = generate_samples(pyll, nsamples)
    ax01.scatter([s[0] for s in samples], [s[1] for s in samples])
    ax01.set_xlabel(dim0.name)
    ax01.set_ylabel(dim1.name)
    ax01.set_title(f"1-D uniform random sampling N={nsamples}")
    plt.draw()


def run_hyperopt_1d_uniformint_like_fex_tfidf():
    # note the range on uniformint sampling is unexpected:
    dim = Dim(lo=0.5, up=3.5, name="fex/tfidf/ngram_max")
    pyll = [
        hyperopt.hp.uniformint(dim.name, dim.lo, dim.up),
    ]
    nsamples = 1000
    samples = generate_samples(pyll, nsamples)
    bin_edges = numpy.linspace(dim.lo, dim.up, round(dim.up - dim.lo) + 1)
    counts, bins = numpy.histogram([s[0] for s in samples], bin_edges)
    ax10.stairs(counts, bins)
    ax10.set_xlabel(dim.name)
    ax10.set_ylabel("count")
    ax10.set_title(f"1-D uniformint random sampling N={nsamples}")
    plt.draw()


def run_hyperopt_1d_randint_like_fex_doc2vec_dm():
    dim = Dim(lo=0, up=3, name="fex/doc2vec/dm")
    pyll = [
        hyperopt.hp.randint(dim.name, dim.lo, dim.up),  # draws integers [0, 3)
    ]
    nsamples = 1000
    samples = generate_samples(pyll, nsamples)
    bin_edges = numpy.linspace(dim.lo - 0.5, dim.up - 0.5, dim.up - dim.lo + 1)
    counts, bins = numpy.histogram([s[0] for s in samples], bin_edges)
    ax11.stairs(counts, bins)
    ax11.set_xlabel(dim.name)
    ax11.set_ylabel("count")
    ax11.set_title(f"1-D randint random sampling N={nsamples}")
    plt.draw()


def run_hyperopt_choice_bal_cls():
    pyll = {
        "bal": hyperopt.hp.choice(
            "bal",
            [
                get_pyll("bal-double"),
                get_pyll("bal-simple"),
                get_pyll("bal-undersample"),
            ],
        ),
        "cls": hyperopt.hp.choice(
            "cls",
            [
                get_pyll("cls-logistic"),
                get_pyll("cls-nb"),
                get_pyll("cls-nn-2-layer"),
                get_pyll("cls-rf"),
                get_pyll("cls-svm"),
            ],
        ),
        "fex": hyperopt.hp.choice(
            "fex",
            [
                get_pyll("fex-doc2vec"),
                get_pyll("fex-sbert"),
                get_pyll("fex-tfidf"),
            ],
        ),
        "qry": hyperopt.hp.choice(
            "qry",
            [
                get_pyll("qry-cluster"),
                get_pyll("qry-max"),
                get_pyll("qry-max-random"),
                get_pyll("qry-max-uncertainty"),
                get_pyll("qry-random"),
                get_pyll("qry-uncertainty"),
            ],
        ),
        "sam": hyperopt.hp.choice(
            "sam",
            [
                get_pyll("sam-handpicked"),
                get_pyll("sam-random"),
            ],
        ),
        "stp": hyperopt.hp.choice(
            "stp",
            [
                get_pyll("stp-min"),
                get_pyll("stp-none"),
                get_pyll("stp-nq"),
            ],
        ),
    }
    nsamples = 100
    _ = generate_samples(pyll, nsamples)
    assert False, "needs assertions"


if __name__ == "__main__":
    run_hyperopt_1d_uniform()
    run_hyperopt_2d_uniform()
    run_hyperopt_1d_uniformint_like_fex_tfidf()
    run_hyperopt_1d_randint_like_fex_doc2vec_dm()
    run_hyperopt_choice_bal_cls()
    plt.show()
