"""Tools for environment- and OS-related stuff"""

import os
import platform
import subprocess
import time
import webbrowser

from ai_replica.utils.files import is_file, get_main_dir_path


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


def get_python_exec_name(python_version=None):
    """Returns a string like 'python3.8', given the python version (e.g. '3.8')"""
    if python_version == None:
        return "python3"
    return "python" + python_version


def create_env_if_not_exist(env_path, python_version):
    """Creates a venv virtual environment"""
    if not os.path.exists(env_path):
        python_exec_name = get_python_exec_name(python_version)
        subprocess.call([python_exec_name, "-m", "venv", env_path])
        print("created" + str(env_path))
        existed7 = False
    else:
        print(str(env_path) + " already exist")
        existed7 = True
    return existed7


def install_requirements_with_pip(pip_path, requirements_path):
    """Uses pip to install the requirements defined in the file located at requirements_path. Also updates pip"""
    subprocess.call([pip_path, "install", "-U", "pip"])  # updating pip
    subprocess.call([pip_path, "install", "-r", requirements_path])
    print(f"Installed dependencies according to {requirements_path}")


def install_dependencies(
    pip_path, venv_path, requirements_path, python_version, name=""
):
    if is_file(pip_path):
        print(f"It seems that {name} requirements are already installed, which is nice")
    else:
        create_env_if_not_exist(venv_path, python_version)
        install_requirements_with_pip(pip_path, requirements_path)


def install_replica_dependencies(python_version):
    """Installs the dependencies that are necessary to run the core functionality of AI-replica."""
    main_dir_abs = get_main_dir_path()
    venv_dir_abs = main_dir_abs + "/venv"
    pip_exec_path_abs = venv_dir_abs + "/bin/pip3"
    requirements_path_abs = main_dir_abs + "/requirements.txt"

    install_dependencies(
        pip_exec_path_abs,
        venv_dir_abs,
        requirements_path_abs,
        python_version,
        name="AI-replica",
    )


def execute_command(
    exec_path,
    command,
    work_dir=None,
    wait_till_finished7=False,
    run_in_another_terminal7=False,
):
    """Runs an executable with a command.

    For example, if you want to run 'path/to/python3 server_bot.py', you can do it as follows:

    execute_command(exec_path="path/to/python3", command="server_bot.py")

    By default, the command will be executed in a separate process, and the script will not wait for the end of the execution.
    If it's not what you want, set wait_till_finished7=True
    """
    args = [exec_path] + command.split()
    print("launching the script " + str(command))

    if run_in_another_terminal7:
        args = ["gnome-terminal", "--"] + args

    if wait_till_finished7:
        subprocess.call(args, cwd=work_dir)
    else:
        subprocess.Popen(args, cwd=work_dir)


def kill_processes(expected_command_line_part, sleep_sec=30):
    # Importing it here to avoid problems with requirements installation automation
    import psutil

    # TODO: check if the kill was successful, and return the result. Optionally, wait until it is actually killed
    for process in psutil.process_iter():
        actual_line = " ".join(process.cmdline())
        if expected_command_line_part in actual_line:
            process.kill()
    time.sleep(sleep_sec)  # to give it time to offload the processes from the memory


def set_environmental_variable(key, value):
    """Sets the value of an environmental variable.

    For example, if you want to execute 'SANIC_HOST localhost', you can do it as follows:

    set_environmental_variable(key='SANIC_HOST', value='localhost')
    """
    os.environ[key] = str(value)


def open_url_in_browser(url):
    """Opens the given url. As the result, the user will see the opened page in their default browser"""
    webbrowser.open(url, new=0, autoraise=True)
