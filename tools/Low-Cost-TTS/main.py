""" Low-Cost Text To Speech.

    This module is for making a custom TTS with the voice of the user.
    It is an alternative to the cloning voice with Ml technics.
    It is useful for low-cost computational resources.
    And suitable for low consume chatbots.

"""

# Imports
import os
import time
from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
import pyttsx3
from pydub import AudioSegment


# Learning phase
def learning_phase(language):
    """Learning phase.

        The function is called by the menu.
        Create a specific folder in a defined language
        based in abbreviated international code (es, en ...)
        Load a list between 1000 and 3000 more
        frequently used words in a language.
        From a text file. The user can load in the
        project another vocabulary.
        File is vocabulary.txt

        The text file is consumed like a list.
        The list is iterated sequentially in order
        to record every word with the associated sound.

        The sound is stored in the language folder: pronunciation_{lang}
        Until the learning cycle ends.

    """
    pronunciation_folder = "pronunciation_" + language

    if not os.path.exists(pronunciation_folder):
        os.makedirs(pronunciation_folder)
    # Open vocabulary and load the list
    words = []
    with open('vocabulary.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    # Get pronunciation folder filenames
    pronunciation_list = os.listdir(pronunciation_folder)
    pronunciation_list = [filename.split('.')[0] for filename in pronunciation_list]
    # Create a list of missing words in the pronunciation list
    missing_words = [word for word in words if word not in pronunciation_list]
    # Show missing words in pronunciation list
    print("Missing words in pronunciation list:")
    print(len(missing_words))
    current_word_index = 0

    while current_word_index < len(missing_words): # old words variable list
        current_word = missing_words[current_word_index]  # old words variable list
        print("Word:", current_word)

        audio_file = os.path.join(pronunciation_folder, current_word + ".wav")

        # Recording loop
        # Params
        fs = 44100  # Sample rate
        seconds = 1  # Duration of recording
        is_recording = False
        silent_frames = 0

        print("Speak the word after press enter")
        while True:

            if not is_recording:
                is_recording = True

            if is_recording:
                silent_frames += 1

            if is_recording and silent_frames > 10:
                break

        # Save audio to file
        # Record
        input(f'Press Enter to record, pay attention, is around {seconds} sec.')
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write(audio_file, fs, recording)  # Save as WAV file
        time.sleep(1)
        input("Press Enter to continue...")
        current_word_index += 1

    print("Learning finished.")


# Pronunciation phase
def pronunciation_phase(language):
    """ Pronunciation phase.

        The function is called by the menu.
        Load the vocabulary.txt into a list called words.
        The prompt ask for a phrase and the procedure
        read and list every word. and compare it with the
        records listed in the language folder.
        Then assembled in order to play.

        In case of failure to play a word, the program
        activates a subroutine that asks for the word
        in the phrase and records new audio to store.
        Add the new word into vocabulary.txt.


    """
    pronunciation_folder = "pronunciation_" + language
    words = []
    with open('vocabulary.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    sentence = input("Enter a sentence: ")
    file_names = []
    for word in sentence.split():
        if word in words and os.path.isfile(os.path.join(pronunciation_folder, word + ".wav")):
            # Pronounce the word
            audio_file = os.path.join(pronunciation_folder, word + ".wav")
            # Cargar la muestra sonora desde un archivo WAV
            sound = AudioSegment.from_wav(audio_file)
            # Duración en milisegundos de la atenuación gradual
            # Aplicar la atenuación gradual al principio y al final de la muestra sonora
            sound = sound.fade_in(100).fade_out(100)
            # Exportar la muestra sonora con la atenuación gradual aplicada
            sound.export("output.wav", format="wav")
            # Play
            playsound("output.wav")
        else:
            try:
                # Pronounce the unknown word using gTTS
                print('Low-Cost TTS failed, switching to gTTS...')
                message = gTTS(text=word, lang=language, slow=False)
                message.save("unknown.wav")
                playsound("unknown.wav")
            except:
                # If gTTS fails, switch to pyTTSx3
                print('gTTS failed, switching to pyTTSx3...')
                engine = pyttsx3.init()
                engine.setProperty('voice', language)
                engine.say(word)
                engine.runAndWait()

    for word in sentence.split():
        if word in words:
            pass
        else:            
            response = input(f"The word '{word}' is not in the pronunciation list. Do you want to record it? (y/n): ")
            # sub-routine to get new word and new sound
            if response.lower() == "y":
                if word not in words:
                    with open("vocabulary.txt", "a") as archivo:
                        archivo.write("\n" + word)
                    words.append(word)
                    audio_file = os.path.join(pronunciation_folder, word + ".wav")

                    # Recording loop
                    # Params
                    fs = 44100  # Sample rate
                    seconds = 1  # Duration of recording
                    is_recording = False
                    silent_frames = 0
                    print("Speak the word:")
                    while True:

                        if not is_recording:
                            is_recording = True

                        if is_recording:
                            silent_frames += 1

                        if is_recording and silent_frames > 10:
                            break

                    # Save audio to file
                    # Record
                    input(f'Press Enter to record, pay attention, is around {seconds} sec.')
                    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                    sd.wait()  # Wait until recording is finished
                    write(audio_file, fs, recording)  # Save as WAV file
                    time.sleep(1)
                    input("Press Enter to continue...")

    print("Pronunciation finished.")


# Main program
def main():
    """ Main.

        Control flow of the program.
        Where is placed the functions,
        procedures and sub-routines
        for sound and text processing.

    """
    while True:
        print("1. Start learning phase")
        print("2. Start pronunciation phase")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            language = input("Enter the language you want to learn: ")
            learning_phase(language)

        elif choice == "2":
            language_folders = [f for f in os.listdir(".") if f.startswith("pronunciation_")]
            if not language_folders:
                print("No language folders found.")
                continue

            print("Existing language folders:")
            for index, folder in enumerate(language_folders):
                print(f"{index + 1}. {folder}")

            folder_choice = input("Enter the number of the folder you want to continue with: ")
            if not folder_choice.isdigit() or int(folder_choice) < 1 or int(folder_choice) > len(language_folders):
                print("Invalid folder choice.")
                continue

            language = language_folders[int(folder_choice) - 1][14:]
            pronunciation_phase(language)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
