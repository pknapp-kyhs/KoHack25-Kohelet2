import json
import os
running= True

def countryJewishCommunities():
    global running
    while running == True:
        calgarySelect = input("Input a location:")
        if calgarySelect == "CALGARY":
            print("History: The Majority of the Jews in Calgary come from Russian Origins.")
            print("Traditional Dishes:Borsht and Smoked fish.")
            print("Customs: Generally Ashkenazi,the community custom is to visit the graves of family members before Yom Kippur")
            print("Music: Folk Music")
            print("Language: English")
            print("Chabad:Chabad Lubavitch of Alberta:134, Forge, Rd, SE, Calgary, AB T2H 0S8, Canada,+1(403)-281-3770" )
            running = False
        if calgarySelect == "LITHUANIA":
            print("History: Majority of the Jews come from Germany after WW2")
            print("Traditional Dishes: Berches and Liptauer")
            print("Customs: Ashkenazi customs")
            print("Music: Folk Music")
            print("Language: Lithuanian and Yidish")
            print("Chabad: Chabad Lubavitch of Lithuania, Šv. Kazimiero g. 12, Vilnius, 01126 Lithuania, 370-615-83814")
            running = False
        else:
            print("INVALID: Please choose another location")

def createCountry(country, history, traditionalDishes, customs, music, language, chabad):
    countryStructure = {
        country: {
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

            
# countryJewishCommunities()
# createCountry("Germany", "The jews died", "pasta", "ashkenzi", "pop", "french", "none")