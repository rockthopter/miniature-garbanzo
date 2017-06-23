import webbrowser


class Movie():

    """Creates a class which holds a movie's information.

    Args:
        movie_title: The movie's title.
        movie_storyline: Brief summation of the movie's storyline.
        poster_image: Web address of an image of a movie's poster.
        trailer_youtube: Web address of trailer on Youtube.

    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
