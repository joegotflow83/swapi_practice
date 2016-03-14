import requests


def begin():
    """Start the app"""
    choice = input("What do you want to look up?\n"
                   "Characters?\n"
                   "Films?\n"
                   "Vehicles\n"
                   "Type the first letter of the word ").lower()
    options = {
        'c': character(),
        'f': films(),
        'v': vehicles()
    }
    return options[choice]


def json_character(key):
    """Grab SW character"""
    response = requests.get("http://swapi.co/api/people/")
    json_response = response.json()
    if key == 'All':
        for person in range(json_response.get('count') + 1):
            url = "http://swapi.co/api/people/" + "{}/".format(person)
            new_url = requests.get(url)
            json_url = new_url.json()
            print(json_url.get('name'))
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
    num = 1
    for film in range(json_response.get('count')):
        print(num)


def character():
    """Allow a user to search for characters"""
    person = input("Who do you want to search for?\n"
                   "Type all for almost everyone ").title()
    character = json_character(person)
    print('\n {}'.format(character))
    return character


def films():
    pass


def vehicles():
    pass


begin()
