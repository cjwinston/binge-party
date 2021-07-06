import requests
import json

# menu

print("Hello! Welcome to Binge-Party!!")
title = input("What is the full title you looking for? ")


def switch(featureType):
    switcher = {
        1: 'movie',
        2: 'tv'
    }
    return switcher.get(featureType, "Invalid choice")


print("Is this a movie or tv show?")
featureType = switch(int(input("Enter 1 for movie or 2 for tv show: ")))
api_key = '25cd471bedf2ee053df9b1705494367d'

titleResponse = requests.get(
                'https://api.themoviedb.org/3/search/movie?api_key='
                + api_key + '&query=' + title
                )
# print(titleResponse.json())

r = titleResponse.json()

for results in r['results']:
    print(results['title'], results['release_date'], "ID:", results['id'])
resultID = input("Type in the id of the movie/show you're interested in: ")

provResponse = requests.get(
                'https://api.themoviedb.org/3/'
                + featureType + '/' + resultID
                + '/watch/providers?api_key=' + api_key)
# print(provResponse.json())
# pr = provResponse.json()
# for res in pr['results']:
# print(res['provider_name'])
