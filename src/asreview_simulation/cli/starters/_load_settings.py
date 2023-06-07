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
            obj.balancer.abbr = settings["balancer"]["abbr"]
            obj.balancer.params = settings["balancer"]["params"]
            obj.provided.balancer = True
        except KeyError as e:
            print(
                "Expected balancer settings to include a model abbreviation and the corresponding parameterization."
            )
            raise e

    if "classifier" in settings.keys():
        try:
            obj.classifier.abbr = settings["classifier"]["abbr"]
            obj.classifier.params = settings["classifier"]["params"]
            obj.provided.classifier = True
        except KeyError as e:
            print(
                "Expected classifier settings to include a model abbreviation and the corresponding parameterization."
            )
            raise e

    if "extractor" in settings.keys():
        try:
            obj.extractor.abbr = settings["extractor"]["abbr"]
            obj.extractor.params = settings["extractor"]["params"]
            obj.provided.extractor = True
        except KeyError as e:
            print(
                "Expected extractor settings to include a model abbreviation and the corresponding parameterization."
            )
            raise e

    if "querier" in settings.keys():
        try:
            obj.querier.abbr = settings["querier"]["abbr"]
            obj.querier.params = settings["querier"]["params"]
            obj.provided.querier = True
        except KeyError as e:
            print(
                "Expected querier settings to include a model abbreviation and the corresponding parameterization."
            )
            raise e

    if "sampler" in settings.keys():
        try:
            obj.sampler.abbr = settings["sampler"]["abbr"]
            obj.sampler.params = settings["sampler"]["params"]
            obj.provided.sampler = True
        except KeyError as e:
            print(
                "Expected sampler settings to include a model abbreviation and the corresponding parameterization."
            )
            raise e

    if "stopping" in settings.keys():
        try:
            obj.stopping.abbr = settings["stopping"]["abbr"]
            obj.stopping.params = settings["stopping"]["params"]
            obj.provided.stopping = True
        except KeyError as e:
            print(
                "Expected stopping settings to include a model abbreviation and the corresponding parameterization."
            )
            raise e
