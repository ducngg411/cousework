import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

def setup_context_menu(window):
    context_menu = tk.Menu(window, tearoff=0)
    context_menu.add_command(label="Play Video", command=play_video)
    context_menu.add_command(label="Remove Video", command=remove_video)
    return context_menu

def on_right_click(event, context_menu):
    try:
        # Đặt vị trí hiển thị menu
        context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()

def play_video():
    messagebox.showinfo("Action", "Play Video action triggered")

def remove_video():
    messagebox.showinfo("Action", "Remove Video action triggered")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("680x540")
        self.title("Video Player Context Menu Example")
        self.configure(bg="gray17")

        self.listbox = ctk.CTkTextbox(self, width=450, height=300, wrap="none")
        self.listbox.pack(pady=20, padx=20)
        self.listbox.insert("end", "Video 1\nVideo 2\nVideo 3\nVideo 4")

        # Thiết lập menu ngữ cảnh
        self.context_menu = setup_context_menu(self)
        self.listbox.bind("<Button-3>", lambda event: on_right_click(event, self.context_menu))

if __name__ == "__main__":
    app = App()
    app.mainloop()
