import PySimpleGUI as sg
from pygame import mixer
from play import *
import audiodb


# settigs window
sg.theme('DarkGray13')
run = True
size_screen = width, height = 362, 520
title = 'PySound'


# path images
icon_win = 'image/icon-window.ico'
icon_left_arrow = sg.Image(filename='image/interface/arrow-left-play.png',enable_events=True,key='button-previous-music')
icon_right_arrow = sg.Image(filename='image/interface/arrow-right-play.png',enable_events=True,key='button-next-music')
icon_pause = sg.Image('image/interface/icon-pause-player.png',enable_events=True,key='button-play')
img_interface = sg.Image(filename='image/interface/image-back.png')


# main interface layout
def Player():
    # ***********************************************************************************
    player_gui = [[sg.Column([[img_interface]], justification='center')],
    [sg.Column([[icon_left_arrow]], justification='left'),sg.Column([[icon_pause]], justification='center'), sg.Column([[icon_right_arrow]], justification='right')],
    [sg.Button('Cancel playlist',font=10, button_color='red')]]
    
    playlist_gui = [[sg.Listbox([m for m in audiodb.text_musics], size=(50,len(audiodb.files_musics)+10))]]
    
    interface = [[sg.TabGroup([[sg.Tab('Play',player_gui), sg.Tab('Playlist',playlist_gui)]])]]
    
    window = sg.Window(title, interface,size=size_screen,icon=icon_win)
    # ***********************************************************************************

    # data control
    # --------------
    pause_on = None
    # ---------------
    # running app
    while run:
        # player control
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'button-play':
            print(f'Pause On: {pause_on}')
            if pause_on == None:
                run_music()
                pause_on = False

            elif not pause_on:
                pause_music()
                print('Music pause')
                pause_on = True

            elif pause_on:
                despause_music()
                print('Music unpause')
                pause_on = False

        # arrows control
        elif event == 'button-next-music':
            next_music()
            pause_on = False

        elif event == 'button-previous-music':
            previous_music()
            pause_on = False

        # stop control
        elif event == 'Cancel playlist':
            stop_music()
            pause_on = None
    # close
    window.close()
