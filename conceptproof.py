from imdb import Cinemagoer

# Function to get directors of a movie
def getDirector(movieTitle):
    im = Cinemagoer()
    movie = im.search_movie(movieTitle)
    print('Directors of ' + str(movie[0]) + ': ')
    for director in im.get_movie(movie[0].movieID)['directors']:
        print(director['name'])

