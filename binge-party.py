import requests
import json
import plotly.express as px
import pandas as pd

def menu():
    print("""
        ***********************************
        * Hello! Welcome to Binge-Party!! *
        ***********************************
        """)
    pass


def getFeatureTitle():
    title = input("Full name of desired film: ")
    return title


def switch(featureType):
    switcher = {
        1: 'movie',
        2: 'tv'
    }
    return switcher.get(featureType, "Invalid choice")


def getFeatureType():
    print("Is this a movie or tv show?")
    featureType = switch(int(input("""
    **************
    * 1. Movie   *
    * 2. Tv Show *
    **************

Enter a number: """)))
    return featureType


def getTitleJSONData(api_key, title, featureType):
    titleResponse = requests.get(
                    'https://api.themoviedb.org/3/search/'
                    + featureType + '?api_key='
                    + api_key + '&query=' + title
                    )
    r = titleResponse.json()
    return r


def getFeatureID(r, featureType):
    print("""
        *********************
        * TOP RESULTS BELOW *
        *********************
        """)
    if featureType == 'movie':
        for results in r['results']:
            print(results['title'])
            try:
                if results['release_date'] == "":
                    print("     No release date")
                else:
                    print("     Released", results['release_date'])
            except:
                print("     No release date")
            print("     ID:", results['id'])
    else:
        for results in r['results']:
            print(results['name'])
            if results['first_air_date']:
                print("     First Aired:", results['first_air_date'])
            print("     ID:", results['id'])
    resultID = input("Type in the id of the movie/show you're interested in: ")
    return resultID


def getProvJsonData(featureType, resultID, api_key):
    provResponse = requests.get(
                    'https://api.themoviedb.org/3/'
                    + featureType + '/' + resultID
                    + '/watch/providers?api_key=' + api_key
                    )
    re = provResponse.json()
    pr = re['results']
    return pr


def switch2(buyOption):
    switcher = {
        1: 'flatrate',
        2: 'rent',
        3: 'buy'
    }
    return switcher.get(buyOption, "No listings available for this option.")


def getBuyOption():
    buyOption = switch2(int(input("""
    ********************************
    * 1. Streaming service options *
    * 2. Renting options           *
    * 3. Buying options            *
    ********************************

Enter a number: """)))
    return buyOption


def printProvResults(pr, buyOption, featureType):
    print("""
        ****************************
        * FOUND ON PLATFORMS BELOW *
        ****************************
        """)
    for results in pr['US'][buyOption]:
        print(results['provider_name'])
        
def graphing(ID, pr, api_key, typ):
    print('Would you like to see a graph of the available types of providers?')
    graphResponse = input('Enter 1 for yes or 0 for no: ')
    if graphResponse == '1':
        if typ == '1':
            typesProviders = ['Streaming', 'Rent', 'Buy']
            streamingCounter = 0
            for results in pr['US']['flatrate']:
                streamingCounter += 1
            rentCounter = 0
            for results in pr['US']['rent']:
                rentCounter += 1
            buyCounter = 0
            for results in pr['US']['buy']:
                buyCounter += 1
            provCounter = [streamingCounter, rentCounter, buyCounter]
            detailsM = requests.get('https://api.themoviedb.org/3/movie/'
                            + ID +'?api_key=' + api_key + '&language=en-U')
            details = detailsM.json()
            name = deatils['title']
        else:
            typesProviders = ['Streaming', 'Buy']
            streamingCounter = 0
            for results in pr['US']['flatrate']:
                streamingCounter += 1
            buyCounter = 0
            for results in pr['US']['buy']:
                buyCounter += 1
            provCounter = [streamingCounter, buyCounter]
            detailsT = requests.get('https://api.themoviedb.org/3/tv/'
                            + ID +'?api_key=' + api_key + '&language=en-U')
            details = detailsT.json()
            name = details['name']
        fig = px.bar(x=typesProviders, y=provCounter, 
                     color = typesProviders,
                     labels={'x':'Types of Providers', 'y':'Number of Providers'},
                     title = name)
        fig.write_html('figure.html')
        maxVal = max(provCounter)
        index = provCounter.index(maxVal)
        if typesProviders[index] == 'Streaming':
            print('There are more options to stream.')
        elif typesProviders[index] == 'Rent':
            print('There are more options to rent.')
        else:
            print('There are more options to buy.')


def createDataFrame(pr, buyOption):
    buyOpData = pr['US'][buyOption]
    df = pd.DataFrame(buyOpData)
    cols = ['provider_name', 'provider_id', 'display_priority', 'logo_path']
    df = df[cols]
    return df


def main():
    menu()
    api_key = '25cd471bedf2ee053df9b1705494367d'
    search = getFeatureTitle()
    typ = getFeatureType()
    resp = getTitleJSONData(api_key, search, typ)
    ID = getFeatureID(resp, typ)
    resp2 = getProvJsonData(typ, ID, api_key)
    graphing(ID, resp2, api_key, typ)
    buyOp = getBuyOption()
    printProvResults(resp2, buyOp, typ)
    print("""
        ***************************************
        * THANK YOU FOR USING BINGE-PARTY! :) *
        ***************************************
        """)
    df = createDataFrame(resp2, buyOp)
    #print(df)


if __name__ == "__main__":
    main()
