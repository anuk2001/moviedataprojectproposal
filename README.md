# IMDb Movie Assistant | PYTHON 3, Windows 10
Cinemagoer Docs: https://imdbpy.readthedocs.io/en/latest/

To Install Cinemagoer Package (Command Line): ```pip install git+https://github.com/cinemagoer/cinemagoer```

This github repository is set up for the proposal of a web application to better visualize movie data from IMDb, as well as provide personalized recommendations for movies based on pre-existing movie taste.

This application currently is set up as a proof of concept for the proposal, and only has a few functions to test IMDb implementation through Cinemagoer wrapper API. 

These functions include:
 - getDirector(movieTitle): Function to get directors of a movie
 - getPeopleList(person): Function to get a list of actors/actresses of similar name
 - getTopNMovies(): Get top n movies on IMDb
 - getBottomNMovies(): Get bottom n movies on IMDb
 
 All of these functions call upon the Cinemagoer instance to retrieve data from IMDb.
 
 In order to use the current proposal build: basic knowledge of Python syntax is required. Clone the repository to your desktop or preferred workspace and open with VSCode, or another suitable editor. In the code, call the function with the required parameters, run the code, and view the output.
 
