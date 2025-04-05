import pathlib
import tempfile

import requests
from plexapi.server import PlexServer

from plex2nfo.cli import main
from test_plex2nfo.test_updater import http_query, request_get


def test_cli(monkeypatch):
    """Test the updater module."""
    monkeypatch.setattr(PlexServer, "query", http_query)
    monkeypatch.setattr(requests, "get", request_get)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = pathlib.Path(tmpdir).resolve()
        movie_name = "The King's Man - Première Mission (2021)"

        main(
            [
                "http://localhost:32400/",
                "aaaabbbbcccdddddeeee",
                "-v",
                f"{tmpdir}:/data/Films-Test",
            ]
        )
        assert (tmpdir / movie_name).exists()
