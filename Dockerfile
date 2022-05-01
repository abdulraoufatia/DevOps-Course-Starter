FROM python:3.7.13-slim-buster as base

WORKDIR /app

ENV PATH="${PATH}:/root/.poetry/bin" 

RUN apt-get update \
    && apt-get -y install curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - 

EXPOSE 4000

COPY . /app/

RUN poetry config virtualenvs.create false --local && poetry install

FROM base as development

CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]

FROM base as production

CMD poetry run gunicorn -b 0.0.0.0:4000 "todo_app.app:create_app()"