from user import User
from movie import Movie


user = User("Nikos")

user.add_movie("Matrix", "Sci-Fi")
user.add_movie("The dictator", "Comedy")


# Ideally, the following will create a file with the user name and the respective movies
#user.save_to_file()
user.load_from_file()