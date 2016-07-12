import webbrowser

class Movie():
	""" This class stores information about a movie """
	
	VALID_RATINGS = ['G', 'PG', 'PG-13', 'R'] #class variable

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title #instance variables
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self): #instance method
		webbrowser.open(self.trailer_youtube_url)