import requests

from api.models import Character

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
