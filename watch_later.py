import customtkinter as ctk
import tkinter.scrolledtext as tkst
import re # regex package


import video_library as lib
import font_manager as fonts
import library_item as li
import watch_later_store as wls 
from CTkListbox import *

special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

def set_text(text_area, content):
    text_area.delete("1.0", ctk.END)
    text_area.insert(1.0, content)


class WatchLater():
    def __init__(self, window):
        window.geometry("580x400")
        window.title("Update Videos")
        window.resizable(False, False)
        window.iconbitmap(bitmap='icon packs/windows_media_player_25521.ico')

        top_frame = ctk.CTkFrame(window, corner_radius=10)
        top_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        bottom_frame = ctk.CTkFrame(window, corner_radius=10)
        bottom_frame.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        header_lbl = ctk.CTkLabel(top_frame, text="List of videos added to watch later", compound='left')
        header_lbl.grid(row=0, column=0, padx=10, pady=10)

        clear_btn = ctk.CTkButton(top_frame, text="Clear all", hover_color='green' ,fg_color='#1ED760', text_color='black',command=self.clear_all_clicked)
        clear_btn.grid(row=0, column=2, padx=10, pady=10, sticky='e')

        remove_btn = ctk.CTkButton(top_frame, bg_color='transparent', fg_color='transparent', text='')
        remove_btn.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        self.list_txt = CTkListbox(bottom_frame, width=500, height=200)
        self.list_txt.grid(row=1, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.status_lbl = ctk.CTkLabel(window, text="", font=("Helvetica", 15), text_color='green')
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="n", padx=10, pady=10)

        self.index = 0 # Initialize index
        self.load_videos()

        self.index = 0 # Initialize index
        self.load_videos()

    def load_videos(self):
        video_list = wls.get_watch_later_list().split('\n')
        
        for video in video_list:
            if video.strip():
                self.list_txt.insert(self.index, video.strip())
                self.index += 1  # Update index for each video
    
    def clear_all_clicked(self):
        self.list_txt.delete(0, ctk.END)  # Clear all items from the list box
        wls.clear_watch_later_list()  # Clear the storage 

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = ctk.CTk()        # create a TK object
    fonts.configure()       # configure the fonts
    WatchLater(window)     # open the CheckVideo GUI
    window.mainloop() 