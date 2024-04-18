from library_item import LibraryItem


library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4, 'img packs/tomandjerry.jpg', 'video packs/video01.mp4')
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5,'img packs/breakfast.jpg', 'video packs/video02.mp4')
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2, 'img packs/Casablanca.jpg', 'video packs/video03.mp4')
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1,'img packs/Sound_of_music.jpg', 'video packs/video04.mp4')
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3, 'img packs/Gone With the wind.jpg','video packs/video05.mp4')


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
        return rating # KO CO RETURN
    except KeyError:
        return -11


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
        return item
    except KeyError:
        return -1

def get_img_path(key):
    try:
        item = library[key]
        return item.img_path
    except KeyError:
        return -1
    
def get_video_path(key):
    try:
        item = library[key]
        return item.video_path
    except KeyError:
        return -1
    

list_all()