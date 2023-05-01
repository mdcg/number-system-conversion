from python:3.9.16-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.13

RUN mkdir /app
WORKDIR /app
COPY ./api/ /app/

RUN apt-get update
RUN apt-get install make

RUN make poetry/setup
RUN poetry config virtualenvs.create false
RUN make poetry/install-dependencies

CMD python -m sanic core:app --host=0.0.0.0 --port=1337 --workers=4
EXPOSE 1337
