import json
import click


@click.command(
    "load-settings",
    help="Load settings",
    short_help="Load settings",
)
@click.option(
    "--from",
    "settings_file",
    help="The file holding the settings",
    default=None,
    required=True,
    type=click.File("rt"),
)
@click.pass_obj
def load_settings_subcommand(obj, settings_file):
    assert obj.provided.balancer is False, "Attempted reassignment of balancer model configuration"
    assert obj.provided.classifier is False, "Attempted reassignment of classifier model configuration"
    assert obj.provided.extractor is False, "Attempted reassignment of extractor model configuration"
    assert obj.provided.querier is False, "Attempted reassignment of querier model configuration"
    assert obj.provided.sampler is False, "Attempted reassignment of sampler model configuration"
    assert obj.provided.stopping is False, "Attempted reassignment of stopping model configuration"

    click.echo(f"Loading configuration from file '{settings_file.name}'...")
    with open(settings_file.name) as fid:
        settings = json.load(fid)

    for key in settings.keys():
        assert key in [
            "balancer",
            "classifier",
            "extractor",
            "querier",
            "sampler",
            "stopping",
        ], f"Unexpected key '{key}' found in model settings from '{settings_file.name}'."

    if "balancer" in settings.keys():
        try:
            obj.models.balancer.abbr = settings["balancer"]["abbr"]
            obj.models.balancer.params = settings["balancer"]["params"]
            obj.provided.balancer = True
        except KeyError as e:
            print("Expected balancer settings to include a model abbreviation and the corresponding parameterization.")
            raise e

    if "classifier" in settings.keys():
        try:
            obj.models.classifier.abbr = settings["classifier"]["abbr"]
            obj.models.classifier.params = settings["classifier"]["params"]
            obj.provided.classifier = True
        except KeyError as e:
            print(
                "Expected classifier settings to include a model abbreviation and the corresponding parameterization."
            )
            raise e

    if "extractor" in settings.keys():
        try:
            obj.models.extractor.abbr = settings["extractor"]["abbr"]
            obj.models.extractor.params = settings["extractor"]["params"]
            obj.provided.extractor = True
        except KeyError as e:
            print("Expected extractor settings to include a model abbreviation and the corresponding parameterization.")
            raise e

    if "querier" in settings.keys():
        try:
            obj.models.querier.abbr = settings["querier"]["abbr"]
            obj.models.querier.params = settings["querier"]["params"]
            obj.provided.querier = True
        except KeyError as e:
            print("Expected querier settings to include a model abbreviation and the corresponding parameterization.")
            raise e

    if "sampler" in settings.keys():
        try:
            obj.models.sampler.abbr = settings["sampler"]["abbr"]
            obj.models.sampler.params = settings["sampler"]["params"]
            obj.provided.sampler = True
        except KeyError as e:
            print("Expected sampler settings to include a model abbreviation and the corresponding parameterization.")
            raise e

    if "stopping" in settings.keys():
        try:
            obj.models.stopping.abbr = settings["stopping"]["abbr"]
            obj.models.stopping.params = settings["stopping"]["params"]
            obj.provided.stopping = True
        except KeyError as e:
            print("Expected stopping settings to include a model abbreviation and the corresponding parameterization.")
            raise e
