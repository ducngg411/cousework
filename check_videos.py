import re # regex package
special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

from tkinter import *
from PIL import Image, ImageTk

from tkVideoPlayer import TkinterVideo

import tkinter as tk # import tkinter library (using for building GUI application) as tk to make more convenient
import tkinter.scrolledtext as tkst #import tkinter scrolled text - module provides the text widget along with a scroll bar

import video_library as lib # Call the Video Library module to use the features it contains
import font_manager as fonts # Call the Font Manager allow apply font family for all code of window


def set_text(text_area, content): # Defines functions set_text to update the content of text area widget. 
    # text area - the location where the content will update
    # content - the content will be displayed for users to see

    text_area.delete("1.0", tk.END) # clear content from beginning "1.0" to the end "tk.End"
    text_area.insert(1.0, content) # insert new content at beginning of text area 


class CheckVideos(): # Defines functions CheckVideos 
    def __init__(self, window):  # constructor __init__ with parameter window to create GUI layout
        self.window = window
        window.geometry("800x480") # Set width and height for app
        window.title("Check Videos") # Set title for app
        window.resizable(False,False)

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked) # Create a button name List All Video 
        # It is linked to event handle : list_videos_clicked. Which will be executed when the button is pressed

        list_videos_btn.grid(row=0, column=0, padx=10, pady=10) # Using grid geometry (uses concepts of rows and columns to arrange the widget) 
        # to set location for button. 

        enter_lbl = tk.Label(window, text="Enter Video Number") # Create a label name Enter Video Number
        enter_lbl.grid(row=0, column=1, padx=10, pady=10) # Set location for label 

        self.input_txt = tk.Entry(window, width=3) # Create a input form, allow user type content from keyboard
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) # Set location for input

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked) # Create a button name Check Video 
        # It is linked to event handle : check_video_clicked. Which will be executed when the button is pressed
        
        check_video_btn.grid(row=0, column=3, padx=10, pady=10) # Set location for button 

        self.list_txt = tkst.ScrolledText(window, width=48, height=18, wrap="none") # Create a screen that display list video with a scroll bar
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) # Set location (columnspan: Merge 3 columns, sticky: West )

        self.video_txt = tk.Text(window, width=33, height=4, wrap="none") # Create a screen that display video info. 
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10) # Set location (Sticky: North West )

        # self.video_txt2 = tk.Text(window, width=27, height=4, wrap="none") # Create a screen that display video info. 
        # self.video_txt2.grid(row=1, column=3, sticky="NW", padx=10, pady=100, rowspan=3) # Set location (Sticky: North West )

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # Create a label to show status when a button clicked 
        self.status_lbl.grid(row=2, column=0,columnspan=4, sticky="WS", padx=10, pady=40) # Set location (columnspan: Merge 4 columns, sticky: West )


        # self.list_videos_clicked()

    def check_video_clicked(self): # Defines check_video_clicked - invoked when Check Video button clicked
        key = self.input_txt.get() # Get input from user 

        # Bonus Validation
        if key =='':
            set_text(self.video_txt, f"Video number cannot be empty!")

        elif special_char.search(key) != None:
            set_text(self.video_txt, f"Video number cannot be special character!")

        else:
            name = lib.get_name(key) # Get list name of video by using lib module
            if name is not None: # Conditions 
                director = lib.get_director(key) # Get director name of videos
                rating = lib.get_rating(key) # Get rating of videos
                play_count = lib.get_play_count(key) # Get play count of videos 
                video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}" # Format director name, rating and play count 
                
                # show video poster
                img_path = lib.get_img_path(key)
                img = Image.open(img_path)
                img_resized = img.resize((300, 245), Image.Resampling.BOX )
                self.img = ImageTk.PhotoImage(img_resized)
                panel = tk.Button(self.window, text='', image= self.img, compound='center', command=lambda:self.show_video_clicked(key))
                panel.grid(row=1, column=3, sticky="NW", padx=10, pady=100, rowspan=3)

                set_text(self.video_txt, video_details) # Show it in video_details 
            else: 
                set_text(self.video_txt, f"Video {key} not found") # Print False notification if conditions FALSE 
                
                #show 404 not found pic
                img = Image.open("img packs/404not.jpg")
                img_resized = img.resize((300, 245), Image.Resampling.BOX )
                self.img = ImageTk.PhotoImage(img_resized)
                panel = tk.Button(self.window, text='', image= self.img, compound='center')
                panel.grid(row=1, column=3, sticky="NW", padx=10, pady=100, rowspan=3)

            self.status_lbl.configure(text="Check Video button was clicked!") # Show button status when it was clicked

    def list_videos_clicked(self): # Defines list_videos_clicked - - invoked when List Video button clicked
        video_list = lib.list_all() # Show all video in library using lib module
        set_text(self.list_txt, video_list) # Show video in video_list screen
        self.status_lbl.configure(text="List Videos button was clicked!") # Status update when button was clicked 

    def show_video_clicked(self, key):
        window_new =tk.Toplevel(self.window)
        window_new.geometry("800x480") # Set width and height for app

        # play video by key
        name = lib.get_name(key)
        window_new.title(name) # Set title for app
        video_path = lib.get_video_path(key)
        videoplayer = TkinterVideo(master=window_new, scaled=True)
        videoplayer.load(video_path)
        videoplayer.grid(row=0, column=0, sticky= 'NSEW')

        # set video full window
        window_new.grid_rowconfigure(0, weight=1)
        window_new.grid_columnconfigure(0, weight=1)

        videoplayer.play() # play the video


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc