# python_vlc_piper_tts
## a python and vlc based interface for piper tts
This is only in Hungarian, but you can easily change that by swapping the dataset files.
This little project is made so I can use piper by just double clicking a file and write my text without having to memorize the exact commands.
And I also made it so that it works both on linux and windows

linux users may use speak.py while windows users can use speak_win.py or start.bat
A test.wav file is generated and immediately played as an output. This thing can also be used as a module (not tested tho)

linux users need to have VLC installed for sound to be played immediately. Optionally you can modify the code and make it play differently.


# Additional info about the voice datasets
## Model card for imre and berta (medium)

* Language: hu_HU (Hungarian, Hungary)
* Speakers: 1
* Quality: medium
* Samplerate: 22,050Hz

## Dataset

* URL: https://github.com/NabuCasa/voice-datasets
* License: CC0

## Training

Finetuned from U.S. English lessac voice (medium quality).

# License of VLC (which is embedded here)
VLC is released under the GPLv2 (or later) license. On some platforms, it is de facto GPLv3, because of the licenses of dependencies.

libVLC, the engine is released under the LGPLv2 (or later) license.
This allows embedding the engine in 3rd party applications, while letting them to be licensed under other licenses.
