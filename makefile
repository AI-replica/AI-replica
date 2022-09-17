# make sure to make indentation via tabs not whitespaces as it is required by the `make` util
rasa_command_path := ./rasa/venv/bin/rasa
rasa_python_path := ./rasa/venv/bin/python3

# `.` is used instead of `source` which is a bash-specific command
activate_venv:
	. venv/bin/activate
build_ui:
	cd web_chat; npm run build;
build_ui_and_copy_to_server:
	build_ui copy_web_chat_to_server
copy_web_chat_to_server:
	rm -rf /server/static/chat/*; cp -a ./web_chat/build/. ./server/static/chat/;
create_venv:
	python3.9 -m venv venv
# does not work with python3.10: an error is visible in the terminal	
# debug_rasa_train:
# 	python3 -m debugpy --wait-for-client --listen localhost:5678 control.py train_rasa_model
# `.` is used instead of `source` which is a bash-specific command
debug_rasa_train2:
	cd rasa; . ./venv/bin/activate; cd bot; python3 --version; python3 -m debugpy --wait-for-client --listen localhost:5678 ../venv/bin/rasa train --domain domain
format_code:
	black .
freeze_requirements:
	python3 -m pip freeze > requirements.txt
install_dependencies:
	python3 control.py install_dependencies
install_prerequisites:
	python3 -m pip install colorama PyYAML
install_requirements:
	python3 -m pip install -r requirements.txt
lint_code:
	black --check .
reconstruct_mind:
	python3 control.py reconstruct_mind
run_console_bot:
	python3 console_bot.py
run_simple_console_bot:
	python3 simple_console_bot.py
start_all: start_rasa_actions start_rasa_server start_server start_ui
start_all_development_mode: start_rasa_actions start_rasa_server start_server_development_mode start_ui_dev_mode
start_console_chat:
	python3 console_chat.py
start_rasa_actions:
	python3 control.py start_rasa_actions
start_rasa_actions_with_debug_logs:
	python3 control.py start_rasa_actions_with_debug_logs
start_rasa_server:
	python3 control.py start_rasa_server
start_rasa_server_with_debug_logs:
	python3 control.py start_rasa_server_with_debug_logs
start_rasa_shell:
	echo "Need to call: rasa shell"
start_server:
	python3 control.py start_server
start_server_development_mode:
	SERVER_MODE=development python3 control.py start_server
start_ui:
	python3 control.py start_ui
start_ui_dev_mode:
	cd web_chat; npm start;
train_all_models:
	train_core_model train_rasa_model
train_core_model:
	python3 control.py train_core_model
train_rasa_model:
	python3 control.py train_rasa_model
