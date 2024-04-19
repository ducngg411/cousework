import re
import customtkinter as ctk  # CustomTkinter for modern GUI components
from PIL import Image, ImageTk

import video_library as lib
import font_manager as fonts

special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

playlist = []
playlist_2 = []
key_history = []

def set_text(text_area, content):
    text_area.delete("1.0", ctk.END)
    text_area.insert(1.0, content)

def icon(path):
    icon_input = Image.open(path)
    icon_resized = icon_input.resize((20, 20), Image.Resampling.BOX )
    icon = ImageTk.PhotoImage(icon_resized)
    return icon

class CreateVideoList():
    def __init__(self, window):
        window.geometry("860x350")
        window.title("Create Video List")
        window.resizable(False, False)
        window.iconbitmap(bitmap='icon packs/windows_media_player_25521.ico') # Set window icon
        

        top_frame = ctk.CTkFrame(window, corner_radius=10)
        top_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        bottom_frame = ctk.CTkFrame(window, corner_radius=10)
        bottom_frame.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        add_videos_btn = ctk.CTkButton(top_frame, text="Add to playlist", command=self.add_playlist_clicked)
        add_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = ctk.CTkLabel(top_frame, text='Enter Video Number')
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = ctk.CTkEntry(top_frame, width=80, placeholder_text="Type here...")
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        play_btn = ctk.CTkButton(top_frame, text='Play Video', hover_color='red' ,fg_color='#1ED760', text_color='black', command=self.play_video_clicked)
        play_btn.grid(row=0, column=3, padx=45, pady=10, sticky='e')

        reset_btn = ctk.CTkButton(top_frame, text='Reset Playlist', hover_color='green' ,fg_color='#FF6347', text_color='white', command=self.reset_playlist_clicked)
        reset_btn.grid(row=0, column=4, padx=0, pady=10)

        self.list_txt = ctk.CTkTextbox(bottom_frame, width=400, height=150)
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) 

        self.video_txt = ctk.CTkTextbox(bottom_frame, width=340, height=120)
        self.video_txt.grid(row=1, column=3, sticky='WNE', columnspan=2, padx=10, pady=10)

        self.status_lbl = ctk.CTkLabel(bottom_frame, text="", font=("Helvetica", 15), text_color='green')
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.status_video = ctk.CTkLabel(bottom_frame, text="", font=("Helvetica", 15))
        self.status_video.grid(row=2, column=3, columnspan=2, padx=20, pady=10)

        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
    
    def add_playlist_clicked(self):
            key = self.input_txt.get()
    # Validation 
            if key =='': # empty input
                error_icon = icon('icon packs/circle-exclamation-solid.png')
                self.status_video.configure(text=f"  Video number cannot be empty!", image = error_icon, compound = 'left', text_color = '#EC131E')

            elif special_char.search(key) != None: # special character 
                error_icon = icon('icon packs/circle-exclamation-solid.png')
                self.status_video.configure(text=f"  Video number cannot be special character!", image = error_icon, compound = 'left', text_color = '#EC131E')

            elif key in key_history: # duplicate input
                error_icon = icon('icon packs/circle-exclamation-solid.png')
                self.status_video.configure(text=f"  Video {key} is already in the playlist.", image = error_icon, compound = 'left', text_color = '#EC131E')
            
            else:
                name = lib.get_name(key)

                if name is not None:
                    director = lib.get_director(key)
                    play_count = lib.get_play_count(key)
                    video_details = f"{name} {director} {play_count}"
                    playlist.append(video_details)
                    key_history.append(key)
                    playlist_str = ""
                    for i, video in enumerate(playlist, start=1):
                        playlist_str += f"{i}. {video}\n"
                    set_text(self.video_txt, playlist_str)
                    success_icon = icon('icon packs\circle-check-solid (3).png')
                    self.status_video.configure(text= f'  Add Video {key} to playlist successfully!', image = success_icon, compound = 'left', text_color = '#63E6BE')

                else:
                    error_icon = icon('icon packs/circle-exclamation-solid.png')
                    self.status_video.configure(text= f'  Video {key} not found!', image = error_icon, compound = 'left', text_color = '#EC131E')

            self.status_lbl.configure(text='Add Playlist Button was clicked!')

    def play_video_clicked(self):
            playlist_2.clear()

            if len(key_history) == 0:
                error_icon = icon('icon packs/circle-exclamation-solid.png')
                self.status_video.configure(text='  Fail ! You must Create a playlist to play Video.', image = error_icon, compound = 'left', text_color = '#EC131E')
            else:
                for i in range(len(key_history)):
                    key = key_history[i]
                    name = lib.get_name(key)
                    director = lib.get_director(key)
                    lib.increment_play_count(key)
                    play_count = lib.get_play_count(key)
                    video_details_2 = f"{name} {director} {play_count}"
                    playlist_2.append(video_details_2)
                    playlist_update = ""
                    for i, video in enumerate(playlist_2, start=1):
                        playlist_update += f"{i} {video}\n"
                    set_text(self.video_txt, playlist_update)
                    success_icon = icon('icon packs\circle-check-solid (3).png')
                    self.status_video.configure(text='  Play Successfully!',image = success_icon, compound = 'left', text_color = '#63E6BE')

            self.status_lbl.configure(text='Play Video Button was clicked!')

    def reset_playlist_clicked(self):
        if len(key_history) == 0:
                error_icon = icon('icon packs/circle-exclamation-solid.png')
                self.status_video.configure(text='  Dont found any Playlist to reset. Try again!', image = error_icon, compound = 'left', text_color = '#EC131E')
        else:
            playlist.clear()
            playlist_2.clear()
            key_history.clear()
            set_text(self.video_txt, playlist)
            success_icon = icon('icon packs\circle-check-solid (3).png')
            self.status_video.configure(text='  Reset successfully!',image = success_icon, compound = 'left', text_color = '#63E6BE')

        self.status_lbl.configure(text='Reset Playlist Button was clicked!')

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = ctk.CTk()        # create a TK object
    fonts.configure()       # configure the fonts
    CreateVideoList(window)     # open the CheckVideo GUI
    window.mainloop() 



