# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Before Running the app

The set up of this to_do app has been designed for Trello. Set up the .env file and place the information accordingly to your Trello account:

```bash
SECRET_KEY=secret-key # leave this as it is

API_KEY = 'abc'
API_TOKEN = 'def'
BOARD = 'ghi'
NOTSTARTED_LIST = 'klm'
INPROGRESS_LIST = 'nop'
COMPLETED_LIST =  'qrs'
```

## Running the App

Once the all dependencies have been installed and relevant information has been inputted, start the Flask app in development mode within the poetry environment by running:

```bash
poetry run flask run
```

You should see output similar to the following:

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running tests with pytest

Being a DevOps engineer invokes many responabilities, one responsability of a DevOps Engineer is to be involved in identifying required qualities and estimate their impact on the development process. This is done through the practice of testing.

In the world of software engineering, testing is an impertive practice constituting the security of your code.

Through out this project, testing our software was achieved through the pytest framework.

### Getting started - Installing pytest

### Run the following command in your command line

```bash
pip install pytest
```

### Check that you installed the correct version

### Executing the test

1. Creating a simple test

```bash
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```

Testing the function

```bash

$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-6.x.y, py-1.x.y, pluggy-1.x.y
cachedir: $PYTHON_PREFIX/.pytest_cache
rootdir: $REGENDOC_TMPDIR
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================


```

To read more about pytest, please visit pytest offical website here : [pytest documentation] (<https://docs.pytest.org/en/6.2.x/contents.html>)

## DevOps Applications - Containerisation

This application utilises containerisation concept. Containerisation entails placing a software component and its environement, dependencies, and configuration, into an insolated unit called a container. This makes it poosible to deploy an application consistently on any computing envoronment, wether on-premises or cloud-based.

### Getting Started with Docker

To get started with Docker you would need to install a containerisation tool. A containerisation tool used for this project was Docker. However, you may find alternatives depending on your Operating System.

### Build and run the Docker Image

This project is buit using mutlti-stage builds. Mutil-stage builds are useful to optimise Dockerfiles while keeping them easy to read and maintain.  

To build the development enviornment, run the following command:

```bash
docker build --target development --tag todo_app:development .
```

To build the production environment, run the following command:

```bash
docker build --target production --tag todo_app:production .
```

I have built the development, you should see something similar to this:

```bash

(.venv) [Module_5 x] {} DevOps-Course-Starter docker build --target development --tag todo_app .
[+] Building 47.5s (10/10) FINISHED                                                                                                                                                
 => [internal] load build definition from Dockerfile                                                                                                                          0.1s
 => => transferring dockerfile: 567B                                                                                                                                          0.0s
 => [internal] load .dockerignore                                                                                                                                             0.0s
 => => transferring context: 111B                                                                                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.7.13-slim-buster                                                                                                  2.7s
 => exporting to oci image format                                                                                                                                            22.2s
 => => exporting layers                                                                                                                                                       4.0s
 => => exporting manifest sha256:dceec4fdc84fbac49fff46f71ad1dac40ac1a3ba1f2304323b30be6facb9c735                                                                             0.0s 
 => => exporting config sha256:4dc5ab9984f75a1c0f235869e381b822557d1e553bcd41c31d99d98c9d749e6f                                                                               0.0s
 => => sending tarball                                                                                                                                                       18.2s
unpacking docker.io/library/todo_app:latest (sha256:dceec4fdc84fbac49fff46f71ad1dac40ac1a3ba1f2304323b30be6facb9c735)...done

```

The next step is to test the local development setup using the following command:

```bash
docker run --env-file ./.env -p 4000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo_app:development
```

You should see see something like this:

```bash
docker run --env-file ./.env -p 4000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo_app:development
Skipping virtualenv creation, as specified in config file.

 * Serving Flask app "todo_app/app:create_app   " (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 957-903-041
```

If you desire to run the production environment, run the following command:

```bash
docker run --env-file ./.env -p 4000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo_app:production
```



Launching containers with long docker run commands can become tedious, and difficult to share with other developers

To get the app to run in the container using the docker-compose.yml, with the build flag so it rebuilds the image as necessary. The basic principle is the YAML docker-compose.yml file is used to launch the long docker run commands. 

```bash
docker-compose up --build 
```