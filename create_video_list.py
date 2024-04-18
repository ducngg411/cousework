import tkinter as tk
import tkinter.scrolledtext as tkst
import re # regex package



import video_library as lib
import font_manager as fonts

special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

playlist = []
playlist_2 = []
key_history = []

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class CreateVideoList():
    def __init__(self, window):
        window.geometry("850x350")
        window.title("Create Video List")
        window.resizable(False,False)

        add_videos_btn = tk.Button(window, text="Add to playlist", command=self.add_playlist_clicked)
        add_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text='Enter Video Number')
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        play_btn = tk.Button(window, text='Play Video', command=self.play_video_clicked)
        play_btn.grid(row=0, column=3, padx=10, pady=10)

        reset_btn = tk.Button(window, text='Reset Playlist', command=self.reset_playlist_clicked)
        reset_btn.grid(row=0, column=4, padx=10,pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=38, height=12, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky= 'wne', columnspan=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.status_video = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_video.grid(row=2, column=3, columnspan=2, sticky='w', padx=10, pady=10)

        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
    
    def add_playlist_clicked(self):
            key = self.input_txt.get()
    # Validation 
            if key =='': # empty input
                self.status_video.configure(text=f"Video number cannot be empty!")

            elif special_char.search(key) != None: # special character 
                self.status_video.configure(text=f"Video number cannot be special character!")

            elif key in key_history: # duplicate input
                self.status_video.configure(text=f'Video {key} is already in the playlist. Enter a different video!')
            
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
                    self.status_video.configure(text= f'Add Video {key} to playlist successfully!')

                else:
                    self.status_video.configure(text= f'Video {key} not found!')

            self.status_lbl.configure(text='Add Playlist Button was clicked!')

    def play_video_clicked(self):
            playlist_2.clear()

            if len(key_history) == 0:
                self.status_video.configure(text='Fail ! You must Create a playlist to play Video.')
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
                    self.status_video.configure(text='Play Successfully!')

            self.status_lbl.configure(text='Play Video Button was clicked!')

    def reset_playlist_clicked(self):
        if len(key_history) == 0:
                self.status_video.configure(text='Dont found any Playlist to reset. Try again!')
        else:
            playlist.clear()
            playlist_2.clear()
            key_history.clear()
            set_text(self.video_txt, playlist)
            self.status_video.configure(text='Reset successfully!')

        self.status_lbl.configure(text='Reset Playlist Button was clicked!')

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CreateVideoList(window)     # open the CheckVideo GUI
    window.mainloop() 
