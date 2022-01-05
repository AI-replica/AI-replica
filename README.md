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

### Server bot
Alternatively, run the server bot (default port is 8000, default adress is localhost):
`python3 server_bot.py`

or:
`python3 server_bot.py --port=8001`

For help, run:
`python3 server_bot.py -h`

Then open your browser and navigate to the address and port server listens.

## 2. Testing

To run doctests, execute `doctests_run`