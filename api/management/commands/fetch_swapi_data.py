import requests

from api.models import Character, Film, Starship

BASE_URL = "https://swapi.dev/api/"


def fetch_and_save_characters():
    """Fetches character data from SWAPI and saves it to the Character model."""
    response = requests.get(f"{BASE_URL}people/")
    if response.status_code == 200:
        data = response.json()
        for character_data in data["results"]:
            character, created = Character.objects.update_or_create(
                name=character_data["name"],
                defaults={
                    "birth_year": character_data["birth_year"],
                    "eye_color": character_data["eye_color"],
                    "gender": character_data["gender"],
                    "hair_color": character_data["hair_color"],
                    "height": character_data["height"],
                    "mass": character_data["mass"],
                    "skin_color": character_data["skin_color"],
                    "homeworld": character_data["homeworld"],
                    "species": character_data["species"],
                    "vehicles": character_data["vehicles"],
                    "created": character_data["created"],
                    "edited": character_data["edited"],
                    "url": character_data["url"],
                },
            )


def fetch_and_save_films():
    """Fetches film data from SWAPI and saves it to the Film model."""
    response = requests.get(f"{BASE_URL}films/")
    if response.status_code == 200:
        data = response.json()
        for film_data in data["results"]:
            film, created = Film.objects.update_or_create(
                title=film_data["title"],
                defaults={
                    "episode_id": film_data["episode_id"],
                    "opening_crawl": film_data["opening_crawl"],
                    "director": film_data["director"],
                    "producer": film_data["producer"],
                    "release_date": film_data["release_date"],
                    "characters": film_data["characters"],
                    "planets": film_data["planets"],
                    "starships": film_data["starships"],
                    "vehicles": film_data["vehicles"],
                    "species": film_data["species"],
                    "created": film_data["created"],
                    "edited": film_data["edited"],
                    "url": film_data["url"],
                },
            )


def fetch_and_save_starships():
    """Fetches starship data from SWAPI and saves it to the Starship model."""
    response = requests.get(f"{BASE_URL}starships/")
    if response.status_code == 200:
        data = response.json()
        for starship_data in data["results"]:
            starship, created = Starship.objects.update_or_create(
                name=starship_data["name"],
                defaults={
                    "model": starship_data["model"],
                    "manufacturer": starship_data["manufacturer"],
                    "cost_in_credits": starship_data["cost_in_credits"],
                    "length": starship_data["length"],
                    "max_atmosphering_speed": starship_data["max_atmosphering_speed"],
                    "crew": starship_data["crew"],
                    "passengers": starship_data["passengers"],
                    "cargo_capacity": starship_data["cargo_capacity"],
                    "consumables": starship_data["consumables"],
                    "hyperdrive_rating": starship_data["hyperdrive_rating"],
                    "MGLT": starship_data["MGLT"],
                    "starship_class": starship_data["starship_class"],
                    "pilots": starship_data["pilots"],
                    "created": starship_data["created"],
                    "edited": starship_data["edited"],
                    "url": starship_data["url"],
                },
            )
