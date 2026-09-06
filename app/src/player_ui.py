from utils import tools, ctk_listbox
import customtkinter
import audiodb
from play import Player
from PIL import Image




class PySound(customtkinter.CTk):
    # built-in IMAGE'S
    # --------------------------------------------------------------
    back_img = 'image/interface/image-back.png'
    arrow_right_img = 'image/interface/arrow-right-play.png'
    arrow_left_img = 'image/interface/arrow-left-play.png'
    icon_pause_img = 'image/interface/icon-pause-player.png'
    # --------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.music_running = None
        self.playing_music = False
        self.index_music = 0

        self.title('PySound')
        self.geometry('1000x630')
        self.resizable(False, False)
        self.grid_columnconfigure((0,1,2), weight=0)


    def player_ui(self):
        if tools.exists_path(self.back_img) and (tools.exists_path(self.arrow_right_img)) and tools.exists_path(self.arrow_left_img):
            images_controlls = [
                customtkinter.CTkImage(dark_image=Image.open(self.back_img), size=(600, 400)),
                customtkinter.CTkImage(dark_image=Image.open(self.arrow_right_img), size=(60,60)),
                customtkinter.CTkImage(dark_image=Image.open(self.arrow_left_img), size=(60,60)),
                customtkinter.CTkImage(dark_image=Image.open(self.icon_pause_img), size=(60,60))
            ]
            
            label_back_img = customtkinter.CTkLabel(self, image=images_controlls[0], text='')
            label_back_img.grid(row=0, column=0, padx=0, pady=0)

            self.label_now_playing = customtkinter.CTkLabel(
                self, 
                text="No music playing", 
                font=("Arial", 14, "bold"),
                wraplength=550,
                text_color=('green')
            )
            self.label_now_playing.grid(row=1, column=0, pady=(5, 5))

            button_controlpause = customtkinter.CTkButton(self, image=images_controlls[3], text='', corner_radius=100, width=10, command=self.pause_on)
            button_controlpause.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
            
            button_controlright = customtkinter.CTkButton(self, image=images_controlls[1], command=self.next_on, text='', corner_radius=100, width=285)
            button_controlright.grid(row=3, column=0, padx=10, pady=0, sticky='e')
            
            button_controlleft = customtkinter.CTkButton(self, image=images_controlls[2], command=self.previous_on, text='', corner_radius=100, width=285)
            button_controlleft.grid(row=3, column=0, padx=10, pady=0, sticky='w')


    def playlist_ui(self):
        playlist_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        playlist_frame.grid(row=0, column=1, rowspan=3, padx=70, pady=20, sticky="n")
        title_playlist = customtkinter.CTkLabel(
            playlist_frame, 
            text="Playlist", 
            font=("Arial", 20, "bold")
        )
        title_playlist.pack(anchor="w", pady=(0, 10))

        listbox = ctk_listbox.CTkListbox(playlist_frame, command=self.selected, width=280, height=300)
        listbox.pack()
        for index, music in enumerate(audiodb.name_musics, start=0):
            listbox.insert(index, music)
            

    def pause_on(self):
        print('Pause clicked')
        
        if self.music_running == None:
            self.music_running = audiodb.name_musics[self.index_music]
            name_music = self.music_running
            self.playing_music = True
            music_selected = Player(name_music, fr'..\\audio_files\\{name_music}', self.index_music, self.playing_music)
            music_selected.run_music()
        else:
            name_music = self.music_running
            if self.playing_music:
                self.playing_music = False
                music_selected = Player(name_music, fr'..\\audio_files\\{name_music}', self.index_music, self.playing_music)
                music_selected.pause_music()
            elif not self.playing_music:
                self.playing_music = True
                music_selected = Player(name_music, fr'..\\audio_files\\{name_music}', self.index_music, self.playing_music)
                music_selected.unpause_music()
        self.update_current_track_ui()


    def next_on(self):
        print('Next clicked')
        length_musics = len(audiodb.name_musics)-1
        if self.index_music < length_musics:
            self.index_music += 1
            print(f'Index: {self.index_music}\nMusics index: {length_musics}')
        elif self.index_music == length_musics:
            self.index_music = 0
            print(f'Index: {self.index_music}\nMusics index: {length_musics}')
        # run
        self.music_running = audiodb.name_musics[self.index_music]
        name_music = self.music_running
        self.playing_music = True
        music_selected = Player(name_music, fr'..\\audio_files\\{name_music}', self.index_music, self.playing_music)
        music_selected.run_music()
        self.update_current_track_ui()


    def previous_on(self):
        print('Previous clicked')
        length_musics = len(audiodb.name_musics)-1
        if self.index_music < length_musics:
            self.index_music -= 1
            print(f'Index: {self.index_music}\nMusics index: {length_musics}')
        elif self.index_music == length_musics:
            self.index_music = 0
            print(f'Index: {self.index_music}\nMusics index: {length_musics}')
        # run
        self.music_running = audiodb.name_musics[self.index_music]
        name_music = self.music_running
        self.playing_music = True
        music_selected = Player(name_music, fr'..\\audio_files\\{name_music}', self.index_music, self.playing_music)
        music_selected.run_music()
        self.update_current_track_ui()


    def selected(self, m):
        self.music_running = m
        self.playing_music = True
        music_selected = Player(self.music_running, fr'..\\audio_files\\{self.music_running}', self.index_music, self.playing_music)
        music_selected.run_music()
        self.update_current_track_ui()

    
    def update_current_track_ui(self):
        if self.music_running and hasattr(self, 'label_now_playing'):
            self.label_now_playing.configure(text=f"Playing now: {self.music_running}")