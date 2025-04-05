"""Run the main script."""

from plex2nfo import cli


def run(name: str, argv=None):
    if name == "__main__":
        cli.main(argv=argv)


run(__name__)
