# Low-Cost TTS

    Module for computational low-cost custom TTS.
    Working as an alternative to ML cloning voice. 
    And avoid the problem of a computer without
    much RAM or CPU or GPU. It is useful for
    Cloning a basic human voice. 
    In this URL, you can find a list in many languages of the frequent basic 1000
    words, just copy the list into vocabulary.txt and then start to teach to
    the computer to imitate your voice.
    
- [1000 most common words in many languages](https://github.com/bukowa/1000-common-words/blob/master/Spanish-1000-common.txt)


## Warranty

    None

## Documentation

    $ ./install_complements.sh
    $ pip install -r requirements.txt 
    $ python main.py

    You need a vocabulary file in the main folder with 1000 to 3000 most frequent words in the
    language target. Or get a big batch from your text dataset extracted from your data mining.
    The example in the folder is just for orientation.

## Folder structure

    ├── install_complements.sh\
    ├── main.py\
    ├── pronunciation_{lang}\
    ├── README.MD\
    ├── requirements.txt\
    └── vocabulary.txt\



## Testing
    
    OS:       Ubuntu Mate LTS 22.04 64 bits
    HW:       HP Laptop
    RAM:      15 GiB
    CPU:      AMD Ryzen 7 4700U with Radeon Graphics × 8 
    GRAPHICS: RENOIR (Renoir, LLVM 15.0.6, DRM 3.47, 5.19.0-45-generic)
    VERSION:  Python 3.10.6

## Workflow

    $ python3 main.py

### Dialog

    1. Start learning phase
    2. Start pronunciation phase
    3. Exit
    Enter your choice: 1
    Enter the language you want to learn: es
    Word: hola
    Speak the word or press Enter to skip:
    Press Enter to continue...
    Word: amigo
    Speak the word or press Enter to skip:
    Press Enter to continue...
    Word: mio
    Speak the word or press Enter to skip:
    Press Enter to continue...
    Learning finished.
    1. Start learning phase
    2. Start pronunciation phase
    3. Exit
    Enter your choice: 2
    Existing language folders:
    1. pronunciation_es
    Enter the number of the folder you want to continue with: hola
    Invalid folder choice.
    1. Start learning phase
    2. Start pronunciation phase
    3. Exit
    Enter your choice: 2
    Existing language folders:
    1. pronunciation_es
    Enter the number of the folder you want to continue with: 1
    Enter a sentence: hola
    Pronunciation finished.
    1. Start learning phase
    2. Start pronunciation phase
    3. Exit
    Enter your choice: 1
    Enter the language you want to learn: es
    Word: hola
    Speak the word or press Enter to skip:
    Press Enter to continue...
    Word: amigo
    Speak the word or press Enter to skip:
    Press Enter to continue...
    Word: mio
    Speak the word or press Enter to skip:
    Press Enter to continue...
    Learning finished.
    1. Start learning phase
    2. Start pronunciation phase
    3. Exit
    Enter your choice: 2
    Existing language folders:
    1. pronunciation_es
    Enter the number of the folder you want to continue with: 1
    Enter a sentence: hola
    Pronunciation finished.
    1. Start learning phase
    2. Start pronunciation phase
    3. Exit
    Enter your choice: 2
    Existing language folders:
    1. pronunciation_es
    Enter the number of the folder you want to continue with: 1
    Enter a sentence: hola amigo
    Pronunciation finished.
    1. Start learning phase
    2. Start pronunciation phase
    3. Exit
    Enter your choice: 2
    Existing language folders:
    1. pronunciation_es
    Enter the number of the folder you want to continue with: 1
    Enter a sentence: hola amigo mio
    Pronunciation finished.
    1. Start learning phase
    2. Start pronunciation phase
    3. Exit
    Enter your choice: 2
    Existing language folders:
    1. pronunciation_es
    Enter the number of the folder you want to continue with: 1
    Enter a sentence: amigo mio
    Pronunciation finished.
    1. Start learning phase
    2. Start pronunciation phase
    3. Exit
    Enter your choice: 3


## Resources


    Please, if not fail the script, the environment or your operative system then you need to 
    dive into the documentation's dependencies.


- [pyTTSx3](https://github.com/nateshmbhat/pyttsx3)

- [gTTS](https://gtts.readthedocs.io/en/latest/)

- [Playsound](https://github.com/TaylorSMarks/playsound)

- [SoundDevice](https://python-sounddevice.readthedocs.io/en/0.4.6/)

- [SciPy](https://pypi.org/project/scipy/)
