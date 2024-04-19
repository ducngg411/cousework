import customtkinter as ctk
import tkinter.scrolledtext as tkst
import re # regex package


import video_library as lib
import font_manager as fonts
import library_item as li

special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

def set_text(text_area, content):
    text_area.delete("1.0", ctk.END)
    text_area.insert(1.0, content)


class UpdateVideos():
    def __init__(self, window):
        window.geometry("900x400")
        window.title("Update Videos")
        window.resizable(False, False)
        window.iconbitmap(bitmap='icon packs/windows_media_player_25521.ico')

        top_frame = ctk.CTkFrame(window, corner_radius=10)
        top_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        bottom_frame = ctk.CTkFrame(window, corner_radius=10)
        bottom_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        enter_number_lbl = ctk.CTkLabel(top_frame, text='Enter Video Number')
        enter_number_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.number_input = ctk.CTkEntry(top_frame, width=80, placeholder_text="Type here...")
        self.number_input.grid(row=0, column=1, padx=10, pady=10)

        enter_rating_lbl = ctk.CTkLabel(top_frame, text='Enter New Rating')
        enter_rating_lbl.grid(row=0, column=2, padx=10, pady=10)

        self.rating_input = ctk.CTkEntry(top_frame, width=80, placeholder_text="Type here...")
        self.rating_input.grid(row=0, column=3, padx=10, pady=10)

        update_btn = ctk.CTkButton(top_frame, text='Update Video', hover_color='green' ,fg_color='#1ED760', text_color='black',command=self.update_videos_clicked)
        update_btn.grid(row=0, column=4, padx=130, pady=10)

        self.list_txt = ctk.CTkTextbox(bottom_frame, width=450, height=200, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.video_txt = ctk.CTkTextbox(bottom_frame, width=350, height=100, wrap="none")
        self.video_txt.grid(row=1, column=4, sticky= 'wne', padx=10, pady=10)

        self.status_lbl = ctk.CTkLabel(window, text="", font=("Helvetica", 15), text_color='green')
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="n", padx=10, pady=10)

        video_list = lib.list_all()
        set_text(self.list_txt, video_list)

    def update_videos_clicked(self):
        key = self.number_input.get()
        rating_input = self.rating_input.get()

        if key =='':
            set_text(self.video_txt, "Video number cannot be empty!")

        elif special_char.search(key) != None:
            set_text(self.video_txt, "Video number cannot be special character!")

        else:
            name = lib.get_name(key)

            if not rating_input: # Check empty input
                set_text(self.video_txt, 'Rating cannot be empty!')
                return  # End function

            try:
                rating = int(rating_input)  # Try to trans str to int
            except ValueError:
                set_text(self.video_txt, 'Error! Rating must be a number.')
                
            if name is None:
                set_text(self.video_txt, f"Video {key} not found")
            elif rating is None:
                set_text(self.video_txt, f'Rating cannot be empty!')
            elif rating < 0:
                set_text(self.video_txt, f'Rating cannot be negative!')
            elif rating > 5 or rating == 0: 
                set_text(self.video_txt, f'Error! Rating starts 1 - 5.')
            else:
                new_rating = lib.set_rating(key, rating)
                play_count = lib.get_play_count(key)
                video_details = f"{name}\nnew rating:{new_rating}\nplays:{play_count}"
                set_text(self.video_txt, f'Update Successfully!\n{video_details}' )
            
            self.status_lbl.configure(text="Update Video button was clicked!")


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = ctk.CTk()        # create a TK object
    fonts.configure()       # configure the fonts
    UpdateVideos(window)     # open the CheckVideo GUI
    window.mainloop() 