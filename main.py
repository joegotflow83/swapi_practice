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


def json_grab(obj, item):
    response = requests.get("http://swapi.co/api/{}/".format(obj))
    json_response = response.json()
    for data in range(json_response.get('count') + 1):
        url = "http://swapi.co/api/people/" + "{}/".format(data)
        new_url = requests.get(url)
        json_url = new_url.json()
        print(json_url.get(item))
    return json_response


def json_character(key):
    """Grab SW character"""
    if key == 'All':
        json_response = json_grab('people', 'name')
        return
    for person in range(json_response.get('count') + 1):
        url = "http://swapi.co/api/people/" + "{}/".format(person)
        new_url = requests.get(url)
        json_url = new_url.json()
        if json_url.get('name') == key:
            print('\n {}'.format(json_url.get('name')))
            return json_url
    return 'Not Found'


def json_films(key):
    """Grab SW film"""
    response = requests.get("http://swapi.co/api/films/")
    json_response = response.json()
    if key == 'All':
        for movie in range(json_response.get('count') + 1):
            url = "http://swapi.co/api/films/" + "{}/".format(movie)
            new_url = requests.get(url)
            json_url = new_url.json()
            print(json_url.get('title'))
    for movie in range(json_response.get('count') + 1):
        url = "http://swapi.co/api/films/" + "{}/".format(movie)
        new_url = requests.get(url)
        json_url = new_url.json()
        if json_url.get('title') == key:
            print('\n {}'.format(json_url.get('title')))
            print('\n Top 3 Actors/Actresses: {}')
            for actor in json_url.get('characters')[:3]:
                response = requests.get(actor)
                json_response = response.json()
                print(json_response.get('name'))
            return json_url
    return 'Not Found'


def json_vehicles(key):
    """Grab SW vehicle"""
    response = requests.get("http://swapi.co/api/vehicles/")
    json_response = response.json()
    for vehicle in range(json_response.get('count') + 1):
        url = "http://swapi.co/api/vehicles/" + "{}/".format(vehicle)
        new_url = requests.get(url)
        json_url = new_url.json()
        if json_url.get('name') == key:
            print('\n {}'.format(json_url.get('name')))
            print(json_url)
            return
    return 'Not Found'


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
