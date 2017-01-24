#Use the contents of media.py file. It is good practice to define class in seperate file
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ" )
#print(avatar.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ" )

hidden_figures = media.Movie("Hidden Figures", "African American women working on one of the greatest missions at NASA", "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg","https://www.youtube.com/watch?v=RK8xHq6dfAo")
#print(hidden_figures.storyline)
#hidden_figures.show_trailer()

arrival = media.Movie('Arrival', 'A linguistics expert talks to aliens', 'https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg', 'https://www.youtube.com/watch?v=tFMo3UJ4B4g')

robo_cop = media.Movie('Robo Cop', 'A human cop becomes a robot cop', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/16/RoboCop_%281987%29_theatrical_poster.jpg/220px-RoboCop_%281987%29_theatrical_poster.jpg', 'https://www.youtube.com/watch?v=FnRJ0r0eivk')

martian = media.Movie('The Martian', 'A man gets left behind on mars.', 'https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg', 'https://www.youtube.com/watch?v=tFMo3UJ4B4g')

mummy = media.Movie('The Mummy', 'An ancient egyptian priest is accidently resurrected', 'https://upload.wikimedia.org/wikipedia/en/thumb/6/68/The_mummy.jpg/220px-The_mummy.jpg', 'https://www.youtube.com/watch?v=h3ptPtxWJRs')


#print(avatar.storyline)
#avatar.show_trailer()
#print arrival.storyline

movies = [toy_story, avatar,hidden_figures, arrival, robo_cop, martian, mummy]
fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS
