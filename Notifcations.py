# This holds all the information that will be reported based on your location 
locations = [
    {"name":"Calgary",
     "info": {
     "History-": "The Majority of the Jews in Calgary come from Russian Origins.",
     "Dishes-":"Borsht and Smoked fish.",
     "Customs-": "Generally Ashkenazi,the community custom is to visit the graves of family members before Yom Kippur",
     "Music-": "Folk Music",
     "Language-": "English",
     "Chabad-":"Chabad Lubavitch of Alberta:134, Forge, Rd, SE, Calgary, AB T2H 0S8, Canada,+1(403)-281-3770",
     "Current Events-": "Walk with Israel"}},
    {"name":"Lithuania",
     "info": {
     "History-": "Majority of the Jews come from Germany after WW2",
     "Dishes-":"Berches and Liptauer",
     "Customs-": "Ashkenazi customs",
     "Music-": "Folk Music",
     "Language-": "Lithuanian and Yidish",
     "Chabad-":"Chabad Lubavitch of Lithuania, Šv. Kazimiero g. 12, Vilnius, 01126 Lithuania, 370-615-83814",
     "Current Events-": "Bible Studies at Chabad"}}
    ]

#This is when you input your location  
user_location = input ("Where are you?")
print ("You are in ", user_location)

# Once you put in your location this will give you information based on where you are
for i in locations: #looping through list
    for key, value in i.items(): #looping through top dict
        #print (key, value)
        if key == "name" and value==user_location:
            for innerkey, innervalue in i["info"].items():
                print (innerkey, innervalue)
            exit()
            
        #else: 
print("We don't have information on that, try again")
            

            

