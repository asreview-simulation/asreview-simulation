import sys
if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points


def get_quads():
    group = "asreview_simulationcontrib.quads"
    try:
        quads = [(e.name, e.load()) for e in entry_points(group=group)]
    except Exception as e:
        print(
            f"Something went wrong loading a module from entrypoint group '{group}'. Th"
            + f"e error message was: {e}\nContinuing..."
        )
        quads = []

    return quads
