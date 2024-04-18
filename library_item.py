import re # regex package



special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
number_str = re.compile('[123456789]')


class LibraryItem:
    def __init__(self, name, director, rating, img_path, video_path):
        # # Validation for name
        # if name == '':
        #     raise ValueError('Name cannot be empty!')
        
        # if not isinstance(name, str) or number_str.search(name) != None:
        #     raise ValueError('Name must be letters and cannot be numbers!')
        
        # if special_char.search(name) != None:
        #     raise ValueError('Name cannot be special character!')

        # # Validation for director
        # if director == '':
        #     raise ValueError('Director cannot be empty!')
        
        # if not isinstance(director, str) or number_str.search(director) != None:
        #     raise ValueError('Director must be letters and cannot be numbers!')
        
        # if special_char.search(director) != None:
        #     raise ValueError('Director cannot be special character!')
        
        # # Validation for rating
        # if rating < 0:
        #     raise ValueError('Rating cannot be negative!')
        
        # if rating > 5:
        #     raise ValueError('Rating must lower than 6!')


        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0
        self.img_path = img_path
        self.video_path = video_path

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"
        

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
    



