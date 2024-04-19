
import re
import customtkinter as ctk  # CustomTkinter for modern GUI components
from PIL import Image, ImageTk
from tkVideoPlayer import TkinterVideo
from CTkListbox import *

import video_library as lib
import font_manager as fonts
import watch_later as wl
import watch_later_store

special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

def set_text(text_area, content):
    text_area.delete("1.0", ctk.END)
    text_area.insert(1.0, content)

def load_image(img_path, width, height):
    try:
        img = Image.open(img_path)
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except IOError:
        print(f"Error opening image file {img_path}. Make sure the path is correct.")
        return None


class CheckVideos:
    def __init__(self, window):
        self.window = window
        window.geometry("640x670")
        window.title("Check Videos")
        window.resizable(False, False)
        window.iconbitmap(bitmap='icon packs/windows_media_player_25521.ico') # Set window icon


        # Using frames to organize layout
        top_frame = ctk.CTkFrame(window, corner_radius=10)
        top_frame.grid(row=0, column=0, padx=30, pady=20, sticky="ew")

        middle_frame = ctk.CTkFrame(window, corner_radius=10)
        middle_frame.grid(row=1, column=0, padx=20, pady=5, sticky="ew") 

        bottom_frame = ctk.CTkFrame(window, corner_radius=10)
        bottom_frame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        list_videos_btn = ctk.CTkButton(top_frame, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = ctk.CTkLabel(top_frame, text="Enter Video Number:")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = ctk.CTkEntry(top_frame, width=80, placeholder_text="Type here...")
        self.input_txt.grid(row=0, column=2, padx=20, pady=10)

        check_video_btn = ctk.CTkButton(top_frame, text="Check Video", hover_color='green' ,fg_color='#1ED760', text_color='black',command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = ctk.CTkTextbox(bottom_frame, width=580, height=200, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=4, sticky="w", padx=10, pady=10)

        self.video_txt = ctk.CTkTextbox(middle_frame, width=300, height=250, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="e", padx=10, pady=10, rowspan = 3)

        self.image_label = ctk.CTkLabel(middle_frame, text='')
        self.image_label.grid(row=1, column=4, padx=10, pady=10)
        
        self.play_button = ctk.CTkButton(middle_frame, bg_color='transparent', fg_color='transparent', text='')
        self.play_button.grid(row=2, column=4, padx=0, pady=10, sticky='w')
        
        self.watch_later = ctk.CTkButton(middle_frame, bg_color='transparent', fg_color='transparent', text='')
        self.watch_later.grid(row=2, column=4, padx=0, pady=10, sticky='e')

        self.status_lbl = ctk.CTkLabel(window, text="", font=("Helvetica", 13), text_color='green')
        self.status_lbl.grid(row=3, column=0, padx=5, pady=5)

    def check_video_clicked(self):
        key = self.input_txt.get()

        if key == '':
            set_text(self.video_txt, "Video number cannot be empty!")
        elif special_char.search(key) is not None:
            set_text(self.video_txt, "Video number cannot be special character!")
        else:
            name = lib.get_name(key)
            if name is not None:
                director = lib.get_director(key)
                rating = lib.get_rating(key)
                play_count = lib.get_play_count(key)
                video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
                
                # show video poster
                img_show = load_image(lib.get_img_path(key), 325, 240)
                self.image_label.configure(image = img_show)
                
                play_button_icon = load_image('icon packs\circle-play-regular (1).png', 30, 30)
                self.play_button.configure(image = play_button_icon, text ='Watch Now', compound='left', hover_color ='green' ,command=lambda:self.show_video_clicked(key))
                
                watch_later_icon = load_image('icon packs\clock-solid.png', 30, 30)
                self.watch_later.configure(image = watch_later_icon, text ='Watch Later', compound='left', hover_color ='green' ,command=lambda:self.watch_later_clicked(key))

                set_text(self.video_txt, video_details)
            else:
                set_text(self.video_txt, f"Video {key} not found")

                # #show 404 not found pic
                img_show = load_image('img packs/404not.jpg')
                self.image_label.configure(image = img_show)

            self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    def show_video_clicked(self, key):
        window_new =ctk.CTkToplevel(self.window)
        window_new.geometry("800x480") # Set width and height for app

        # play video by key
        name = lib.get_name(key)
        lib.increment_play_count(key)
        window_new.title(name) # Set title for app
        video_path = lib.get_video_path(key)
        videoplayer = TkinterVideo(master=window_new, scaled=True)
        videoplayer.load(video_path)
        videoplayer.grid(row=0, column=0, sticky= 'NSEW')

        # set video full window
        window_new.grid_rowconfigure(0, weight=1)
        window_new.grid_columnconfigure(0, weight=1)

        videoplayer.play() # play the video

    def watch_later_clicked(self, key):
        # This should be dynamically obtained based on the current video context
        success = watch_later_store.add_to_watch_later(key)
        if success:
            self.status_lbl.configure(text="Video added to Watch Later", text_color='#63E6BE')
        else:
            self.status_lbl.configure(text="Video already in Watch Later list", text_color='red')

if __name__ == "__main__":
    window = ctk.CTk()
    fonts.configure()
    CheckVideos(window)
    window.mainloop()