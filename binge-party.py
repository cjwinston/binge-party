import requests
import json

def menu():
    #print("Hello! Welcome to Binge-Party!!")
    pass


def getFeatureTitle():
    title = input("What is the full title you looking for? ")
    return title


def switch(featureType):
    switcher = {
        1: 'movie',
        2: 'tv'
    }
    return switcher.get(featureType, "Invalid choice")


def getFeatureType():
    print("Is this a movie or tv show?")
    featureType = switch(int(input("Enter 1 for movie or 2 for tv show: ")))
    return featureType


def getTitleJSONData(api_key, title, featureType):
    titleResponse = requests.get(
                    'https://api.themoviedb.org/3/search/' +
                     featureType +
                    '?api_key='+ api_key + '&query=' + title
                    )
    r = titleResponse.json()
    return r


def getFeatureID(r, featureType):
    if featureType == 'movie':
        for results in r['results']:
            print(results['title'], results['release_date'], "ID:", results['id'])
    else:
        for results in r['results']:
            print(results['name'], "ID:", results['id'])
    resultID = input("Type in the id of the movie/show you're interested in: ")
    return resultID


def getProvJsonData(featureType, resultID, api_key):
    provResponse = requests.get(
                    'https://api.themoviedb.org/3/'
                    + featureType + '/' + resultID
                    + '/watch/providers?api_key=' + api_key
                    )
    pr = provResponse.json()
    return pr


def switch2(buyOption):
    switcher = {
        1: 'flatrate',
        2: 'rent',
        3: 'buy'
    }
    return switcher.get(buyOption, "No listings available for this option.")


def getBuyOption():
    #print('1).Streaming Services\n2).Rent\n3).Buy')
    buyOption = switch2(int(input("Enter 1 for streaming service options, 2 for rent options, or 3 for buy options. ")))
    return buyOption


def printProvResults(pr, buyOption, featureType):
    print("Here are all of the platforms you can find this on: ")
    for results in pr['results']['US'][buyOption]:
        print(results['provider_name'])


def main():
    api_key = '25cd471bedf2ee053df9b1705494367d'
    search = getFeatureTitle()
    typ = getFeatureType()
    resp = getTitleJSONData(api_key, search, typ)
    ID = getFeatureID(resp, typ)
    resp2 = getProvJsonData(typ, ID, api_key)
    buyOp = getBuyOption()
    printProvResults(resp2, buyOp, typ)


if __name__ == "__main__":
    main()