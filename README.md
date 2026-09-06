# PySound

PySound is a small desktop music player written in Python. It has a simple graphical interface for browsing the local playlist and controlling playback.

The project is still a prototype, but it is already able to:

- show the music files stored in the local playlist;
- start a selected track;
- pause and resume playback;
- move to the next or previous track;
- display the track that is currently playing.

## Requirements

- Python 3.10 or newer;
- ```pygame-ce==2.5.7```
- ```customtkinter==5.2.2```
- ```pillow==12.2.0```

The current `docs/requiriments.txt` file contains the original dependencies used by the project. The interface also imports `customtkinter` and `Pillow`, so install them before running PySound.

## Installation

Clone or download the project, then create a virtual environment from the project root:

```bat
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```bat
pip install pygame customtkinter Pillow
```

The repository also includes `setup.bat` to activate an existing virtual environment on Windows. It does not create the environment or install packages.

## Running the player

The application uses relative paths for its audio files and interface images. For that reason, run the program from `app/src`:

```bat
cd app\src
python main.py
```

The player window opens with the playlist on the right and the playback controls on the left. Select a song from the playlist or use the controls to start playback.

## Adding music

Copy audio files into:

```text
app/audio_files/
```

PySound currently discovers the files in that folder when it starts. Restart the application after adding or removing tracks. The files should be in a format supported by the installed `pygame` mixer, such as MP3 or WAV.

## Project structure

```text
PySound/
├── app/
│   ├── audio_files/       # Local music files
│   └── src/
│       ├── main.py        # Application entry point
│       ├── player_ui.py   # Window, playlist and controls
│       ├── play.py        # Playback operations
│       ├── audiodb.py     # Builds the playlist from audio_files/
│       ├── image/         # Interface images and application icon
│       └── utils/          # Small helper modules and listbox widget
├── docs/                  # Notes and dependency information
└── setup.bat              # Activates the Windows virtual environment
```


## Screenshots

<img src='/screenshots/PySound_01.png' width=300 height=400>


## Current limitations

PySound is intended for local files and does not include streaming, metadata management, volume controls, or playlist editing yet. The playlist is rebuilt at startup from the contents of `app/audio_files/`.

## License

copyright by AnonymoxZ
