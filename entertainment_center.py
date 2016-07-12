import movie
import fresh_tomatoes

# define 4 movies to show on the web page
godfather = movie.Movie('The Godfather', 'When an organized crime boss dies, his son reluctantly takes control of his empire.', 'http://keyartdesigns.com/wp-content/uploads/2010/09/the-godfather-movie-poster-1020243893.jpg', 'https://www.youtube.com/watch?v=w0VGcWHkNeA')

breathless =  movie.Movie('A Bout de Souffle', 'Michel and his American girlfriend try to escape from the police.', 'https://upload.wikimedia.org/wikipedia/en/3/3f/%C3%80_bout_de_souffle_%28movie_poster%29.jpg', 'https://www.youtube.com/watch?v=WCDEAu4R8hA')

space_odyssey = movie.Movie('2001: A Space Odyssey', 'Astronauts, helped by AI named Hal, travel to Jupiter after the discovery of a strange monolith', 'https://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg', 'https://www.youtube.com/watch?v=E8TABIFAN4o')

eight_one_half = movie.Movie('8 1/2', 'A director struggles to complete a film, suffering from a creative block.', 'https://images-na.ssl-images-amazon.com/images/I/51NENWV55VL.jpg', 'https://www.youtube.com/watch?v=PTmiA-uNSD8')

movies = [godfather, breathless, space_odyssey, eight_one_half]

# open web page with the above movie data
fresh_tomatoes.open_movies_page(movies)
