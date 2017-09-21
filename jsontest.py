import json
import datetime


def write_birthday(name):
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


def get_same_age(name):
    import math
    database = load_database()
    date = datetime.datetime.strptime(database[name], "%d/%m/%Y")
    now = datetime.datetime.now()
    age =math.floor((now - date).days/365.2425)

    for k,v in database.items():
        date = datetime.datetime.strptime(database[k], "%d/%m/%Y")
        if math.floor((now - date).days/365.2425) == age:
            print('{} as the same age as {}, {} years!' .format(k,name, age))


while True:
    # ask the user if they want to search for a birthday or add a new one
    name = input("please enter a name:")

    if not name:
        break

    database = load_database()
    if name in database:
        print("we found " + name + '\'s birthday, it is', database[name])
        if input('do you want to see if there are more people with the same age?') == 'y':
            get_same_age(name)

    else:
        if input('we didnt find that name in the database, do you want to add it?') == 'y':
            write_birthday(name)



# json.load(f) #loads from a file previously opened
# json.loads(s) #loads from a string
# json.dump(obj, f) #wite obj to file
# json.dumps(obj) #returns a string from obj