from importlib.metadata import entry_points as list_entry_points
import argparse
import sys


def _print_asreview_help(subcommands):

    parser = argparse.ArgumentParser(
        prog="asreview",
        formatter_class=argparse.RawTextHelpFormatter,
        description="asreview description",
    )
    subparsers = parser.add_subparsers()
    for subcommand in subcommands.keys():
        subparsers.add_parser(subcommand)
    parser.print_help()


def cli():

    group_name = "asreview.subcommands"
    try:
        entry_points = {e.name: e.load() for e in list_entry_points(group=group_name)}
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'{group_name}'. The error message was: {e}\nContinuing...")
        entry_points = {}

    has_args = len(sys.argv) > 1
    if not has_args:
        _print_asreview_help(entry_points)
        return

    first_arg_is_subcommand = not sys.argv[1].startswith("-")
    if not first_arg_is_subcommand:
        print("arg not a subcommand")
        return

    subcommand_name = sys.argv[1]
    is_valid_name = subcommand_name in entry_points.keys()
    if not is_valid_name:
        raise ValueError(f"'{subcommand_name}' is not a valid subcommand.")
    subcommand = entry_points[subcommand_name]()
    subcommand(sys.argv[2:])

