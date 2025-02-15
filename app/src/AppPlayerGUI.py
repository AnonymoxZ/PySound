import PySimpleGUI as sg
from pygame import mixer

mixer.init()



# settigs window
sg.theme('DarkGray15')
run = True
size_screen = width, height = 362, 520
title = 'PySound'



# path images
icon_win = 'image/icon-window.ico'
icon_left_arrow = sg.Image(filename='image/interface/arrow-left-icon.png',enable_events=True,key='button-next-music')
icon_right_arrow = sg.Image(filename='image/interface/arrow-right-play.png',enable_events=True,key='button-previous-music')
icon_pause = sg.Image('image/interface/icon-pause-player.png',enable_events=True,key='button-play')
img_interface = sg.Image(filename='image/interface/image-back.png')


# main interface layout
def Player():
    # *********************************************************************************** #
    # layout gui
    player_interface = [[sg.Column([[img_interface]], justification='center')],
    [sg.Column([[icon_left_arrow]], justification='left'),sg.Column([[icon_pause]], justification='center'), sg.Column([[icon_right_arrow]], justification='right')],
    [sg.Button('stop music',font=10)]]
    window = sg.Window(title, player_interface,size=size_screen,icon=icon_win)
    # *********************************************************************************** #

    # settings player
    # --------------
    pause_on = None
    # ---------------
    # running app
    while run:
        # player controls
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'button-play':
            if pause_on == None:
                mixer.music.load('audio_files/VØJ_ Narvent Lost Memory Looped to perfection 2 hours long(MP3_160K).mp3')
                mixer.music.play()
                pause_on = False

            elif not pause_on:
                mixer.music.pause()
                pause_on = True

            elif pause_on:
                mixer.music.unpause()
                pause_on = False

        elif event == 'stop music':
            pause_on = None
            mixer.music.unload()

    # close
    mixer.music.unload()
    mixer.quit()
    window.close()
