# -*- coding: UTF-8 -*-

# define basic class Media, it represents the basic variables need be used for
# a media for the project.
# Attributes:
#   title(str): to show the media title
#   duration(str): the duration of trailer for a media
#   poster_image(str): the URL of poster for this media
#   youku_id(str): the trailer video id in www.youku.com


class Media():
    def __init__(self, title, duration, poster_image, youku_id):
        self.title = title
        self.duration = duration
        self.poster_image_url = poster_image
        self.trailer_youku_url = youku_id


# Class Movie inherited Class Media, to identify the movie object
# Attributes:
#   movie_title(str): the name of the movie
#   movie_duration(str): he duration of trailer for a movie
#   poster_image(str): the movie poster url
#   youku_id(str): the trailer video id in www.youku.com
#   movie_storyline()str: a summary of a movie story
class Movie(Media):
    def __init__(self, movie_title, movie_duration, poster_image, youku_id,
                 movie_storyline):
        Media.__init__(self, movie_title, movie_duration,
                       poster_image, youku_id,)
        self.storyline = movie_storyline
