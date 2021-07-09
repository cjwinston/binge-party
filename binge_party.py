import requests
import json


def menu():
    print("""
        ***********************************
        * Hello! Welcome to Binge-Party!! *
        ***********************************
        """)


def getFeatureTitle():
    title = input("Enter the name: ")
    return title


def switch(featureType):
    switcher = {
        1: 'movie',
        2: 'tv'
    }
    return switcher.get(featureType, "Invalid choice")


def getFeatureType():
    print("Are you looking for a movie or tv show?")
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
            print(counter, "--", results['title'])
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
            print(counter, "--", results['name'])
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
            print(results['provider_name'], "\n")
    except KeyError:
        if buyOption == 1:
            print('There are no streaming options currently available.\n')
        elif buyOption == 2:
            print('There are no rent options currently available.\n')
        else:
            print('There are no buy options currently available.\n')


def main():
    loop = True
    while(loop):
        menu()
        api_key = '25cd471bedf2ee053df9b1705494367d'
        hasResults = False
        while(not hasResults):
            typ = getFeatureType()
            search = getFeatureTitle()
            resp = getTitleJSONData(api_key, search, typ)
            if resp['total_results'] != 0:
                hasResults = True
            else:
                print("""
There are no results for this title.
Please make sure you entered the title correctly or
choose another movie or show!
                    """)
        ID = getFeatureID(resp, typ)
        resp2 = getProvJsonData(typ, ID, api_key)
        moreOps = 'yes'
        while(moreOps == 'y' or moreOps == 'yes'):
            buyOp = getBuyOption()
            printProvResults(resp2, buyOp, typ)
            print('Would you like to see other provider options?')
            moreOps = input('Enter yes or no: ')
            moreOps.lower()
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
