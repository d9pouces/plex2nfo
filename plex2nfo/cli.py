import argparse

from plex2nfo.updater import PlexServerUpdater


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("plex_url", type=str, help="URL of your Plex media server.")
    parser.add_argument("plex_token", type=str, help="Value of the Plex token.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Do not write any .NFO or image file.",
    )
    parser.add_argument(
        "--verbose",
        "-V",
        action="store_true",
        default=False,
        help="Show all written files.",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        default=False,
        help="Disable the progress bar.",
    )
    parser.add_argument(
        "--overwrite-picture",
        "-W",
        action="store_true",
        default=False,
        help="Overwrite existing pictures in directories.",
    )
    parser.add_argument(
        "-s",
        "--section",
        action="append",
        default=[],
        help="Name of a section to update.",
    )
    parser.add_argument(
        "-v",
        "--volume",
        action="append",
        default=[],
        help="Useful when using docker: map a local folder to a Plex one. "
        "Syntax: --volume /path/to/local/folder:/path/to/plex/folder",
    )
    args = parser.parse_args(args=argv)
    plex_url = args.plex_url
    plex_token = args.plex_token
    dry_run = args.dry_run
    volumes = args.volume
    sections = args.section
    verbose = args.verbose
    quiet = args.quiet
    PlexServerUpdater(
        plex_url,
        plex_token,
        volumes,
        dry_run=dry_run,
        verbose=verbose,
        quiet=quiet,
        overwrite_picture=args.overwrite_picture,
    ).update_sections(sections=sections)
