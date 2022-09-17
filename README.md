# 0. Intro

Have you ever dreamed of having a conversation with a person from the distant past? 
Aristotle, William Shakespeare, Benjamin Franklin, Ada Lovelace … any person of your choice. 

Would you like to create your own digital replica?

The long-term goal of this project is to make it a reality. 

It should work as follows:

1. Collect all the writings of the person in one place.
2. Give it to AI-Replica.
3. The software will try to reconstruct the person’s mind.
4. If you ask the replica some question, it should provide an answer that is authentic to the original person.
5. If you ask the replica to do some intelligent task, it should be able to do it, as good as the original.

We plan to iteratively expand the replica’s capabilities, to make the conversation more natural and more authentic.

This software and the sample data are under very permissive Creative Commons Zero v1.0 Universal license
(basically, it describes a release into the Public Domain). 

# 1. How to use: Prerequisites

Clone this repo.

Navigate to the root dir of the repo.

Install `make` tool, so that you can execute useful commands from project's `makefile`.

Make sure Python3.9 is installed in the system and available via `python3.9` command. (By default, the server uses Rasa which supports Python3.9 as of August 2022.) 

Also make sure that the following packages are installed: 
- `python3.9-distutils`;
- `python3.9-venv`;
- `python3.9-dev`. 

(You can install them by running `sudo apt install python3.9-dev python3.9-venv python3.9-distutils`).

Install prerequisites: 

`make install_prerequisites`

Pre-requisites include:
- PyYAML Python module (it is required to read yaml config).
- colorama - used by installation script to output colored text in case of errors.


## Development
Install git hooks for the pre-push stage. See [documentation/python.md](documentation/python.md) for more info.
```bash
pip3 install pre-commit
pre-commit install --hook-type pre-push
```

Install Node.js for the webchat development.

Notes. 
- The project uses the [`black`](https://github.com/psf/black) code style.


# 2. How to use: Simlple Console Bot

Make sure that [Prerequisites ](#1-how-to-use-prerequisites) are satisfied.

Run the console bot:

`make run_simple_console_bot`

# 3. How to use: Server Bot

Make sure that [Prerequisites ](#1-how-to-use-prerequisites) are satisfied.

Install dependencies:
```bash
make install_dependencies
```

The previous command creates Python3.9 virtual environment (it should be created in the root folder). Activate the venv:
```bash
source venv/bin/activate
```

**!!! Make sure that all the subsequent commands and work are done in this venv. !!!**

*Note. Alternatively, you can install general and Rasa's dependencies manually using `requirements.txt` files in the root dir of the repo and in the `rasa` dir. (e.g. `python3.9 -m pip install -r requirements.txt`)*

Train Rasa model:

`make train_rasa_model`

Then you can launch all the servers by running:

`make start_all`

The UI chat will be available at `http://localhost:8000/chat/` (prod mode).

**Note**. It can take a couple of minutes for Rasa server to start. Until that the UI can work incorrectly. You can check the status of Rasa server in the corresponding terminal (the one that starts reporting the message "Starting Rasa server"). Once the Rasa server is up, the terminal should report "Rasa server is up and running".

## Development
Run all in dev mode (server and chat):

`make start_all_development_mode`

 The chat will open at `http://localhost:3000` (dev mode).

Run webchat in development mode manually:
- Go to the `webchat` folder.
- Install dependencies by running `npm install` or `npm ci`.
- Run `npm start`.
- The chat will open at `http://localhost:3000`

## Rasa

By default, Rasa bot engine is used. Before running the server, make sure that:
- Rasa server is being run at `http://localhost:8002`.
- Rasa actions server is being run at `http://localhost:8004`. 

To turn off Rasa engine, change the value of the `bot_engine setting` in `config.yaml`.

For how to start Rasa, check [Rasa docs](./documentation/rasa.md).

## Launch server

Run the server bot (default port is 8000, default address is localhost):

`python3 server_bot.py`

or:

`python3 server_bot.py --port=8000`

For help, run:

`python3 server_bot.py -h`

### Web chat
Build web chat by running `make build_ui`. Then copy web chat to the server's static folder: `make copy_web_chat_to_server`.

Then open your browser and navigate to the `\chat` path at the address and port the server listens on (by default, the port is 8000) (e.g. `http://localhost:8000/chat`).

### Preserving conversation history
By default, conversations are stored in sqllite in-memory db.
In case you want to preserve conversations history between server reloads, you need to:
- set path to db file in the `db_path` field in server's config.
- set sqlite in-file tracker store in Rasa's endpoints.yml (just uncomment the corresponding tracker store and provide path to you db file).

Note. Two dbs are used currently: server's one and Rasa's one - for the sake of concerns separation.

### Activating voice output
You can activate voice output in the UI chat by setting `text_to_speech_activated` option in the server's config to `true` and specifyig TTS engine.
Currently, the voice output can be provided by consuming Google's api on server-side. Also, pyttsx3 output is possible. 
Install `espeak-ng` for text-to-speech generation by pyttsx3: `sudo apt install espeak-ng`.

## Docs

Please check how to launch Rasa and other project-related Rasa docs here: [Rasa docs](./documentation/rasa.md).

# 4. Testing

To run doctests, execute `doctests_run`

# Code Style
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
