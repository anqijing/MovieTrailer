import webbrowser


class Movie():
    # creats memory for instance
    def __init__(self, title, movie_storyline, poster_imge, trailer_youtube):
        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_imge
        self.trailer_youtube_url = trailer_youtube

    # show movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
