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

# Example usage:
file_path = 'backroundinfo.json'
data_dict = read_json_to_dict(file_path)

#if data_dict:
    #print("JSON data as dictionary:")
    #print(data_dict)


def notify(data):
    #This is when you input your location  
    user_location = input ("Where are you?")
    print ("You are in ", user_location)

    # Once you put in your location this will give you information based on where you are
    for i in data: #looping through list
        for key, value in i.items(): #looping through top dict
            #print (key, value)
            if key == user_location:
                for innerkey, innervalue in i[key].items():
                    #print (innerkey, innervalue)
                    print (f"{innerkey} - {innervalue}")
                repeat=input("try again? y or n")
                if (repeat=="y"):
                    notify(data)
                else:
                    exit()
            
            #else: 
    print("We don't have information on that, try again")
    notify(data)


notify(data_dict)
            

            

