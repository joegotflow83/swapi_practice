import requests


def begin():
    """Start the app"""
    choice = input("What do you want to look up?\n"
                   "Characters?\n"
                   "Films?\n"
                   "Vehicles\n"
                   "Type the first letter of the word ").lower()
    if choice == 'c':
        return character()
    elif choice == 'f':
        return films()
    elif choice == 'v':
        return vehicles()


def json_grab(obj, item, response, json_response):
    """display all data in a given category"""
    for data in range(json_response.get('count') + 1):
        url = "http://swapi.co/api/{}/".format(obj) + "{}/".format(data)
        new_url = requests.get(url)
        json_url = new_url.json()
        print(json_url.get(item))
    return


def data_grab(key, obj, json_response, item):
    """Display specific data the user asks for"""
    for data in range(json_response.get('count') + 1):
        url = "http://swapi.co/api/{}/".format(obj) + "{}/".format(data)
        new_url = requests.get(url)
        json_url = new_url.json()
        if json_url.get(item) == key:
            print('\n{}'.format(json_url.get(item)))
            return json_url
    return 'Not Found'


def json_character(key):
    """Grab SW character"""
    response = requests.get("http://swapi.co/api/people/")
    json_response = response.json()
    if key == 'All':
        print(json_grab('people', 'name', response, json_response))
        return
    return data_grab(key, 'people', json_response, 'name')


def json_films(key):
    """Grab SW film"""
    response = requests.get("http://swapi.co/api/films/")
    json_response = response.json()
    if key == 'All':
        print(json_grab('films', 'title', response, json_response))
        return
    movie = data_grab(key, 'films', json_response, 'title')
    for actor in movie.get('characters')[:3]:
        response = requests.get(actor)
        json_response = response.json()
        print(json_response.get('name'))
    return movie


def json_vehicles(key):
    """Grab SW vehicle"""
    response = requests.get("http://swapi.co/api/vehicles/")
    json_response = response.json()
    if key == 'All':
        print(json_grab('vehicles', 'name', response, json_response))
        return
    return data_grab(key, 'vehicles', json_response, 'name')


def character():
    """Allow a user to search for characters"""
    person = input("Who do you want to search for?\n"
                   "Type all for everyone ").title()
    character = json_character(person)
    print('\n {}'.format(character))
    return character


def films():
    """Allow a user to search for films"""
    movie = input("Which movie do you want to search for?\n"
                  "Type all for all movies ").title()
    film = json_films(movie)
    print('\n {}'.format(film))
    return film


def vehicles():
    """Allow a user to search for vehicles"""
    vehicle = input("Which vehicle do you want to search for?\n").title()
    user_pick = json_vehicles(vehicle)
    print('\n {}'.format(user_pick))
    return user_pick


begin()
