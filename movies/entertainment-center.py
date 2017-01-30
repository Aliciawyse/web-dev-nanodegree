# Use the contents of media.py & fresh_tomatoes files
import fresh_tomatoes
import media

# Create six instances of the class Movie
hidden_figures = media.Movie("Hidden Figures",
                             "Black women working on one of the \
                             greatest missions at NASA",
                             "https://upload.wikimedia.org/wikipedia/en/4/4f/ \
                             The_official_poster_for_the_\
                             film_Hidden_Figures%2C_2016.jpg",
                             "https://www.youtube.com/watch?v=RK8xHq6dfAo")

arrival = media.Movie('Arrival', 'A linguistics expert talks to aliens',
                      'https://upload.wikimedia.org/wikipedia/en/d/df/ \
                       Arrival%2C_Movie_Poster.jpg',
                      'https://www.youtube.com/watch?v=tFMo3UJ4B4g')

robo_cop = media.Movie('Robo Cop', 'A human cop becomes a robot cop',
                       'https://upload.wikimedia.org/wikipedia/en/1/16/ \
                        RoboCop_%281987%29_theatrical_poster.jpg',
                       'https://www.youtube.com/watch?v=FnRJ0r0eivk')

martian = media.Movie('The Martian', 'A man gets left behind on mars.',
                      'https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/\
                      The_Martian_film_poster.jpg/220px-The_\
                      Martian_film_poster.jpg',
                      'https://www.youtube.com/watch?v=tFMo3UJ4B4g')

mummy = media.Movie('The Mummy', 'An ancient egyptian priest is \
                    accidently resurrected',
                    'https://upload.wikimedia.org/wikipedia \
                    /en/thumb/6/68/The_mummy.jpg/220px-The_mummy.jpg',
                    'https://www.youtube.com/watch?v=h3ptPtxWJRs')

fences = media.Movie('Fences', 'A father misses a lifetime of opportunities',
                     'https://upload.wikimedia.org/wikipedia/en/\
                     0/0d/Fences_%28film%29.png',
                     'https://www.youtube.com/watch?v=a2m6Jvp0bUw')

# List of movies
movies = [hidden_figures, arrival, robo_cop, martian, mummy, fences]

# Use list of movies as the arguement to open_movies_page function
fresh_tomatoes.open_movies_page(movies)
