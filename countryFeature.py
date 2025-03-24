import json
import os

# This function pulls out the history and details of the Jewish communities in the location wanted
def countryJewishCommunities():
   location = input("Input a location:")
   countryResult = findCountry(location) 
   if countryResult is not False:
    print(countryResult)
   else:
    print(f"{location} is an invalind location")
    

# This pulls information from the json file, and returns the country name or false if the country is not in the file
def findCountry(countryName):
    if os.path.getsize("./backroundinfo.json") > 0:
        with open ("./backroundinfo.json", "r") as file:
            data = json.load(file)

    countries_dict = {list(country.keys())[0].lower(): country[list(country.keys())[0]] for country in data}

    if countryName.lower() in countries_dict:
        return countries_dict[countryName.lower()]
    else:
        return False

# This code adds these countries properties into the json a json file
def createCountry(country, history, traditionalDishes, customs, music, language, chabad):
    countryStructure = {
        country.lower(): {
            "history": history,
            "traditionalDishes": traditionalDishes,
            "customs": customs,
            "music": music,
            "language": language,
            "chabad": chabad
        }
    }
    if os.path.getsize("./backroundinfo.json") > 0:
        with open ("./backroundinfo.json", "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(countryStructure)

    with open ("./backroundinfo.json", "w") as file:
        json.dump(data, file, indent=2)

            # This starts the whole feature and asks for a country in order to see the backround info of it
countryJewishCommunities()


# The following are commented out,but this is when we added to the json file
# createCountry("Calgary", "The Majority of the Jews in Calgary come from Russian Origins.", "Borsht and Smoked fish.", "the community custom is to visit the graves of family members before Yom Kippur", "folk music", "English", "Chabad Lubavitch of Alberta:134, Forge, Rd, SE, Calgary, AB T2H 0S8, Canada,+1(403)-281-3770" )
# createCountry("Lithuania","Majority of the Jews come from Germany after WW2", "Berches and Liptauer", "Ashkenazi", "Folk Music","Lithuanian, and Yidish",  "Chabad Lubavitch of Lithuania, Šv. Kazimiero g. 12, Vilnius, 01126 Lithuania, 370-615-83814")

# findCountry("Japan")
# findCountry("CALGARY")