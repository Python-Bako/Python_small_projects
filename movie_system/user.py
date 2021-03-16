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


    # save a user to a file as a csv format

    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write(movie.name + "," + movie.genre + "," + str(movie.watched) + "\n")


    # Bako's version to load and read line by line the file
    # def load_from_file(self):
    #     with open("{}.txt".format(self.name),'r') as f:
    #         line = f.readline()
    #         cnt = 1
    #         while line:
    #             print("Line {}: {}".format(cnt, line.strip()))
    #             line = f.readline()
    #             cnt += 1

    # Another version -- one more oop oriented
    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1]: # this is where the written movies lie (start)
                movie_data = line.split(',') # ['name', 'genre', 'watched']
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True" ))
            
            user = User(username)
            user.movies = movies

            return user

