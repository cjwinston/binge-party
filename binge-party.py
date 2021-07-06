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


{'page': 1, 'results': [
    {'adult': False, 
     'backdrop_path': '/k7h4RNAarfOrF2r2YMN0P2FQSr4.jpg', 
     'genre_ids': [80, 18, 53, 28], 
     'id': 75780, 
     'original_language': 
     'en', 'original_title': 
     'Jack Reacher', 'overview': 'When a gunman takes five lives with six shots, all evidence points to the suspect in custody. On interrogation, the suspect offers up a single note: "Get Jack Reacher!" So begins an extraordinary chase for the truth, pitting Jack Reacher against an unexpected enemy, with a skill for violence and a secret to keep.', 
     'popularity': 33.1, 
     'poster_path': '/zlyhKMi2aLk25nOHnNm43MpZMtQ.jpg', 
     'release_date': '2012-12-20', 
     'title': 'Jack Reacher', 
     'video': False, 
     'vote_average': 6.5, 
     'vote_count': 5292
    }, 
    {'adult': False, 
     'backdrop_path': '/ww1eIoywghjoMzRLRIcbJLuKnJH.jpg', 
     'genre_ids': [28], 'id': 343611, 
     'original_language': 'en', 
     'original_title': 'Jack Reacher: Never Go Back', 
     'overview': 'Jack Reacher must uncover the truth behind a major government conspiracy in order to clear his name. On the run as a fugitive from the law, Reacher uncovers a potential secret from his past that could change his life forever.', 'popularity': 42.551, 'poster_path': '/wxLUQ1pIms3HAlVGYvEG9zg2kDs.jpg', 
     'release_date': '2016-10-19', 
     'title': 'Jack Reacher: Never Go Back', 
     'video': False, 
     'vote_average': 5.8, 
     'vote_count': 3631
    }
], 
 'total_pages': 1, 
 'total_results': 2}