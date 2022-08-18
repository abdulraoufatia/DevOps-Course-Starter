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

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install the required packages, run the following from your preferred shell:

```bash
poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on the first setup:

```bash
cp .env.template .env  # (first time only)
```

The `.env` file is used by Flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Before Running the app

The set-up of this to_do app has been designed for Trello. Set up the .env file and place the information accordingly with your Trello account:

```bash
SECRET_KEY=secret-key # leave this as it is

API_KEY = 'abc'
API_TOKEN = 'def'
BOARD = 'ghi'
NOTSTARTED_LIST = 'klm'
INPROGRESS_LIST = 'nop'
COMPLETED_LIST =  'qrs'
PRIMARY_CONNECTION_STRING = 'zxc'
```

## Running the App

Once all dependencies have been installed and relevant information has been inputted, start the Flask app in development mode within the poetry environment by running:

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

Being a DevOps engineer invokes many responsibilities, one responsibility of a DevOps Engineer is to be involved in identifying required qualities and estimate their impact on the development process. This is done through the practice of testing.

In the world of software engineering, testing is an imperative practice constituting the security of your code.
Throughout this project, testing our software was achieved through the pytest framework.

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

To read more about pytest, please visit the pytest official website here: [pytest documentation] (<https://docs.pytest.org/en/6.2.x/contents.html>)

## DevOps Applications - Containerisation

This application utilises containerisation concept. Containerisation entails placing a software component and its environment, dependencies, and configuration, into an insolated unit called a container. This makes it possible to deploy an application consistently in any computing environment, whether on-premise or cloud-based.

To get started, you need to install a containerisation tool. A containerisation tool used for this project was Docker. However, you may find alternatives depending on your Operating System.

## Getting Started with Docker

### Build and run the Docker Image

This project is built using multi-stage builds. Multi-stage builds are useful to optimise Dockerfiles while keeping them easy to read and maintain.  

To build the development environment, run the following command:

```bash
docker build --target development --tag todo_app:development .
```

To build the production environment, run the following command:

```bash
docker build --target production --tag todo_app:production .
```

I have built the development environment image, you should see something similar to this:

```bash

(.venv) [Module_5 x] {} DevOps-Course-Starter docker build --target development --tag todo_app:development .
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

You should see something like this:

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

## Advanced Features of Docker - Docker Compose

Launching containers with long docker run commands can become tedious, and difficult to share with other developers. The basic principle of 'docker compose' is utilised to launch long docker run commands. So, rather than running the aforementioned commands, one could run a simple:

```bash
docker-compose up --build 
```

