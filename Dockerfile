FROM python:3.13-alpine
LABEL org.opencontainers.image.authors="github@19pouces.net"
LABEL description="Docker image for plex2nfo"
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=on \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  POETRY_NO_INTERACTION=1
RUN adduser --disabled-password --gecos "plex2nfo" plex2nfo --home /plex2nfo \
    && python3 -m venv /venv \
    && chown -R plex2nfo:plex2nfo /venv
RUN /venv/bin/python3 -m pip install --no-cache-dir pip plex2nfo --upgrade
USER plex2nfo
ENTRYPOINT ["/venv/bin/python3", "-m", "plex2nfo"]
