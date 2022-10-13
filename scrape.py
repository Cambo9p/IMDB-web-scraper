"""
this file will scrape the top 250 movies from the IMDB website 

"""

import requests 
from bs4 import BeautifulSoup
from random import *

MOST_POPULAR_URL = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"


def main():

    """scrapes the most popular movies from the internet, gets the top 100"""

    response = requests.get(MOST_POPULAR_URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    title_column = soup.find_all(class_="titleColumn")  # finds the html in the titleColumn class
    movies = [] 

    for i in title_column:
        title = str(i.a)
        movies.append(str(i.a.get_text()))

    # pick a random movie 
    ran = randint(0, len(movies))

    print(movies[ran])

main()
