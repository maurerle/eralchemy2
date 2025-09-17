import argparse
from importlib.metadata import PackageNotFoundError, version

from eralchemy import render_er

from .helpers import check_args

try:
    __version__ = version(__package__)
except PackageNotFoundError:
    __version__ = "na"


def cli() -> None:
    """Entry point for the application script"""
    parser = get_argparser()

    args = parser.parse_args()
    check_args(args)
    if args.v:
        print(f"eralchemy2 version {__version__}.")
        exit(0)
    render_er(
        args.i,
        args.o,
        args.m or "auto",
        title=args.title,
        include_tables=args.include_tables,
        include_columns=args.include_columns,
        exclude_tables=args.exclude_tables,
        exclude_columns=args.exclude_columns,
        schema=args.s,
    )


def get_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="eralchemy2")
    parser.add_argument("-i", nargs="?", help="Database URI to process.")
    parser.add_argument("-o", nargs="?", help="Name of the file to write.")
    parser.add_argument("-s", nargs="?", help="Name of the schema.")
    parser.add_argument("--title", nargs="?", help="Add a title to the output graph")
    parser.add_argument(
        "-m",
        nargs="?",
        help="Output mode to write format, default: auto",
    )
    parser.add_argument(
        "--exclude-tables",
        "-x",
        nargs="+",
        help="Name of tables not to be displayed.",
    )
    parser.add_argument(
        "--exclude-columns",
        nargs="+",
        help="Name of columns not to be displayed (for all tables).",
    )
    parser.add_argument(
        "--include-tables",
        nargs="+",
        help="Name of tables to be displayed alone.",
    )
    parser.add_argument(
        "--include-columns",
        nargs="+",
        help="Name of columns to be displayed alone (for all tables).",
    )
    parser.add_argument("-v", help="Prints version number.", action="store_true")
    return parser


if __name__ == "__main__":
    cli()
