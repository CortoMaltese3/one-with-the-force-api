from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Character, Film, Starship


class CharacterViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Populate database with initial test data for Character
        cls.character = Character.objects.create(
            name="Luke Skywalker",
            birth_year="19BBY",
            eye_color="blue",
            gender="male",
            hair_color="blond",
            height="172",
            mass="77",
            skin_color="fair",
            homeworld="https://swapi.dev/api/planets/1/",
            species=[],
            vehicles=[],
            created="2014-12-09T13:50:51.644000Z",
            edited="2014-12-20T21:17:56.891000Z",
            url="https://swapi.dev/api/people/1/",
        )

    def test_list_characters(self):
        url = reverse("character-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_character(self):
        url = reverse("character-list") + "?search=Luke"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Luke Skywalker", [c["name"] for c in response.json()["results"]])

    def test_character_not_found(self):
        url = reverse(
            "character-detail", kwargs={"pk": 999}
        )  # Assume ID 999 does not exist
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_character_data(self):
        url = reverse("character-list")
        invalid_data = {"name": ""}  # Name should not be empty
        response = self.client.post(url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class FilmViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Populate database with initial test data for Film
        cls.film = Film.objects.create(
            title="A New Hope",
            episode_id=4,
            opening_crawl="It is a period of civil war...",
            director="George Lucas",
            producer="Gary Kurtz, Rick McCallum",
            release_date="1977-05-25",
            planets=[],
            species=[],
            vehicles=[],
            created="2014-12-10T14:23:31.880000Z",
            edited="2014-12-20T19:49:45.256000Z",
            url="https://swapi.dev/api/films/1/",
        )

    def test_list_films(self):
        url = reverse("film-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_film(self):
        url = reverse("film-list") + "?search=Hope"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("A New Hope", [f["title"] for f in response.json()["results"]])

    def test_film_not_found(self):
        url = reverse("film-detail", kwargs={"pk": 999})  # Assume ID 999 does not exist
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_film_data(self):
        url = reverse("film-list")
        invalid_data = {"title": ""}  # Title should not be empty
        response = self.client.post(url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class StarshipViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Populate database with initial test data for Starship
        cls.starship = Starship.objects.create(
            name="Death Star",
            model="DS-1 Orbital Battle Station",
            manufacturer="Imperial Department of Military Research, Sienar Fleet Systems",
            cost_in_credits="1000000000000",
            length="120000",
            max_atmosphering_speed="n/a",
            crew="342,953",
            passengers="843,342",
            cargo_capacity="1000000000000",
            consumables="3 years",
            hyperdrive_rating="4.0",
            MGLT="10",
            starship_class="Deep Space Mobile Battlestation",
            created="2014-12-10T16:36:50.509000Z",
            edited="2014-12-10T16:36:50.509000Z",
            url="https://swapi.dev/api/starships/9/",
        )

    def test_list_starships(self):
        url = reverse("starship-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_starship(self):
        url = reverse("starship-list") + "?search=Death"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Death Star", [s["name"] for s in response.json()["results"]])

    def test_starship_not_found(self):
        url = reverse(
            "starship-detail", kwargs={"pk": 999}
        )  # Assume ID 999 does not exist
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_starship_data(self):
        url = reverse("starship-list")
        invalid_data = {"name": ""}  # Name should not be empty
        response = self.client.post(url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
