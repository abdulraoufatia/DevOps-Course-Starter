# 1 - Installing Python Image
FROM python:3.7.13-slim-buster as base

# 2 - Preliminary measures
WORKDIR /app
ENV PATH="${PATH}:/root/.poetry/bin" 

# 3 - Installing dependencies
RUN apt-get update \
    && apt-get -y install curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - 

# 4 - Copying across my application code
COPY . /app

FROM base as development
# 5 - Defining an entrypoint and default launch command
CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]
    
# 7 - Project Initalisation 
    # Installing dependencies 
RUN poetry config virtualenvs.create false --local && poetry install
    # Listening on specific port
EXPOSE 4000
FROM base as production
# 8 - Ensuring app runs with gunicorn
CMD poetry run gunicorn -b 0.0.0.0:$4000 "todo_app.app:create_app()"