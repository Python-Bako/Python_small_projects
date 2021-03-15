from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name) # it allows me to define a string
                                             # that will represent the object everytime
                                             # it gets printed

    def add_movie(self, name, genre):
        new_movie = Movie(name, genre, False)
        self.movies.append(new_movie)


    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))
        


    def watched_movies(self):
        # calculate a list of movies that have been watched
        # SOLUTION A
        # watched_movies = [] # initialize an empty list
        # for m in self.movies:
        #     if m.watched == True:
        #         watched_movies.append(m)
        #     return(watched_movies)    

        # DO THE SAME USING THE FILTER METHOD
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        # lambda function returns if the parametes it is passed on (x)
        # is true or false
        # we convert it to a list to get the result we want
        return(movies_watched)

