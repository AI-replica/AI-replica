# make sure to make indentation via tabs not whitespaces as it is required by the `make` util
rasa_command_path := ./rasa/venv/bin/rasa
rasa_python_path := ./rasa/venv/bin/python3

build_ui:
	python3 build_web_chat.py
format_code:
	black .
freeze_requirements:
	python3 -m pip freeze > requirements.txt
install_rasa:
	echo "Not implemented..."
install_replica_dependencies:
	python3 control.py install_replica_dependencies
install_requirements:
	python3 -m pip install -r requirements.txt
reconstruct_mind:
	python3 control.py reconstruct_mind
run_console_bot:
	python3 console_bot.py
start_all: start_rasa_actions start_rasa_server start_server start_ui
start_rasa_actions:
	python3 control.py start_rasa_actions
start_rasa_server:
	python3 control.py start_rasa_server
start_rasa_server_with_debug_logs:
	python3 control.py start_rasa_server_with_debug_logs
start_rasa_shell:
	echo "Need to call: rasa shell"
start_server:
	python3 control.py start_server
start_ui:
	python3 control.py start_ui
train_rasa_model:
	python3 control.py train_rasa_model
# does not work with python3.10: an error is visible in th terminal	
# debug_rasa_train:
# 	python3 -m debugpy --wait-for-client --listen localhost:5678 control.py train_rasa_model
# `.` is used instead of `source` which is a bash-specific command
debug_rasa_train2:
	cd rasa; . ./venv/bin/activate; cd bot; python3 --version; python3 -m debugpy --wait-for-client --listen localhost:5678 ../venv/bin/rasa train --domain domain
