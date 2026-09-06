# playlist musics user
from pathlib import Path


files_musics = []
name_musics = [] # for tab playlist
files = Path('../audio_files')

def removePathName(file:str):
    '''
    :1 -> remove the referencies of path;
    :2 -> name_formated[15:] ignore "..\baudio_files\b" in first char of file name;
    '''
    index = str(file)
    return index[15:]



# visual playlist on the tab "playlist"
for m in files.iterdir():
    music = removePathName(m)
    name_musics.append(music)


# playlist to player
for m in files.iterdir():
    files_musics.append(m)