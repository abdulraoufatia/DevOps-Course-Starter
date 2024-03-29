FROM python:3.10 as base

WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin" 

RUN apt-get update \
    && apt-get -y install curl \
    && curl -sSL https://install.python-poetry.org | python -

COPY . /app/

RUN poetry config virtualenvs.create false --local && poetry install

FROM base as development

CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]

FROM base as test

ENV PATH="${PATH}:/root/todo_app/tests"

CMD ["poetry", "run", "pytest"]

FROM base as production

ENV PORT=5000

CMD poetry run gunicorn -b 0.0.0.0:$PORT "todo_app.app:create_app()"