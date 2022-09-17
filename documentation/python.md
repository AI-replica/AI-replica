# Debug
`breakpoint()` - set breakpoint in code
`debugpy` - A debugger for Python: https://github.com/microsoft/debugpy

# Sanic
`A webserver for Python: https://sanic.dev/en/.
Serve static files: https://sanic.dev/en/guide/basics/routing.html#static-files
Extensions/plugins: https://sanic.dev/en/plugins/sanic-ext/getting-started.html
CLI: https://sanic.dev/en/guide/deployment/running.html#running-via-command

## Notes

- When Sanic report "[INFO] Starting worker", it means that the server is started and ready to server requests.

# Black
A code formatter for Python: https://github.com/psf/black.
Documentation: https://black.readthedocs.io/en/stable/

# pre-commit
Git hooks for Python: https://pre-commit.com/.
Adding custom hooks: https://pre-commit.com/#new-hooks
Sample hooks: https://github.com/pre-commit/pre-commit-hooks

## Local Hooks
https://pre-commit.com/#repository-local-hooks

# APScheduler

Job scheduler for Python.
https://pypi.org/project/APScheduler/

Docs: https://apscheduler.readthedocs.io/en/master/userguide.html
Git: https://github.com/agronholm/apscheduler

# Datetime UTC

## Get current datetime in UTC

Warning Because naive datetime objects are treated by many datetime methods as local times, it is preferred to use aware datetimes to represent times in UTC. As such, the recommended way to create an object representing the current time in UTC is by calling datetime.now(timezone.utc). (source: https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow)

## Get datetime in UTC from POSIX timestamp

Warning Because naive datetime objects are treated by many datetime methods as local times, it is preferred to use aware datetimes to represent times in UTC. As such, the recommended way to create an object representing a specific timestamp in UTC is by calling datetime.fromtimestamp(timestamp, tz=timezone.utc). (source: https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp)

# pip

## Install package from github

pip allows installing packages from git: from a branch, tag, commit, etc. The packages can be installed in editable and normal modes.

pip docs: https://pip.pypa.io/en/stable/topics/vcs-support/

Installing private Python packages: https://docs.readthedocs.io/en/stable/guides/private-python-packages.html

https://stackoverflow.com/a/20548189

Install package in normal mode, i.e. the package is installed globally: `python3 -m pip install "git+https://github.com/nateshmbhat/pyttsx3.git@5d3755b060a980f48fcaf81df018dd06cbd17a8f#egg=pyttsx3"`. 

Install package in editable mode, i.e. the package is installed in the `src` folder of the current directory (default folder): `python3 -m pip install -e "git+https://github.com/nateshmbhat/pyttsx3.git@5d3755b060a980f48fcaf81df018dd06cbd17a8f#egg=pyttsx3"`.

Editable installs: https://pip.pypa.io/en/stable/topics/vcs-support/#editable-vcs-installs

# VSCode

## Select Python interpreter

- Open Commmand Palette.
- Find the command: Python: select interpreter
- Enter the path to the Python interpreter (e.g. /usr/local/bin/python3)

## Debug Python
[Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging)

https://code.visualstudio.com/docs/python/debugging#_python
