import click


name = "new"


@click.command(help="Use a new extractor", name=f"ext:{name}")
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.pass_obj
def new_extractor_cmd(obj, force):
    if not force:
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.extractor.model = name
    obj.extractor.params = {}
    obj.provided.extractor = True

