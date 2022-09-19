from imdb import Cinemagoer

# Function to get directors of a movie
def getDirector(movieTitle):
    im = Cinemagoer()
    movie = im.search_movie(movieTitle)
    print('Directors of ' + str(movie[0]) + ': ')
    for director in im.get_movie(movie[0].movieID)['directors']:
        print(director['name'])

# Function to get a list of actors/actresses of similar name
def getPeopleList(person):
    im = Cinemagoer()
    people = im.search_person(person)
    for person in people:
        print(person['name'])

# Get top 10 movies
def getTop10Movies():
    im = Cinemagoer()
    top10 = im.get_top250_movies()
    print('Top 10 Movies on IMDb:')
    for i in range(10):
        print(top10[i])

# Get bottom 10 movies    
def getBottom10Movies():
    im = Cinemagoer()
    bottom10 = im.get_bottom100_movies()
    print('Bottom 10 Movies on IMDb:')
    for i in range(10):
        print(bottom10[i])



