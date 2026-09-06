from pygame import mixer
import audiodb
from utils import tools





class Player:
    mixer.init()
    def __init__(self, name_music, path_file, index, playing):
        self.name_music = name_music
        self.path_file = path_file
        self.index = index
        self.playing = None
    

    def run_music(self):
        # tools.breakln(len(self.name_music)+9)
        # print(f'Playing: {self.name_music}')
        # print(f'From: {self.path_file}')
        # tools.breakln(len(self.name_music)+9)
        # print(f'[ {self.name_music} ] -> Current Music')
        mixer.music.load(self.path_file)
        mixer.music.play()


    def pause_music(self):
        mixer.music.pause()
        tools.breakln(len(self.name_music)+9)
        # print(f'Paused: {self.name_music}')
        tools.breakln(len(self.name_music)+9)
        

    def unpause_music(self):
        mixer.music.unpause()
        tools.breakln(len(self.name_music)+9)
        # print(f'Unpaused: {self.name_music}')
        tools.breakln(len(self.name_music)+9)
