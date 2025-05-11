# playlist musics user
from pathlib import Path


files_musics = []
text_musics = [] # for tab playlist
files = Path('../audio_files')

def removePathName(index:str):
    '''
    :1 -> remove the referencies of path;
    :2 -> name_formated[1:] ignore "\" in first char of file name;
    '''
    index = str(index)
    name_formated = index.replace('..\\audio_files','')
    return name_formated[1:]


# visual playlist on the tab "playlist"
for m in files.iterdir():
    music = removePathName(m)
    text_musics.append(music)

# playlist to player
for m in files.iterdir():
    files_musics.append(m)