Note: docker-compose.yml is configured in YAML. To further develop your understanding, please see [this link](https://docs.docker.com/compose/gettingstarted/) --> Docker Compose Getting Started | See step 3

### Running Tests

This approach helps to identify bugs as early as possible. These inherent features of a DevOps testing environment contribute significantly toward improving software quality. A third Docker stage is included describing the ability to encapsulate a complete test environment( unit, integration and end-to-end tests).

If you have been following along, don't forget to stop the container, to stop a container you may run the following command:

```bash
docker-compose stop
```

To build the test image run the following command:

```bash
docker build --target test --tag test-image .
```

We can confirm the success of the event by having an output similar to the following :

```bash
devops-course-starter-web-1  | Skipping virtualenv creation, as specified in config file.
devops-course-starter-web-1  | ============================= test session starts ==============================
devops-course-starter-web-1  | platform linux -- Python 3.7.13, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
devops-course-starter-web-1  | rootdir: /app
devops-course-starter-web-1  | collected 4 items
devops-course-starter-web-1  | 
devops-course-starter-web-1  | todo_app/test/test_app.py .                                              [ 25%]
devops-course-starter-web-1  | todo_app/test/test_viewmodel.py ...                                      [100%]
devops-course-starter-web-1  | 
devops-course-starter-web-1  | ============================== 4 passed in 0.21s ===============================
devops-course-starter-web-1 exited with code 0
```

Knowledge of Automating  Testing is required to understand what is happening above.

#### Running individual containers

If you wish to run a container separately, use each command respectively either:

```bash
docker-compose up todo-development
```

```bash
docker-compose up todo-test
```

```bash
docker-compose up todo-production
```

## Application of Continuous Integration and Continuous Delivery

Continuous Integration (CI) is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. This repository CI pipeline is set in the following manner:

### Continuous Integration

1. It runs Snyk to check for vulnerabilities with the python application
2. It builds the test image
3. It runs the test image, printing the results of the test, if all is well it proceeds with the next step;
4. Notification is sent

### Continuous Delivery

1. The second job will run upon the success of the first job (CI)
2. Docker buildx is set up
3. Docker is authenticated
4. Production image is pushed to docker (using argument  `target: production`)
5. Image deployed on Azure App Service
6. Notification is sent

### Important Heroku Dockerfile commands and runtime

- If argument `target : <name_of_env>` is set to a specific target, it will upload the target name, the stage by default will upload the last stage. This is because, in our application, it's production, if you were to change this to `test`, the `test` target stage will be pushed to Dockerhub (action name = Pushing to DockerHub )
- The web process must listen for HTTP traffic on $PORT, which is set by Heroku
- EXPOSE in Dockerfile is not respected, but can be used for local testing. Only HTTP requests are supported.

Heroku CI/CD action:

```
    - name: Deploying to Heroku
      
      uses: akhileshns/heroku-deploy@v3.12.12 
      
      with:
        
        heroku_api_key: ${{secrets.HEROKU_API_KEY}}
        
        heroku_app_name: "todo-app-apprenticeship"
        
        heroku_email: ${{ secrets.HEROKU_USERNAME }}
        
        usedocker: true 
```

## Tooling and Cloud Infrastructure

### Getting Ready

One would need to have an Azure account set up for this part. If you do not have an Azure Account, create one here at [Microsoft Azure - GB](https://azure.microsoft.com/en-gb/free/) (azure.microsoft.com).

#### Setting up an Azure Account

When prompted select the "Start with an Azure free trial". This gives 12 months of access to some resources, and $150 credit for 30 days, along with "always free" tiers for most common resources. One could use the  Free Tier for this exercise, ensure you select the "FREE Tier" or "SKU F1" when creating resources, as the default is usually the cheapest paid option. The Free Tier and Free Subscription have some downsides: the size, scalability and some functionality of resources are limited, and you can
only have one or two of each resource type taking advantage of the Free Subscription.

If you see an error like "The subscription you have selected already has an app with free tier enabled" then you should either delete the existing resource in the Portal or opt for the cheap-but-paid Basic Tier for your resource.

#### Creating and Locating a Resource Group

A resource group is a logical container into which Azure resources, such as web apps, databases, and storage accounts, are deployed and managed. More Azure Terminology [here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview#terminology).

- Within the portal, search for "Resource group"
- Click on  "+ Create". It will open a form to create a resource group. Select your subscription.

#### Installing the CLI

The Azure Command-Line Interface (CLI) allows the execution of commands through a terminal using interactive command-line prompts or a script. Furthermore, the CLI is available to install in Windows, macOS and Linux environments. It can also be run in a Docker container and Azure Cloud Shell.

Once installed, open a new terminal window and enter `az login`, which will launch a browser window to allow you to log in.

### Install on Windows

For Windows, the Azure CLI is installed via the Microsoft Installer (MSI), which gives you access to the CLI through the Windows Command Prompt (CMD) or PowerShell. When installing for Windows Subsystem for Linux (WSL), packages are available for your Linux distribution. See the main install page for the list of supported package managers or how to install manually under WSL.

The current version of the Azure CLI is 2.38.0. For information about the latest release, see the release notes. To find your installed version and see if you need to update, run `az version`.

Microsoft Installer: [Link](https://aka.ms/installazurecliwindows) (aka.ms/installazurecliwindows)

### Install on macOS

With Homebrew, it is the easiest way to manage your CLI install. It provides convenient ways to install, update, and uninstall. If you don't have homebrew available on your system, [install homebrew](https://docs.brew.sh/Installation.html) before continuing.

You can install the Azure CLI on macOS by updating your brew repository information, and then running the `install` command:

``` brew update && brew install azure-cli ```

*The Azure CLI has a dependency on the* Homebrew python@3.10 package and will *install it.*

For troubleshooting, please see [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos#troubleshooting) (docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos#troubleshooting).

### Hosting Frontend on Azure

Side note: Azure App Service" with Containers vs "Azure Container Instances"

Azure App Services are set up for hosting long-running web applications, with a nice setup for front-facing web applications, with SSL and domain names built in, and allows either raw code or a Container Image to be uploaded.

- One Basic Tier App Service is part of the "Always Free" offering from Azure.

- Azure Container Instances are for lightweight short-run "compute" containers and quickly releasing local Docker compose-based apps. They are faster to deploy and billed per-second, with better orchestration for multiple containers. However, they are more expensive than App Services to run for extended periods and aren't as suited to production web applications.

- Azure Container Apps are a relatively new (General Availability Q2 2022) way of running containers on Azure, with built-in autoscaling support and a focus on microservices

#### Uploading Container Image on DockerHub registry

As Azure Container Registry (ACR) has a cost attached to it, so, therefore, this project is set up with container images pushed to the DockerHub registry. This CI/CD pipeline contains an action that it uploads to Docker Hub Registry.

#### Creating a Web App

<Webapp_name> needs to be *globally* unique, and will form part of the URL of the deployed app: <<https://<webapp_name>.azurewebsites.net>>.

Below are two different methods of how one can create the web_app:

- Portal
  - Within the portal, search for `App Services`
  - Click on `+ Create button`
  - Choose the right `Resource Group`
  - Name your App Service -  *Globally Unique*
  - Choose the desired `OS`
  - Chose the best `region` for low latency
  - Click Next: Docker
  - For `Image Source`, choose the appropriate   source, for the todo app, we will choose `Docker Hub`
  - Leave the rest as default, others are optional and may have an additional costings involved and `create`

- CLI

  - Create the Service App Plan:

`az appservice plan create --resource-group <resource_group_name> -n <appservice_plan_name> --sku B1 --is-linux`

- Create the Web App:

  `az webapp create --resource-group <resource_group_name> --
plan <appservice_plan_name> --name <webapp_name> --deployment-container-image-name <dockerhub_username>/todo-app:latest`

#### Setting up the Environment Variables

- Portal

  - Under the `Settings Blade`, Click on `Configuration`
  - Add all environment variables accordingly to your .env file as `New application Setting`
  - Remember to press save!

- CLI

  - You can enter environment variables individually via:

     `az webapp config appsettings set -g <resource_group_name> -n
     <webapp_name> --settings FLASK_APP=todo_app/app. <env1=token> <env2=key>`

     Don't forget to add all the environment variables your application needs.

#### Confirming Status of Application

Browse to `<http://<webapp_name>.azurewebsites.net/>` and confirm no functionality has been lost.

### Setting up Continuous Deployment

When creating an app service, Azure sets up a webhook URL. Post requests to this endpoint cause your app to restart and pull the latest version of the container
image from the configured registry.

- Find the webhook URL: From the app service in Azure Portal, navigate to Deployment Center

- Test webhook provided with:

`curl -dH -X POST your_webhook_url`

- To prevent the `$username` part of the webhook being interpreted by your shell as a variable name place
backslash before the dollar sign. For example:
`curl -dH -X POST https://\$my-todo-app:abc123@...etc`

- The command was then added to the CD pipeline