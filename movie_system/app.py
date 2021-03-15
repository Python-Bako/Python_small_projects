from movie import Movie
from user import User

user_a = User("Nikos")
my_movie = Movie("The Matrix", "Sci-Fi", True)

user_a.movies.append(my_movie)

new_movie = user_a.add_movie("godfather","drama")
user_a.movies.append(new_movie)


