import json
import click
from asreview_simulation._private.lib.one_model_config import OneModelConfig


def assign_balancer(settings):
    if "bal" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["bal"]["abbr"], params=settings["bal"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("balancer")
            raise e


def assign_classifier(settings):
    if "cls" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["cls"]["abbr"], params=settings["cls"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("classifier")
            raise e


def assign_extractor(settings):
    if "fex" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["fex"]["abbr"], params=settings["fex"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("extractor")
            raise e


def assign_querier(settings):
    if "qry" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["qry"]["abbr"], params=settings["qry"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("querier")
            raise e


def assign_sampler(settings):
    if "sam" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["sam"]["abbr"], params=settings["sam"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("sampler")
            raise e


def assign_stopping(settings):
    if "stp" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["stp"]["abbr"], params=settings["stp"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("stopping")
            raise e


def print_keyerror_msg(model_type):
    print(f"Expected {model_type} settings to include a model abbreviation and the corresponding parameterization.")


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
    def assert_keys_are_valid():
        for key in settings.keys():
            assert key in [
                "bal",
                "cls",
                "fex",
                "qry",
                "sam",
                "stp",
            ], f"Unexpected key '{key}' found in model settings from '{settings_file.name}'."

    def assert_none_provided():
        assert obj.provided.bal is False, "Attempted reassignment of balancer model configuration"
        assert obj.provided.cls is False, "Attempted reassignment of classifier model configuration"
        assert obj.provided.fex is False, "Attempted reassignment of extractor model configuration"
        assert obj.provided.qry is False, "Attempted reassignment of querier model configuration"
        assert obj.provided.sam is False, "Attempted reassignment of sampler model configuration"
        assert obj.provided.stp is False, "Attempted reassignment of stopping model configuration"

    assert_none_provided()
    click.echo(f"Loading configuration from file '{settings_file.name}'...")
    with open(settings_file.name) as fid:
        settings = json.load(fid)
    assert_keys_are_valid()

    obj.models.bal, obj.provided.bal = assign_balancer(settings)
    obj.models.cls, obj.provided.cls = assign_classifier(settings)
    obj.models.fex, obj.provided.fex = assign_extractor(settings)
    obj.models.qry, obj.provided.qry = assign_querier(settings)
    obj.models.sam, obj.provided.sam = assign_sampler(settings)
    obj.models.stp, obj.provided.stp = assign_stopping(settings)
