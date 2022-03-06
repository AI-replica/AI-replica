"""Rasa-related utils"""

from ai_replica.utils.files import get_main_dir_path
from ai_replica.utils.system import set_environmental_variable, execute_command


def get_rasa_paths():
    """Returns various paths that are used during the Rasa launch"""
    rasa_dir_abs = get_main_dir_path() + "/rasa"
    venv_path_abs = rasa_dir_abs + "/venv"
    working_dir_abs = rasa_dir_abs + "/bot"
    requirements_path_abs = rasa_dir_abs + "/requirements.txt"
    rasa_exec_path_abs = venv_path_abs + "/bin/rasa"
    pip_exec_path_abs = venv_path_abs + "/bin/pip3"
    return (
        venv_path_abs,
        working_dir_abs,
        requirements_path_abs,
        rasa_exec_path_abs,
        pip_exec_path_abs,
    )


def start_rasa_main_server(rasa_exec, working_dir):
    """Starts the main Rasa server by executing a command like this: `rasa run -i localhost -p 8002`."""
    execute_command(rasa_exec, "run -i localhost -p 8002", working_dir)


def start_rasa_actions_server(rasa_exec, working_dir):
    """Starts the Rasa server for actions"""
    set_environmental_variable(key="SANIC_HOST", value="localhost")
    execute_command(rasa_exec, "run actions -p 8004", working_dir)


def train_model(rasa_exec, work_dir):
    """Executes `rasa train --domain domain` to train your model.

    The trained model will appear in the `models` folder."""
    execute_command(rasa_exec, "train --domain domain", work_dir, wait_till_finished7=True)
