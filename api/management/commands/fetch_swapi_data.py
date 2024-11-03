from django.core.management.base import BaseCommand
import requests

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


def fetch_all_from_url(url, limit=None):
    data = []
    count = 0
    while url and (limit is None or count < limit):
        response = requests.get(url)
        if response.status_code == 200:
            page_data = response.json()
            results = page_data["results"]
            if limit is not None:
                results = results[
                    : limit - count
                ]  # Limit the results to the remaining count
            data.extend(results)
            count += len(results)
            url = (
                page_data.get("next") if count < limit else None
            )  # Continue if limit not reached
        else:
            break
    return data


def fetch_characters(limit=None):
    characters_data = fetch_all_from_url(f"{BASE_URL}people/", limit)
    for character_data in characters_data:
        Character.objects.update_or_create(
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


def fetch_films(limit=None):
    films_data = fetch_all_from_url(f"{BASE_URL}films/", limit)
    for film_data in films_data:
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
        characters = fetch_related_model(Character, film_data["characters"])
        starships = fetch_related_model(Starship, film_data["starships"])
        film.characters.set(characters)
        film.starships.set(starships)


def fetch_starships(limit=None):
    starships_data = fetch_all_from_url(f"{BASE_URL}starships/", limit)
    for starship_data in starships_data:
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
                "created": starship_data["created"],
                "edited": starship_data["edited"],
                "url": starship_data["url"],
            },
        )
        pilots = fetch_related_model(Character, starship_data["pilots"])
        starship.pilots.set(pilots)


class Command(BaseCommand):
    help = "Fetch and store data from SWAPI"

    def add_arguments(self, parser):
        parser.add_argument(
            "--limit",
            type=int,
            default=None,
            help="Limit the number of items to fetch from each category",
        )

    def handle(self, *args, **options):
        limit = options["limit"]
        fetch_characters(limit)
        fetch_films(limit)
        fetch_starships(limit)
        self.stdout.write(
            self.style.SUCCESS("Successfully fetched and stored data from SWAPI")
        )
