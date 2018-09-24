'''Program to get familiar with fundamentals of Web Scraping using BeautifulSoup library '''

#import the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
from gtabview import view


print("WELCOME ! We fetch 2018's top movies from IMDB")
top_number = int(input("Enter the length of the list ??"))

#defining lists for holding data
names = []
ratings = []
metascores = []
votes = []

#specify the url
url = 'http://www.imdb.com/search/title?release_date=2018&sort=num_votes,desc&page=1'

#Query the website and return the html to the variable 'page'
response = requests.get(url)

#Parse the html in the 'response' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(response.text, 'html.parser')

#Use function prettify to look at nested structure of HTML page and save it in variable
allList = soup.find_all('div', class_ = 'lister-item mode-advanced')

for movies in range(0, top_number):

    #storing data in variables.
    movies = allList[movies]
    mvotes = movies.find('span', attrs = {'name':'nv'})
    mscore = movies.find('span', class_ = 'metascore favorable')
    if mscore is not None:
        movie_mscore = mscore.text

    else:
        movie_mscore = null
    
    #appending into the lists
    names.append(movies.h3.a.text)
    ratings.append(movies.strong.text)
    metascores.append(movie_mscore)
    votes.append(mvotes['data-value'])

#storing all the data in dataframe(table like structure)  
test_df = pd.DataFrame({'movie': names,
                       'imdb': ratings,
                       'metascore': metascores,
                       'votes': votes})

#visualisation of dataframe
view(test_df)
