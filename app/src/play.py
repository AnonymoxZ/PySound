from pygame import mixer
import audiodb

mixer.init()
music_playing = 0
musics_list = (len(audiodb.files_musics)-1)


def run_music(name=music_playing):
    print(f'Playing: {audiodb.text_musics[name]}')
    mixer.music.load(audiodb.files_musics[name])
    print(f'\n [ {name} ] -> Current Music \n')
    mixer.music.play()


def next_music():
    global music_playing
    mixer.music.unload()
    print('-'*30)
    if music_playing == musics_list:
        music_playing = 0
    elif music_playing < musics_list:
        music_playing += 1
    # run music
    run_music(name=music_playing)
    print('number music playing: ',music_playing)
    print('-'*30)


def previous_music():
    global music_playing
    mixer.music.unload()
    print('-'*30)
    print('Playlist: ',musics_list)
    if music_playing == 0:
        music_playing = musics_list
    elif music_playing > 0:
        music_playing -= 1
    # run music
    run_music(name=music_playing)
    print('number music playing: ',music_playing)
    print('-'*30)


def pause_music():
    global music_playing
    print(f'Pausing: {audiodb.text_musics[music_playing]}')
    mixer.music.pause()


def despause_music():
    global music_playing
    print(f'Unpausing: {audiodb.text_musics[music_playing]}')
    mixer.music.unpause()


def stop_music():
    global music_playing
    print(f'Canceling: {audiodb.files_musics[music_playing]}')
    mixer.music.stop()
    mixer.music.unload()
    music_playing = 0


