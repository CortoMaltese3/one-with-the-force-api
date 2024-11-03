import requests
from django.core.management.base import BaseCommand
from api.models import Character, Film, Starship

BASE_URL = "https://swapi.dev/api/"


# Fetch related resource function
def fetch_related_model(model, url_list):
    objects = []
    for url in url_list:
        resource_id = url.split("/")[-2]
        obj = model.objects.filter(url__endswith=f"/{resource_id}/").first()
        if obj:
            objects.append(obj)
    return objects


def fetch_characters():
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


def fetch_films():
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
                    "planets": film_data["planets"],
                    "species": film_data["species"],
                    "vehicles": film_data["vehicles"],
                    "created": film_data["created"],
                    "edited": film_data["edited"],
                    "url": film_data["url"],
                },
            )
            # Set character and starship many-to-many fields after creation
            characters = fetch_related_model(Character, film_data["characters"])
            starships = fetch_related_model(Starship, film_data["starships"])
            film.characters.set(characters)
            film.starships.set(starships)


def fetch_starships():
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
            # Set pilot many-to-many field after creation
            pilots = fetch_related_model(Character, starship_data["pilots"])
            starship.pilots.set(pilots)


class Command(BaseCommand):
    help = "Fetch and store data from SWAPI"

    def handle(self, *args, **kwargs):
        fetch_characters()
        fetch_films()
        fetch_starships()
        self.stdout.write(
            self.style.SUCCESS("Successfully fetched and stored data from SWAPI")
        )
