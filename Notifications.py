
import json

def read_json_to_dict(file_path):
    """
    Reads a JSON file and converts it to a Python dictionary.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: A dictionary representing the JSON data, or None if an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return None


# Load our json file and turn it into a dictionary:
file_path = 'backroundinfo.json'
data_dict = read_json_to_dict(file_path)
happening_path = 'Happening.json'
happening_dict = read_json_to_dict(happening_path)

def notify(happenings, data):
    """
    This is meant to notify the user when they enter a new location information on the Jews in that location. 

    Args:
        data (dict): The dictionary created from the JSON file.

    """
    #For the time being we have the user enter their location manually   
    user_location = input ("Where are you?")
    print ("You are in ", user_location)

    #if (user_location == "Lithuania"):
        #print("Happenings-  Community Bible Studies and Purim Party")
    #if (user_location == "Calgary"):
        #print("Happenings- Walk for Israel 3/25/25")
    
    for i in happenings: #looping through list
        for key, value in i.items(): #looping through top dict
            #print (key, value)
            if key == user_location:
                for innerkey, innervalue in i[key].items():
                    #print (innerkey, innervalue)
                    print (f"{innerkey} - {innervalue}")
            

    # Once you put in your location this will give you information based on where you are
    for i in data: #looping through list
        for key, value in i.items(): #looping through top dict
            #print (key, value)
            if key == user_location:
                for innerkey, innervalue in i[key].items(): #looping through inner dictionary
                    #print (innerkey, innervalue)
                    print (f"{innerkey} - {innervalue}")
                repeat=input("try again? y or n")
                if (repeat=="y"):
                    notify(happenings, data) #recursively call the notify function to run it again
                else:
                    exit()
            
            #else: 
    print("We don't have information on that, try again")
    notify(happenings, data) #recursively call the notify function to run it again


notify(happening_dict, data_dict)
            

            

