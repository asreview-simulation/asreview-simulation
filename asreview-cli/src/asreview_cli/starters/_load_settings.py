import click


@click.command("load-settings",
               help="Load settings")
@click.argument("settings_file")
@click.pass_obj
def load_settings(obj, settings_file):
    assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    assert obj.provided.querier is False, "Attempted reassignment of querier"

    # TODO load config, assign state
    click.echo(f"Would load configuration from file {settings_file}")

    obj.provided.balancer = True
    obj.provided.classifier = True
    obj.provided.extractor = True
    obj.provided.querier = True
