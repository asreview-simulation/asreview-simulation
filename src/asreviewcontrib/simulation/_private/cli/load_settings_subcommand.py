import json
import click
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_bal_msg
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_cls_msg
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_fex_msg
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_ofn_msg
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_qry_msg
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_sam_msg
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_stp_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig


def assign_bal(settings):
    if "bal" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["bal"]["abbr"], params=settings["bal"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("bal")
            raise e


def assign_cls(settings):
    if "cls" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["cls"]["abbr"], params=settings["cls"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("cls")
            raise e


def assign_fex(settings):
    if "fex" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["fex"]["abbr"], params=settings["fex"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("fex")
            raise e


def assign_ofn(settings):
    if "obj" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["obj"]["abbr"], params=settings["obj"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("obj")
            raise e


def assign_qry(settings):
    if "qry" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["qry"]["abbr"], params=settings["qry"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("qry")
            raise e


def assign_sam(settings):
    if "sam" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["sam"]["abbr"], params=settings["sam"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("sam")
            raise e


def assign_stp(settings):
    if "stp" in settings.keys():
        try:
            return OneModelConfig(abbr=settings["stp"]["abbr"], params=settings["stp"]["params"]), True
        except KeyError as e:
            print_keyerror_msg("stp")
            raise e


def print_keyerror_msg(model_type):
    print(f"Expected '{model_type}' model settings to include an abbreviation and the corresponding parameterization.")


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
                "ofn",
                "qry",
                "sam",
                "stp",
            ], f"Unexpected key '{key}' found in model settings from '{settings_file.name}'."

    def assert_none_provided():
        assert obj.provided.bal is False, dont_reassign_bal_msg
        assert obj.provided.cls is False, dont_reassign_cls_msg
        assert obj.provided.fex is False, dont_reassign_fex_msg
        assert obj.provided.ofn is False, dont_reassign_ofn_msg
        assert obj.provided.qry is False, dont_reassign_qry_msg
        assert obj.provided.sam is False, dont_reassign_sam_msg
        assert obj.provided.stp is False, dont_reassign_stp_msg

    assert_none_provided()
    click.echo(f"Loading configuration from file '{settings_file.name}'...")
    with open(settings_file.name) as fid:
        settings = json.load(fid)
    assert_keys_are_valid()

    obj.config.bal, obj.provided.bal = assign_bal(settings)
    obj.config.cls, obj.provided.cls = assign_cls(settings)
    obj.config.fex, obj.provided.fex = assign_fex(settings)
    obj.config.obj, obj.provided.obj = assign_ofn(settings)
    obj.config.qry, obj.provided.qry = assign_qry(settings)
    obj.config.sam, obj.provided.sam = assign_sam(settings)
    obj.config.stp, obj.provided.stp = assign_stp(settings)
