import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from watch_later import WatchLater

if __name__ == "__main__":
    window = ctk.CTk()  # create a CTk object
    window.geometry("900x400")
    window.title("Watch Later Videos")
    window.resizable(False, False)
    window.iconbitmap('icon packs/windows_media_player_25521.ico')
    
    app = WatchLater(window)
    window.mainloop()
