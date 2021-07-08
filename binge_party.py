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


def getFeatureTitle():
    title = input("Full name of desired film or tv show: ")
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
    counter = 1
    dataDict = {}
    if featureType == 'movie':
        for results in r['results']:
            print(counter, ").", results['title'])
            try:
                if results['release_date'] == "":
                    print("     No release date")
                else:
                    print("     Released", results['release_date'])
            except KeyError:
                print("     No release date")
            dataDict[counter] = results['id']
            counter += 1
    else:
        for results in r['results']:
            print(counter, ").", results['name'])
            try:
                if results['first_air_date'] == "":
                    print("     No first air date")
                else:
                    print("     Released", results['first_air_date'])
            except KeyError:
                print("     No first air date date")
            dataDict[counter] = results['id']
            counter += 1
    print("")
    option = input("Enter the number of the movie/show you're interested in: ")
    resultID = dataDict[int(option)]
    return str(resultID)


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
    try:
        for results in pr['US'][buyOption]:
            print(results['provider_name'])
    except KeyError:
        if buyOption == 1:
            print('There are no streaming options currently available.')
        elif buyOption == 2:
            print('There are no rent options currently available.')
        else:
            print('There are no buy options currently available.')


def graphing(ID, pr, api_key, typ):
    print('Would you like to see a graph of the available types of providers?')
    graphResponse = input('Enter 1 for yes or 0 for no: ')
    if graphResponse == '1':
        if typ == 1:
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
                                    + ID + '?api_key='
                                    + api_key + '&language=en-U')
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
                                    + ID + '?api_key='
                                    + api_key + '&language=en-U')
            details = detailsT.json()
            name = details['name']
        fig = px.bar(x=typesProviders, y=provCounter,
                     color=typesProviders,
                     labels={'x': 'Types of Providers',
                             'y': 'Number of Providers'},
                     title=name)
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
    loop = True
    while(loop):
        menu()
        api_key = '25cd471bedf2ee053df9b1705494367d'
        hasResults = False
        while(not hasResults):
            search = getFeatureTitle()
            typ = getFeatureType()
            resp = getTitleJSONData(api_key, search, typ)
            if resp['total_results'] != 0:
                hasResults = True
        ID = getFeatureID(resp, typ)
        resp2 = getProvJsonData(typ, ID, api_key)
        # graphing(ID, resp2, api_key, typ)
        buyOp = getBuyOption()
        printProvResults(resp2, buyOp, typ)
        # df = createDataFrame(resp2, buyOp)
        # print(df)
        print("")
        runAgain = input("Would you like to search for another title(y/n)? ")
        runAgain.lower()
        if(runAgain == 'n' or runAgain == 'no'):
            loop = False

    print("""
            ***************************************
            * THANK YOU FOR USING BINGE-PARTY! :) *
            ***************************************
            """)


if __name__ == "__main__":
    main()
