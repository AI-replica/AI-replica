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

## 1. How to use

Clone this repo.

Navigate to the AI-replica dir.

Run the console bot:
`python3 console_bot.py`

### Rasa launcher
`python3 rasa_laucher.py` - installs all the dependnecies and starts rasa server and rasa actions server.

### Server bot
Run the server bot (default port is 8000, default address is localhost):
`python3 server_bot.py`

or:
`python3 server_bot.py --port=8000`

For help, run:
`python3 server_bot.py -h`

Then open your browser and navigate to the address and port server listens on.

By default, Rasa bot engine is used. Before running the server, make sure that Rasa server is being run at `http://localhost:8002`. Can be changed in `config.yaml`. Also make sure that Rasa actions server is being run at `http://localhost:8004`. 
To turn off Rasa engine, change the value of bot_engine setting in `config.yaml`.

### Rasa
**IMPORTANT.** Install Python 3.8 first as Rasa does not support later versions yet (as of January 2022).

Go to "rasa" folder, create virtual environment and switch to the created virtual environment: 
```
cd rasa
python3.8 -m venv ./venv
source ./venv/bin/activate
```

Install latest version of pip: `pip3 install -U pip`

Install Rasa by running `pip3 install rasa` or install dependencies from `requirements.txt` by running `pip3 install -r requirements.txt`.

Go to the `bot` folder. It is a Rasa project folder. It contains data for the bot. Run all the Rasa-related commands from this folder.

Use `rasa train --domain domain` to train your model. The trained model will appear in the `models` folder.


Start Rasa server: `rasa run -i localhost -p 8002`.

As per default config, the AI Replica server expects the Rasa server is being run at http://localhost:8002.
By default, the latest model from the `models` folder is used. If you want to run a specific model, you can do it as follows: `rasa run -i localhost -p 8002 --model models/20220122-164843-charitable-rent.tar.gz`.


Start Rasa actions server as follows: `SANIC_HOST=localhost rasa run actions -p 8004`.

#### Notes
1. Command line interface: https://rasa.com/docs/rasa/command-line-interface
2. Installation: https://rasa.com/docs/rasa/installation/. Install Python 3.8 first as Rasa does not support later versions yet (as of January 2022). In the `pip3 install -U --user pip && pip3 install rasa` command remove `--user` flag, otherwise you can experience an error saying that execution is not possible ("Can not perform a '--user' install. User site-packages are not visible in this virtualenv."). There is no sense to install packages to user folder (--user) when you are in a virtual environment.

## 2. Testing

To run doctests, execute `doctests_run`
