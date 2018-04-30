import webbrowser

class Media():
    def __init__(self, title, duration, poster_image, youku_id):
        self.title = title
        self.duration = duration
        self.poster_image_url = poster_image
        self.trailer_youku_url = youku_id

# Class Movie inherited Class Media
class Movie(Media):
    def __init__(self, movie_title, movie_duration, poster_image, youku_id, movie_storyline):
        Media.__init__(self, movie_title, movie_duration, poster_image, youku_id,)
        self.storyline = movie_storyline
