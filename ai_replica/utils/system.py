"""Tools for environment- and OS-related stuff"""

import os
import platform
import subprocess
import webbrowser


def is_expected_python_version(expected_version):
    """Returns True if the actual Python version is the same as the expected version, and False otherwise.

    It will also return True if the actual version is a subset of the expected version. For example:

    | expected | actual  | result |
    | -------- | ------- | ------ |
    | "3.8.1"  | "3.8.1" | True   |
    | "3.8"    | "3.8.1" | True   |
    | "3"      | "3.8.1" | True   |
    """
    actual_version = platform.python_version()
    return actual_version.startswith(expected_version)


def create_env_if_not_exist(env_path):
    """Creates a venv virtual environment"""
    if not os.path.exists(env_path):
        subprocess.call(["python3", "-m", "venv", env_path])
        print("created" + str(env_path))
        existed7 = False
    else:
        print(str(env_path) + " already exist")
        existed7 = True
    return existed7


def install_piped_requirements(pip_path, requirements_path):
    """Uses pip to install the requirements defined in the file located at requirements_path. Also updates pip"""
    subprocess.call([pip_path, "install", "-U", "pip"])  # updating pip
    subprocess.call([pip_path, "install", "-r", requirements_path])
    print(f"Installed dependencies according to {requirements_path}")


def execute_command(exec_path, command, work_dir=None, wait_till_finished7=False):
    """Runs an executable with a command.

    For example, if you want to run 'path/to/python3 server_bot.py', you can do it as follows:

    execute_command(exec_path="path/to/python3", command="server_bot.py")

    By default, the command will be executed in a separate process, and the script will not wait for the end of the execution.
    If it's not what you want, set wait_till_finished7=True
    """
    args = [exec_path] + command.split()
    print("launching the script " + str(command))
    if wait_till_finished7:
        subprocess.call(args, cwd=work_dir)
    else:
        subprocess.Popen(args, cwd=work_dir)


def set_environmental_variable(key, value):
    """Sets the value of an environmental variable.

    For example, if you want to execute 'SANIC_HOST localhost', you can do it as follows:

    set_environmental_variable(key='SANIC_HOST', value='localhost')
    """
    os.environ[key] = str(value)


def open_url_in_browser(url):
    """Opens the given url. As the result, the user will see the opened page in their default browser"""
    webbrowser.open(url, new=0, autoraise=True)
