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


def json_obj(url):
    """Return a json obj"""
    return requests.get(url).json()


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


def clean_person_data(person):
    """Clean data"""
    print("Height : " + person['height'])
    print("Mass: " + person["mass"])
    print("Hair Color: " + person["hair_color"])
    print("Skin Color: " + person["skin_color"])
    print("Eye Color: " + person["eye_color"])
    print("Birth Year: " + person["birth_year"])
    print("Gender: " + person["gender"])
    print("\n")
    print("Movies starred: ")
    for film in person['films']:
        print(json_obj(film)['title'])
        print("\n")
    print("Species: ")
    for species in person["species"]:
        print(json_obj(species)["name"])
        print("\n")
    print("Vehicles: ")
    for vehicle in person["vehicles"]:
        print(json_obj(vehicle)["name"])
        print("\n")
    print("Starships: ")
    for starship in person["starships"]:
        print(json_obj(starship)["name"])


def clean_film_data(movie):
    """Clean Data"""
    print("\nEpisode ID #: " + str(movie["episode_id"]))
    print("Opening Words: " + movie["opening_crawl"])
    print("Director: " + movie["director"])
    print("Producer: " + movie["producer"])
    print("Release Date: " + movie["release_date"])
    print("\n")


def clean_vehicle_data(vehicle):
    """Clean Data"""
    print("Vehicle Name: " + vehicle["name"])
    print("Vehicle Model: " + vehicle["model"])
    print("Manufacturer: " + vehicle["manufacturer"])
    print("Cost in Credits: " + vehicle["cost_in_credits"])
    print("Length: " + vehicle["length"])
    print("Max Speed: " + vehicle["max_atmosphering_speed"])
    print("Crew: " + vehicle["crew"])
    print("Passengers: " + vehicle["passengers"])
    print("Cargo Capacity: " + vehicle["cargo_capacity"])
    print("Consumables: " + vehicle["consumables"])
    print("Vehicle Class: " + vehicle["vehicle_class"])
    print("")
    print("Movies the vehicle appeared in: ")
    for film in vehicle["films"]:
        print(json_obj(film)["title"])


def json_character(key):
    """Grab SW character"""
    response = requests.get("http://swapi.co/api/people/")
    json_response = response.json()
    if key == 'All':
        return json_grab('people', 'name', response, json_response)
    person = data_grab(key, 'people', json_response, 'name')
    print(person)
    return clean_person_data(person)


def json_films(key):
    """Grab SW film"""
    response = requests.get("http://swapi.co/api/films/")
    json_response = response.json()
    if key == 'All':
        print(json_grab('films', 'title', response, json_response))
        return
    movie = data_grab(key, 'films', json_response, 'title')
    print("Top 3 actors")
    for actor in movie.get('characters')[:3]:
        response = requests.get(actor)
        json_response = response.json()
        print(json_response.get('name'))
    return clean_film_data(movie)


def json_vehicles(key):
    """Grab SW vehicle"""
    response = requests.get("http://swapi.co/api/vehicles/")
    json_response = response.json()
    if key == 'All':
        print(json_grab('vehicles', 'name', response, json_response))
        return
    vehicle = data_grab(key, 'vehicles', json_response, 'name')
    return clean_vehicle_data(vehicle)


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
