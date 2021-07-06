import requests
import json

# Ex API request: https://api.themoviedb.org/3/movie/550?api_key=25cd471bedf2ee053df9b1705494367d
# menu
"""
print("Hello! Welcome to Binge-Party!!")
userInput = input('Enter the name of a movie or tv show: ')
"""

api_key = '25cd471bedf2ee053df9b1705494367d'

response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=' + api_key + '&query=Jack+Reacher')
print(response.json())

# https://api.themoviedb.org/3/search/multi?api_key=<<api_key>>&language=en-US&query=%27lalalalalalalalal%27&page=1&include_adult=false
