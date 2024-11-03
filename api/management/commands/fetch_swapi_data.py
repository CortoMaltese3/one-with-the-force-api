from django.core.management.base import BaseCommand
import requests
from requests.exceptions import RequestException
from django.db.utils import IntegrityError

from api.models import Character, Film, Starship

BASE_URL = "https://swapi.dev/api/"


def fetch_related_model(model, url_list):
    objects = []
    for url in url_list:
        resource_id = url.split("/")[-2]
        try:
            obj = model.objects.filter(url__endswith=f"/{resource_id}/").first()
            if obj:
                objects.append(obj)
        except Exception as e:
            print(f"Error fetching related model {model.__name__} for URL {url}: {e}")
    return objects


def fetch_all_from_url(url, limit=None):
    data = []
    count = 0
    while url and (limit is None or count < limit):
        try:
            response = requests.get(url)
            response.raise_for_status()
            page_data = response.json()
            results = page_data.get("results", [])

            # Enforce limit
            if limit is not None:
                results = results[: limit - count]
            data.extend(results)
            count += len(results)
            url = page_data.get("next") if (limit is None or count < limit) else None
        except RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            break
        except ValueError as e:
            print(f"Error parsing JSON response from {url}: {e}")
            break
    return data


def fetch_characters(limit=None):
    characters_data = fetch_all_from_url(f"{BASE_URL}people/", limit)
    for character_data in characters_data:
        try:
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
        except IntegrityError as e:
            print(f"Error saving character '{character_data['name']}': {e}")


def fetch_films(limit=None):
    films_data = fetch_all_from_url(f"{BASE_URL}films/", limit)
    for film_data in films_data:
        try:
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
            characters = fetch_related_model(Character, film_data.get("characters", []))
            starships = fetch_related_model(Starship, film_data.get("starships", []))
            film.characters.set(characters)
            film.starships.set(starships)
        except IntegrityError as e:
            print(f"Error saving film '{film_data['title']}': {e}")


def fetch_starships(limit=None):
    starships_data = fetch_all_from_url(f"{BASE_URL}starships/", limit)
    for starship_data in starships_data:
        try:
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
            pilots = fetch_related_model(Character, starship_data.get("pilots", []))
            starship.pilots.set(pilots)
        except IntegrityError as e:
            print(f"Error saving starship '{starship_data['name']}': {e}")


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
        try:
            fetch_characters(limit)
            fetch_films(limit)
            fetch_starships(limit)
            self.stdout.write(
                self.style.SUCCESS("Successfully fetched and stored data from SWAPI")
            )
        except Exception as e:
            self.stderr.write(f"An error occurred: {e}")
