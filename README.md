Plex2NFO
========

Given a Plex **movie** library, this tool will generate NFO files for each movie in the library.
The NFO files are compatible with Kodi and Jellyfin and can be used to import the movie library into Kodi or Jellyfin.

I assume that the library is already scanned into Plex, that the metadata is already downloaded and that each movie is in a separate folder.
Please see the [Plex documentation](https://support.plex.tv/articles/naming-and-organizing-your-movie-media-files/), especially the section "Movies in Their Own Folders" for more information.

Existing pictures are not overwritten, but NFO files are always overwritten.

installation
------------

```bash
pip install plex2nfo

```

Usage
-----

```bash
plex2nfo http://localhost:32400/ <plex-token> --section <Section> [--dry-run] --volume /local/volume/Movies:/data/Movies
```

The `--volume` argument is required when the Plex server is running in a Docker container and the NFO files should be written to the host system.
The path `/local/volume/Movies` should be replaced with the path to the movie library on the host system.
The path `/data/Movies` should be replaced with the path to the movie library in the Docker container.

Only Movies are supported, not TV shows.
