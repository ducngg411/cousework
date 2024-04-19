import customtkinter as ctk
from PIL import Image, ImageTk
from tkVideoPlayer import TkinterVideo

import font_manager as fonts
import watch_later_store

from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideos
from watch_later import WatchLater


ctk.set_appearance_mode("dark")  # Default to dark mode

def icon(path):
    icon_input = Image.open(path)
    icon_resized = icon_input.resize((20, 20), Image.Resampling.BOX)
    icon = ImageTk.PhotoImage(icon_resized)
    return icon


def check_videos_clicked():
    success_icon = icon('icon packs/circle-check-solid (3).png')
    status_lbl.configure(text="  Check Videos button was clicked!", compound='left', text_color='#63E6BE', image=success_icon)
    CheckVideos(ctk.CTkToplevel(window))

def create_video_list():
    success_icon = icon('icon packs/circle-check-solid (3).png')
    status_lbl.configure(text="  Create Video List button was clicked!", compound='left', text_color='#63E6BE', image=success_icon)
    CreateVideoList(ctk.CTkToplevel(window))

def update_videos():
    success_icon = icon('icon packs/circle-check-solid (3).png')
    status_lbl.configure(text="  Update Videos List button was clicked!", compound='left', text_color='#63E6BE', image=success_icon)
    UpdateVideos(ctk.CTkToplevel(window))

def watch_later():
    success_icon = icon('icon packs/circle-check-solid (3).png')
    status_lbl.configure(text="  Watch Later button was clicked!", compound='left', text_color='#63E6BE', image=success_icon)
    WatchLater(ctk.CTkToplevel(window))

def toggle_theme():
    if theme_switch.get() == 0:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

window = ctk.CTk()
window.geometry("680x540")
window.title("Video Player")
window.resizable(False, False)
window.iconbitmap(bitmap='icon packs/windows_media_player_25521.ico')

window.grid_columnconfigure(0, weight=1)  # Column should expand
window.grid_rowconfigure(0, weight=3)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)


top_frame = ctk.CTkFrame(window, corner_radius=10)
top_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nwse")

middle_frame = ctk.CTkFrame(window, corner_radius=10)
middle_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

bottom_frame = ctk.CTkFrame(window, corner_radius=10)
bottom_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

videoplayer = TkinterVideo(master=top_frame, scaled=True)
videoplayer.load('video packs/Hello Intro Screen.mp4')
videoplayer.pack(fill="both", expand=True)
videoplayer.play()

theme_switch = ctk.CTkSwitch(middle_frame, text="Dark Mode", command=toggle_theme, onvalue=0, offvalue=1)
theme_switch.grid(row=0, column=0, padx=10, pady=10, sticky="w")
theme_switch.select()  # Assuming select() toggles it to 'onvalue'

header_lbl = ctk.CTkLabel(middle_frame, text="Select an option by clicking one of the buttons below", compound='left')
header_lbl.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='we')

check_icon = icon('icon packs/circle-check-solid22.png')
check_videos_btn = ctk.CTkButton(bottom_frame, text="Check Videos", command=check_videos_clicked, image=check_icon, compound='left')
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_icon = icon('icon packs/circle-plus-solid (1).png')
create_video_list_btn = ctk.CTkButton(bottom_frame, text="Create Video List", command=create_video_list, image=create_icon, compound='left')
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_icon = icon('icon packs/pen-to-square-solid (1).png')
update_videos_btn = ctk.CTkButton(bottom_frame, text="Update Videos", command=update_videos, image=update_icon, compound='left')
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

watch_later_icon = icon('icon packs\clock-solid.png')
watch_later_btn = ctk.CTkButton(bottom_frame, text="Watch Later", command=watch_later, image=watch_later_icon, compound='left')
watch_later_btn.grid(row=1, column=3, padx=10, pady=10)

status_lbl = ctk.CTkLabel(window, text="", font=("Helvetica", 15))
status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
