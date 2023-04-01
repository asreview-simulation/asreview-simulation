import click


@click.command(name="c-nb", help="Use Naive Bayes classifier")
@click.option("-alpha", "alpha", default=3.822, type=float, help="hyperparameter 'alpha'.")
@click.pass_obj
def naive_bayes(obj, alpha):
    assert obj.provided.classifier is False, "Attempted reassignment of naive bayes classifier"
    obj.classifier.model = "nb"
    obj.classifier.params = {
        "alpha": alpha
    }
    obj.provided.classifier = True
