# watch_later_store.py

import re
import customtkinter as ctk  # CustomTkinter for modern GUI components
from PIL import Image, ImageTk
from tkVideoPlayer import TkinterVideo

import video_library as lib
import font_manager as fonts
import watch_later as wl


watch_later_list = []


def add_to_watch_later(video_key):
    if video_key not in watch_later_list:
        watch_later_list.append(video_key)
        return True
    return False

def get_watch_later_list():
    output = ""
    for key in watch_later_list:
        name = lib.get_name(key)
        director = lib.get_director(key)
        play_count = lib.get_play_count(key)
        if name and director and play_count >= 0:
            output += f"Name: {name}, Director: {director}, Play Count: {play_count}\n"
        else:
            output += "Video not found or missing details.\n"
    return output
    


def clear_watch_later_list():
    watch_later_list.clear()
    return watch_later_list

def remove_from_watch_later(video_key):
    if video_key in watch_later_list:
        watch_later_list.remove(video_key)
        return True
    return False