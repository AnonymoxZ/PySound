import PySimpleGUI as sg



# settigs window
sg.theme('DarkGray15')
run = True
size_screen = width, height = 362, 459
title = 'PySound'

# path images
icon_win = 'image/icon-window.ico'
icon_left_arrow = sg.Image(filename='image/interface/arrow-left-icon.png',enable_events=True,key='button-next-music')
icon_right_arrow = sg.Image(filename='image/interface/arrow-right-play.png',enable_events=True,key='button-previous-music')
icon_pause = sg.Image('image/interface/icon-pause-player.png',key='button-pause')
img_interface = sg.Image(filename='image/interface/image-back.png')


# main interface layout
def appPlayer():
    player_interface = [[sg.Column([[img_interface]], justification='center')],
    [sg.Column([[icon_left_arrow]], justification='left'),sg.Column([[icon_pause]], justification='center'), sg.Column([[icon_right_arrow]], justification='right')]]
    # Create the Window
    window = sg.Window(title, player_interface,size=size_screen,icon=icon_win)

    # running app
    while run:
        # read eventes and calls
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'button-next-music':
            print('Next clicked!')

    window.close()