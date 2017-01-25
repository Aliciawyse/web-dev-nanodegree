#In this file we create the class Movie
import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        #open the web browser stored in trailer_youtube_url
        webbrowser.open(self.trailer_youtube_url)

        
    
