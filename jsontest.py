import json
import datetime

# def search_birthday():
#     # look in the database if the birthday exists and return the birthday if found
#     name = input("Whose birthday are you looking for?")
#
#     # open the json file
#     database = load_database()
#
#     # look for the name as a key in the dictionary
#     if name in database.keys():
#         # if found return the date
#         print("we found "+name+'\'s birthday, it is',database[name])
#     else:
#         # if not return an error
#         print("no birthday found for", name)


def write_birthday(name):
    # writing to the database
    # # input a name
    # name = input("please enter your name")

    # input a date
    date_string  = input("please enter your birthday, format is dd/mm/yyyy")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y")

    database = load_database()

    # add to the json file
    with open("database.json",'w') as f:
        database[name] = date_string
        json.dump(database,f)

    print('thank you,'+name+'\'s birthday was added to the database.', date_string,'is a great birthday.')


def load_database():
    with open('database.json','r') as d:
        database = json.load(d)
    return database


while True:
    # ask the user if they want to search for a birthday or add a new one
    name = input("please enter a name:")

    if not name:
        break

    database = load_database()
    if name in database:
        print("we found " + name + '\'s birthday, it is', database[name])
    else:
        write_birthday(name)


# json.load(f) #loads from a file previously opened
# json.loads(s) #loads from a string
# json.dump(obj, f) #wite obj to file
# json.dumps(obj) #returns a string from obj