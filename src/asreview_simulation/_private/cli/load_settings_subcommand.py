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

    def assign_balancer():
        if "bal" in settings.keys():
            try:
                obj.models.bal.abbr = settings["bal"]["abbr"]
                obj.models.bal.params = settings["bal"]["params"]
                obj.provided.bal = True
            except KeyError as e:
                print_keyerror_msg("balancer")
                raise e

    def assign_classifier():
        if "classifier" in settings.keys():
            try:
                obj.models.cls.abbr = settings["cls"]["abbr"]
                obj.models.cls.params = settings["cls"]["params"]
                obj.provided.cls = True
            except KeyError as e:
                print_keyerror_msg("classifier")
                raise e

    def assign_extractor():
        if "extractor" in settings.keys():
            try:
                obj.models.fex.abbr = settings["fex"]["abbr"]
                obj.models.fex.params = settings["fex"]["params"]
                obj.provided.fex = True
            except KeyError as e:
                print_keyerror_msg("extractor")
                raise e

    def assign_querier():
        if "querier" in settings.keys():
            try:
                obj.models.qry.abbr = settings["qry"]["abbr"]
                obj.models.qry.params = settings["qry"]["params"]
                obj.provided.qry = True
            except KeyError as e:
                print_keyerror_msg("querier")
                raise e

    def assign_sampler():
        if "sampler" in settings.keys():
            try:
                obj.models.sam.abbr = settings["sam"]["abbr"]
                obj.models.sam.params = settings["sam"]["params"]
                obj.provided.sam = True
            except KeyError as e:
                print_keyerror_msg("sampler")
                raise e

    def assign_stopping():
        if "stopping" in settings.keys():
            try:
                obj.models.stp.abbr = settings["stp"]["abbr"]
                obj.models.stp.params = settings["stp"]["params"]
                obj.provided.stp = True
            except KeyError as e:
                print_keyerror_msg("stopping")
                raise e

    def print_keyerror_msg(model_type):
        print(f"Expected {model_type} settings to include a model abbreviation and the corresponding parameterization.")

    assert_none_provided()
    click.echo(f"Loading configuration from file '{settings_file.name}'...")
    with open(settings_file.name) as fid:
        settings = json.load(fid)
    assert_keys_are_valid()
    assign_balancer()
    assign_classifier()
    assign_extractor()
    assign_querier()
    assign_sampler()
    assign_stopping()
