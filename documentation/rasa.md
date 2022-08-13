# Rasa
**IMPORTANT.** Install Python 3.9 first as Rasa does not support later versions yet (as of July 2022).

## Automatic launch

You can start Rasa by calling `python3 rasa_launcher.py` from the root directory.

## Manual launch

Go to "rasa" folder, create virtual environment and switch to the created virtual environment: 
```
cd rasa
python3.9 -m venv ./venv
source ./venv/bin/activate
```

Install latest version of pip: `pip3 install -U pip`

Install Rasa by running `pip3 install rasa` or install dependencies from `requirements.txt` by running `pip3 install -r requirements.txt`.

Install spaCy (currently, spaCy model is used by the replica's pipeline):
```
pip3 install rasa[spacy]
python3 -m spacy download en_core_web_lg
```

Go to the `bot` folder. It is a Rasa project folder. It contains data for the bot. Run all the Rasa-related commands from this folder.

Use `rasa train --domain domain` to train your model. The trained model will appear in the `models` folder.

Start Rasa server: `rasa run -i localhost -p 8002`.

As per default config, the AI Replica server expects the Rasa server is being run at http://localhost:8002.
By default, the latest model from the `models` folder is used. If you want to run a specific model, you can do it as follows: `rasa run -i localhost -p 8002 --model models/20220122-164843-charitable-rent.tar.gz`.


Start Rasa actions server as follows: `SANIC_HOST=localhost rasa run actions -p 8004`.

## Debug Rasa
You can get access to some useful Rasa internal info, e.g. intent confidence, via Rasa http api. To activate the api, start Rasa server with `--enable-api` flag, e.g. `rasa run -i localhost -p 8002 --enable-api`.

Then you can, for example, access conversation events via calling `http://localhost:8002/conversations/user/tracker`. **Note.** Here, 'user' is the value of the 'sender' field sent by bot server to Rasa webhook api (see request_handler.py).

Check Tracker api here: `https://rasa.com/docs/rasa/pages/http-api/#tag/Tracker`.

Also, you can run Rasa with `--debug` flag to see some useful output in the console. E.g. `rasa run -i localhost -p 8002 --debug`.

Potentially, it is even more convenient to install Rasa X for the purpose of debugging but it is intended primarily for server-mode setup, so the installation and running is not so straightforward.

## Notes
1. Command line interface: https://rasa.com/docs/rasa/command-line-interface
2. Installation: https://rasa.com/docs/rasa/installation/. Install Python 3.8 first as Rasa does not support later versions yet (as of January 2022). In the `pip3 install -U --user pip && pip3 install rasa` command remove `--user` flag, otherwise you can experience an error saying that execution is not possible ("Can not perform a '--user' install. User site-packages are not visible in this virtualenv."). There is no sense to install packages to user folder (--user) when you are in a virtual environment.

# Useful stuff
`rasa shell` command starts bot in a terminal.
`--debug` flag passed to a rasa command allows seeing some debug information.

# Conversation stores
## Sqlite
Install (on Ubuntu): `sudo apt install sqlite3`
Create a folder where you db will be stored. sqlite does not create folder and throws an error if the folder does not exist. The db file is created by sqlite itself.
Configure: [Tracker Stores](https://rasa.com/docs/rasa/tracker-stores/#sqltrackerstore)
```yaml
tracker_store:
   type: SQL
   dialect: sqlite
   url: sqlite:///../../../db/rasa.db # specify path to a db file after sqlite:///
   db: rasa.db
   username: 
   password: 
```

# API
## webhook
By default, Rasa server provides webhook api: [see](https://rasa.com/docs/rasa/http-api/), [see](https://rasa.com/docs/rasa/connectors/your-own-website#restinput). It looks like webhook is a conversation channel, i.e. it allows to send input messages from user and receive replies from the bot but does not provide access to anything else. E.g. you can have the following webhooks (channels): rest, socket.io, slack, etc.

## http api
To have access to additional functionality of a Rasa server, you can start server with exposed api: [Http API](https://rasa.com/docs/rasa/http-api/), 
**Note** Make sure that the api endoints are protecte either with authorization or hidden behind a proxy server/app router, so that they are not exposed to the Internet.


