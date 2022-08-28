Test another TTS approach.

```pip install TTS```
```sudo apt-get install lzma```
```sudo apt-get install liblzma-dev```

The following error appears when running tts --list_models command: "ModuleNotFoundError: No module named '_lzma'"

Rebuild Python from source as explained here: https://github.com/lucidrains/imagen-pytorch/issues/92


