## 0. Intro

Have you ever dreamed of having a conversation with a person from the distant past? 
Aristotle, William Shakespeare, Benjamin Franklin, Ada Lovelace … any person of your choice. 

Would you like to create your own digital replica?

The long-term goal of this project is to make it a reality. 

It should work as follows:

1. Collect all the writings of the person in one place
2. Give it to AI-Replica
3. The software will try to reconstruct the person’s mind 
4. If you ask the replica some question, it should provide an answer that is authentic to the original person.
5. If you ask the replica to do some intelligent task, it should be able to do it, as good as the original.

We plan to iteratively expand the replica’s capabilities, to make the conversation more natural and more authentic.

This software and the sample data are under very permissive Creative Commons Zero v1.0 Universal license
(basically, it describes a release into the Public Domain). 

## 1. How to use: Prerequisites

Clone this repo.

Navigate to the AI-replica dir.

Install `make` tool, so that you can execute useful commands from project's `makefile`.

Make sure Python3.9 is installed in the system and available via `python3.9` command. Also make sure that the following packages are installed: `python3.9-distutils`, `python3.9-venv`, `python3.9-dev`. (You can install them by running `sudo apt install python3.9-dev python3.9-venv python3.9-distutils`).

Install PyYAML Python module. It is required to read yaml config.

`make install_yaml`

All the following commands should be performed under the created virtual environment.


## 2. How to use: Console bot

Make sure that [Prerequisites ](#1-how-to-use-prerequisites) are satisfied.

Run the console bot:
`make run_console_bot`

## 3. How to use: Server bot

Make sure that [Prerequisites ](#1-how-to-use-prerequisites) are satisfied.

Install some dependencies required to run `install_replica_dependencies` command: 
`python3 -m pip install gtts requests psutil PyYAML`.

By default the server uses Rasa. 
Install Rasa if not installed. You can do it manually (see [Rasa docs](./documentation/rasa.md)) or run the following command:
`make install_replica_dependencies`.

Activate the created venv (it should be created in the root folder):
`source venv/bin/activate`

Make sure that all the subsequent commands are executed in the venv.

Build UI chat by runnning:
`make build_ui`

Train Rasa model:
`make train_rasa_model`

Then you can launch all the servers by running:
`make start_all`

The UI chat will be available at `http://localhost:8000`.

### Rasa

By default, Rasa bot engine is used. Before running the server, make sure that:
- Rasa server is being run at `http://localhost:8002`. Can be changed in `config.yaml`. 
- Rasa actions server is being run at `http://localhost:8004`. 

To turn off Rasa engine, change the value of the `bot_engine setting` in `config.yaml`.

For how to start Rasa, check [Rasa docs](./documentation/rasa.md).

### Launch server

Run the server bot (default port is 8000, default address is localhost):
`python3 server_bot.py`

or:
`python3 server_bot.py --port=8000`

For help, run:
`python3 server_bot.py -h`

### Web chat
Build web chat by running `make build_ui`. The web chat will be prepared in the `dist` folder.

Then open your browser and navigate to the address and port server listens on (by default, the port is 8000).

### Preserving conversation history
By default, conversations are stored in sqllite in-memory db.
In case you want to preserve conversations history between server reloads, you need to:
- set path to db file in the `db_path` field in server's config.
- set sqlite in-file tracker store in Rasa's endpoints.yml (just uncomment the corresponding tracker store and provide path to you db file).

Note. Two dbs are used currently: server's one and Rasa's one - for the sake of concerns separation.

### Activating voice output
You can activate voice output in the UI chat by setting `text_to_speech_activated` option in the server's config to `true`.
Currently, the voice output is provided by consuming Google's api on server-side.

### Docs

Please check how to launch Rasa and other project-related Rasa docs here: [Rasa docs](./documentation/rasa.md).

## 4. Testing

To run doctests, execute `doctests_run`
