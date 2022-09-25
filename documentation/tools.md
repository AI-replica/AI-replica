# React
`react` - a library for building UI apps: https://reactjs.org/.
Adding custom environment variable: https://create-react-app.dev/docs/adding-custom-environment-variables/
Create React App: https://create-react-app.dev/docs/
Add typescript (to new project and to existing project): https://create-react-app.dev/docs/adding-typescript/
Note. When adding typescript to the existing project, you can face an issue that the `tsconfig.json` is not gerenrated automatically. See the following link on how to solve the issue: https://stackoverflow.com/questions/70397360/react-cant-resolve-tsx-files. Basically, you need to genearet a new recat typescript project and copy the file `tsconfig` from there.

## Deployment
https://create-react-app.dev/docs/deployment/


## React Router
https://reactrouter.com/docs/en/v6/getting-started/tutorial

# gTTS

gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.

https://pypi.org/project/gTTS/


It looks like gTTS does not allow to change a voice for a language, so for "en" ("en-US") it is always females voice as of August 2022.

# pyttsx3

Text-to-speech engine.

https://pypi.org/project/pyttsx3/
https://pyttsx3.readthedocs.io/en/latest/engine.html

Supported syntheziers: https://pyttsx3.readthedocs.io/en/latest/support.html

**Note**. The latest version is 2.90, released on 06.07.2020: https://github.com/nateshmbhat/pyttsx3/tags.
**Note**. The latest version tries to load `libespeak.so.1` lib (source: https://github.com/nateshmbhat/pyttsx3/blob/v.2.90/pyttsx3/drivers/_espeak.py). At the same time `espeak-ng` package provides the library `libspeak-ng.so.1`.
**Note**. on Ubuntu, it requires installation of [espeak-ng](#espeak-espeak-ng).

## eSpeak, eSpeak-ng

The pyttsx3 requires a speech synthesizer library to be intalled in the OS. For Linux, it is espeal or espeak-ng.

espeak-ng: https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md
MR that added support for espeak-ng: https://github.com/nateshmbhat/pyttsx3/pull/163/files
espeak-mg git: https://github.com/espeak-ng/espeak-ng

# mozilla/coqui tts

It looks like the TTS project is being developed by Coqui now.
> Coqui-TTS is the successor to Mozilla-TTS: some time ago Mozilla stopped their STT and TTS project. Coqui.ai was founded by members of the former Mozilla team.

(source: https://github.com/coqui-ai/TTS/discussions/1292#discussioncomment-2250327)

- https://rasa.com/blog/how-to-build-a-voice-assistant-with-open-source-rasa-and-mozilla-tools/
- The sample model can be downloaded from [here](https://drive.google.com/drive/folders/1GU8WGix98WrR3ayjoiirmmbLUZzwg4n0) or a model provided by the TTS framework can be used.
- https://gist.github.com/JustinaPetr/e43b84a9664f20c24eb5bb8fe75d4a0a
- https://github.com/mozilla/TTS/wiki
- https://pypi.org/project/TTS/
- https://github.com/coqui-ai/TTS
- https://github.com/coqui-ai/TTS/blob/dev/TTS/bin/synthesize.py

The following model is used by default (as of September 2022):
 > tts_models/en/ljspeech/tacotron2-DDC is already downloaded.
 > vocoder_models/en/ljspeech/hifigan_v2 is already downloaded.
 > Using model: Tacotron2




### Installation

`sudo apt install ffmpeg`
`sudo apt install espeak-ng`
Modify pptsx3/_espeak - load libespeak-ng.so.1 instead of libespeak.so.1. See [pyttsx3](#pyttsx3).

# GitHub Actions

https://github.com/features/actions
https://docs.github.com/en/actions

## Execute custom command from makefile
https://stackoverflow.com/a/66922092

## Execute custom python script

https://stackoverflow.com/q/70458458

## View workflow output

https://github.com/AI-replica/AI-replica/actions

You can click on an individual workflow run to see the output, i.e. how the steps were executed.

## Jobs

https://docs.github.com/en/actions/using-workflows/about-workflows

Every job is run on a runner machine. Two jobs are run on two different runners. By default the jobs are run in parallel.

## Caching dependencies

https://github.com/actions/setup-python#caching-packages-dependencies
https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#caching-packages

## Kill command on timeout

There is `timeout` command in Linux that can kill the command on timeout: https://linuxize.com/post/timeout-command-in-linux/

In the following example, timeout runs the command for one minute, and if it is not terminated, it will kill it after ten seconds:
`sudo timeout -k 10 1m ping 8.8.8.8`

If no signal is given, timeout sends the SIGTERM signal to the managed command when the time limit is reached. You can specify which signal to send using the -s (--signal) option. The signal is sent to the managed command, i.e. to the command that is executed with timeout, i.e. `ping` command in the sample below.
`sudo timeout -s 9 ping 8.8.8.8`

Run command with timeout in github workflow: https://stackoverflow.com/questions/63641822/run-command-with-timeout-in-github-workflow

# Bash

## Conditionals

`if-else-fi`: https://linuxize.com/post/bash-if-else-statement/
