# api/tests/test_models.py
from django.test import TestCase
from api.models import Character, Film, Starship


class CharacterModelTest(TestCase):
    def setUp(self):
        self.character = Character.objects.create(
            name="Leia Organa",
            birth_year="19BBY",
            eye_color="brown",
            gender="female",
            hair_color="brown",
            height="150",
            mass="49",
            skin_color="light",
            homeworld="https://swapi.dev/api/planets/2/",
            species=[],
            vehicles=[],
            created="2014-12-09T13:50:51.644000Z",
            edited="2014-12-20T21:17:56.891000Z",
            url="https://swapi.dev/api/people/5/",
        )

    def test_character_string_representation(self):
        self.assertEqual(str(self.character), "Leia Organa")


class FilmModelTest(TestCase):
    def setUp(self):
        self.film = Film.objects.create(
            title="The Empire Strikes Back",
            episode_id=5,
            opening_crawl="It is a dark time for the Rebellion...",
            director="Irvin Kershner",
            producer="Gary Kurtz, George Lucas",
            release_date="1980-05-17",
            planets=[],
            species=[],
            vehicles=[],
            created="2014-12-12T11:26:24.656000Z",
            edited="2014-12-20T19:49:45.256000Z",
            url="https://swapi.dev/api/films/2/",
        )

    def test_film_string_representation(self):
        self.assertEqual(str(self.film), "The Empire Strikes Back")


class StarshipModelTest(TestCase):
    def setUp(self):
        self.starship = Starship.objects.create(
            name="X-wing",
            model="T-65 X-wing",
            manufacturer="Incom Corporation",
            cost_in_credits="149999",
            length="12.5",
            max_atmosphering_speed="1050",
            crew="1",
            passengers="0",
            cargo_capacity="110",
            consumables="1 week",
            hyperdrive_rating="1.0",
            MGLT="100",
            starship_class="Starfighter",
            created="2014-12-12T11:19:05.340000Z",
            edited="2014-12-20T21:17:50.309000Z",
            url="https://swapi.dev/api/starships/12/",
        )

    def test_starship_string_representation(self):
        self.assertEqual(str(self.starship), "X-wing")
