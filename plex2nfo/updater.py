import logging
import os
import pathlib
from datetime import UTC
from xml.etree import ElementTree as ETr

import requests
import tqdm
from plexapi.base import Playable
from plexapi.exceptions import NotFound, Unauthorized
from plexapi.media import Image
from plexapi.server import PlexServer
from plexapi.video import Episode, Movie
from requests import RequestException
from systemlogger import getLogger

logger = getLogger(name="plex2nfo", extra_tags={"application_fqdn": "system"})


class PlexServerUpdater(PlexServer):
    def __init__(
        self,
        plex_url: str,
        plex_token: str,
        volumes: list[str],
        dry_run: bool = False,
        verbose: bool = False,
        quiet: bool = False,
        overwrite_picture: bool = False,
    ):
        """Initialize the PlexServerUpdater."""
        self.initialized = False
        try:
            super().__init__(plex_url, plex_token)
        except Unauthorized:
            self.show_msg("Invalid credential", level=logging.ERROR)
            return
        except RequestException:
            self.show_msg(f"Unable to connect to {plex_url}", level=logging.ERROR)
            return
        self.initialized = True
        self.volume_mapping: list[tuple[str, str]] = []
        for volume in volumes:
            local_path, plex_path = volume.split(":")
            local_path = str(pathlib.Path(local_path).resolve())
            plex_path = str(pathlib.Path(plex_path).resolve())
            self.volume_mapping.append((local_path, plex_path))
        self.volume_mapping.sort(key=lambda x: len(x[1]), reverse=True)
        self.dry_run = dry_run
        self.verbose = verbose
        self.quiet = quiet
        self.overwrite_picture = overwrite_picture

    def update_sections(self, sections: list[str] = None):
        """Update the required sections of the Plex server."""
        if not self.initialized:
            self.show_msg("Not connected to the Plex server", level=logging.ERROR)
            return
        if not sections:
            sections = [section.title for section in self.library.sections()]
        for section_name in sections:
            self.update_section(section_name)

    def update_section(self, section_name):
        try:
            section = self.library.section(section_name)
        except NotFound:
            self.show_msg(f"Section {section_name} not found", level=logging.ERROR)
            return
        self.show_msg(f"Updating section {section_name}")
        for item in tqdm.tqdm(section.all(), disable=self.verbose or self.quiet):
            self.update_item(item)

    def show_msg(self, msg, level=logging.INFO):
        if self.verbose:
            print(msg)
        else:
            logger.log(level, msg)

    def update_item(self, playable: Playable):
        if isinstance(playable, Movie):
            self.update_movie(playable)
        else:
            raise NotImplementedError("Subclasses must implement this method")

    def update_movie(self, movie: Movie):
        """Create a NFO file content from a movie."""
        # display tags that are not taken into account
        root = ETr.Element("movie")
        x_actors = ETr.SubElement(root, "actors")
        for country in movie.countries:
            ETr.SubElement(root, "country").text = country.tag
        if movie.addedAt:
            ETr.SubElement(root, "dateadded").text = movie.addedAt.astimezone(
                tz=UTC
            ).strftime("%Y-%m-%d %H:%M:%S")
        if movie.lastViewedAt:
            ETr.SubElement(root, "lastplayed").text = movie.lastViewedAt.astimezone(
                tz=UTC
            ).strftime("%Y-%m-%d %H:%M:%S")
        if movie.originalTitle:
            ETr.SubElement(root, "originalTitle").text = movie.originalTitle
        if movie.viewCount:
            ETr.SubElement(root, "playcount").text = str(movie.viewCount)
        if movie.viewCount or movie.lastViewedAt:
            ETr.SubElement(root, "watched").text = "true"
        if movie.summary:
            ETr.SubElement(root, "plot").text = movie.summary
        if movie.originallyAvailableAt:
            ETr.SubElement(root, "releasedate").text = (
                movie.originallyAvailableAt.strftime("%Y-%m-%d")
            )
            ETr.SubElement(root, "premiereda").text = (
                movie.originallyAvailableAt.strftime("%Y-%m-%d")
            )
        if movie.duration:
            ETr.SubElement(root, "runtime").text = str(movie.duration // 60_000)
        if movie.titleSort:
            ETr.SubElement(root, "sorttitle").text = movie.titleSort
        if movie.studio:
            ETr.SubElement(root, "studio").text = movie.studio
        if movie.tagline:
            ETr.SubElement(root, "tagline").text = movie.tagline
        ETr.SubElement(root, "title").text = movie.title
        for guid in movie.guids:
            id_type, sep, id_value = guid.id.partition("://")
            id_element = ETr.SubElement(root, "uniqueid", type=id_type)
            id_element.text = id_value
            if isinstance(movie, Movie) and id_type == "imdb":
                ETr.SubElement(root, "id").text = id_value
            if isinstance(movie, Episode) and id_type == "imdb":
                ETr.SubElement(root, "id").text = id_value
            if id_type == "imdb":
                id_element.set("default", "true")
                ETr.SubElement(root, "imdbid").text = id_value
            elif id_type == "tmdb":
                ETr.SubElement(root, "tmdbid").text = id_value
            elif id_type == "tvdb":
                ETr.SubElement(root, "tvdbid").text = id_value
            elif id_type == "mbid":
                ETr.SubElement(root, "idmbid").text = id_value
        if movie.year:
            ETr.SubElement(root, "year").text = str(movie.year)
        if movie.contentRating:
            cr = (
                movie.contentRating.replace("fr/", "FR-")
                .replace("-Unrated", "-U")
                .replace("-TP", "-Tous publics")
            )
            ETr.SubElement(root, "mpaa").text = cr
        x_ratings = ETr.SubElement(root, "ratings")
        for rating in movie.ratings:
            if rating.type != "audience":
                continue
            rate_site, __, __ = rating.image.partition("://")
            x_rating = ETr.SubElement(x_ratings, "rating", name=rate_site, max="10")
            if rate_site == "imdb":
                x_rating.set("default", "true")
            ETr.SubElement(x_rating, "value").text = f"{rating.value:6f}"
        for writer in movie.writers:
            ETr.SubElement(root, "writer").text = writer.tag
        for director in movie.directors:
            ETr.SubElement(root, "director").text = director.tag
        for genre in movie.genres:
            ETr.SubElement(root, "genre").text = genre.tag
        for order, role in enumerate(movie.roles):
            x_actor = ETr.SubElement(x_actors, "actor")
            ETr.SubElement(x_actor, "name").text = role.tag
            ETr.SubElement(x_actor, "role").text = role.role
            ETr.SubElement(x_actor, "order").text = str(order)
        for collection in movie.collections:
            x_collection = ETr.SubElement(root, "set")
            ETr.SubElement(x_collection, "name").text = collection.tag
        movie_directories = {
            pathlib.Path(part.file).parent
            for media in movie.media
            for part in media.parts
        }
        for image in movie.images:
            if image.type == "coverPoster":
                for movie_directory in movie_directories:
                    self.download_image(image, movie_directory, "poster")
            elif image.type == "background":
                for movie_directory in movie_directories:
                    self.download_image(image, movie_directory, "backdrop")
        ETr.indent(root, level=0)
        content = ETr.tostring(root, encoding="unicode", method="xml")
        for movie_directory in movie_directories:
            full_path = movie_directory / "movie.nfo"
            local_path = self.map_plex_path_to_local(full_path)
            try:
                if not self.dry_run and not os.path.exists(local_path):
                    with open(local_path, "w") as fd:
                        fd.write(content)
                    r = "OK"
                elif os.path.exists(local_path):
                    r = "SKIPPED"
                else:
                    r = "DRY RUN"
                level = logging.INFO
            except Exception as e:
                r = f"FAILED ({e})"
                level = logging.ERROR
            self.show_msg(f"{local_path}: {r}", level=level)

    def download_image(
        self,
        image: Image,
        movie_directory: pathlib.Path,
        basename: str,
    ):
        full_path = movie_directory / f"{basename}.jpeg"
        local_path = self.map_plex_path_to_local(full_path)
        complete_url = self.url(image.url)
        headers = self._headers()
        r = requests.get(url=complete_url, headers=headers, stream=True)
        if r.status_code != 200:
            r = f"FAILED (HTTP code {r.status_code})"
            level = logging.ERROR
        else:
            content_type = r.headers.get("content-type", "")
            basetype, sep, ext = content_type.partition(";")[0].rpartition("/")
            if not ext:
                ext = "jpg"
            full_path = movie_directory / f"{basename}.{ext}"
            local_path = self.map_plex_path_to_local(full_path)
            try:
                if not self.dry_run:
                    os.makedirs(
                        self.map_plex_path_to_local(movie_directory), exist_ok=True
                    )
                if not self.dry_run and (
                    self.overwrite_picture or not os.path.exists(local_path)
                ):
                    with open(local_path, "wb") as fd:
                        for chunk in r.iter_content(1024):
                            fd.write(chunk)

                elif os.path.exists(local_path):
                    r = "SKIPPED"
                else:
                    r = "DRY RUN"
                level = logging.INFO
            except Exception as e:
                r = f"FAILED ({e})"
                level = logging.ERROR
        self.show_msg(f"{local_path}: {r}", level=level)

    def map_plex_path_to_local(self, path: pathlib.Path) -> str:
        """Map a Plex path to a local path using the volume mapping."""
        src_path = str(path)
        for (
            local_path,
            plex_path,
        ) in self.volume_mapping:
            if src_path.startswith(plex_path):
                return src_path.replace(plex_path, local_path, 1)
        return src_path
