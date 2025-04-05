import io
import mimetypes
import pathlib
import tempfile
from importlib.resources import files
from urllib.parse import urlparse
from xml.etree import ElementTree as ETr

import requests
from plexapi.server import PlexServer

from plex2nfo.updater import PlexServerUpdater
from test_plex2nfo.data import EXPECTED_NFO, FILES_MATCHES, HTTP_DATA

mimetypes.init()


def http_query(server, path, **kwargs):
    """Mock the HTTP query to the Plex server."""
    path, sep, query = path.partition("?")
    data = HTTP_DATA[path]
    movie_data = ETr.fromstring(data)
    return movie_data


def request_get(url, **kwargs):
    """Mock the requests.get method."""
    parsed_url = urlparse(url)
    path = FILES_MATCHES[parsed_url.path]
    rel_path = files("test_plex2nfo") / path
    with rel_path.open("rb") as f:
        content = f.read()
    r = requests.Response()
    r.status_code = 200
    r.headers["Content-Type"] = mimetypes.guess_type(rel_path)[0]
    r.raw = io.BytesIO(content)
    return r


#    print("HTTP query:", path, kwargs)


def test_update_library(monkeypatch):
    """Test the updater module."""
    monkeypatch.setattr(PlexServer, "query", http_query)
    monkeypatch.setattr(requests, "get", request_get)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = pathlib.Path(tmpdir).resolve()
        movie_name = "The King's Man - Première Mission (2021)"

        updater = PlexServerUpdater(
            "http://localhost:32400/",
            "aaaabbbbcccdddddeeee",
            [f"{tmpdir}:/data/Films-Test"],
            dry_run=True,
            quiet=True,
            verbose=True,
        )
        updater.update_sections()
        assert not (tmpdir / movie_name).exists()

        updater = PlexServerUpdater(
            "http://localhost:32400/",
            "aaaabbbbcccdddddeeee",
            [f"{tmpdir}:/data/Films-Test"],
            dry_run=False,
            quiet=True,
            verbose=False,
        )
        arg = pathlib.Path(f"/data/Films-Test/{movie_name}/poster.jpeg")
        actual = updater.map_plex_path_to_local(arg)
        expected = f"{tmpdir}/{movie_name}/poster.jpeg"
        assert actual == expected
        updater.update_sections()
        assert (tmpdir / movie_name).exists()
        assert (tmpdir / movie_name / "poster.jpeg").exists()
        assert (tmpdir / movie_name / "backdrop.jpeg").exists()
        assert (tmpdir / movie_name / "movie.nfo").exists()
        actual_nfo = (tmpdir / movie_name / "movie.nfo").read_text()
        assert actual_nfo == EXPECTED_NFO
