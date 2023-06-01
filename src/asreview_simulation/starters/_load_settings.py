import json
import click


@click.command("load-settings", help="Load settings")
@click.argument("settings_file", type=click.File("rt"))
@click.pass_obj
def load_settings(obj, settings_file):
    assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    assert obj.provided.querier is False, "Attempted reassignment of querier"

    click.echo(f"Loading configuration from file '{settings_file.name}'...")
    with open(settings_file.name) as fid:
        settings = json.load(fid)

    if "balancer" in settings.keys():
        try:
            obj.balancer.model = settings["balancer"]["model"]
            obj.balancer.params = settings["balancer"]["params"]
            obj.provided.balancer = True
        except KeyError as e:
            print(
                "Expected balancer settings to include both a model and its parameterization."
            )
            raise e

    if "classifier" in settings.keys():
        try:
            obj.classifier.model = settings["classifier"]["model"]
            obj.classifier.params = settings["classifier"]["params"]
            obj.provided.classifier = True
        except KeyError as e:
            print(
                "Expected classifier settings to include both a model and its parameterization."
            )
            raise e

    if "extractor" in settings.keys():
        try:
            obj.extractor.model = settings["extractor"]["model"]
            obj.extractor.params = settings["extractor"]["params"]
            obj.provided.extractor = True
        except KeyError as e:
            print(
                "Expected extractor settings to include both a model and its parameterization."
            )
            raise e

    if "querier" in settings.keys():
        try:
            obj.querier.model = settings["querier"]["model"]
            obj.querier.params = settings["querier"]["params"]
            obj.provided.querier = True
        except KeyError as e:
            print(
                "Expected querier settings to include both a model and its parameterization."
            )
            raise e
