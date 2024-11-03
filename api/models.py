"""
Models for the One With The Force API application.

This module defines Django ORM models that represent various entities in the 
Star Wars universe, including films, characters, and starships.

Classes:
    Film: Represents a Star Wars film with details such as title, episode, 
        director, and related characters and starships.
    Character: Represents a character in the Star Wars universe with attributes 
        like name, gender, and homeworld.
    Starship: Represents a starship with attributes such as model, manufacturer, 
        crew capacity, and associated pilots.

Each model uses Django's ORM to define relationships and fields, 
including JSON fields for related URLs and other resources.
"""

from django.db import models


class Film(models.Model):
    """Represents a film in the Star Wars universe.

    Attributes:
        title (str): The title of the film.
        episode_id (int): The episode number in the series.
        opening_crawl (str): The opening text crawl for the film.
        director (str): The director of the film.
        producer (str): The producer(s) of the film.
        release_date (date): The release date of the film.
        characters (ManyToManyField): Related characters appearing in the film.
        starships (ManyToManyField): Related starships appearing in the film.
        planets (JSONField): List of planets in the film.
        species (JSONField): List of species appearing in the film.
        vehicles (JSONField): List of vehicles appearing in the film.
        created (DateTime): The timestamp of when the film record was created.
        edited (DateTime): The timestamp of the last edit.
        url (URL): The film's URL identifier.
    """

    title = models.CharField(max_length=500)
    episode_id = models.IntegerField(unique=True)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=500)
    producer = models.CharField(max_length=500)
    release_date = models.DateField()
    characters = models.ManyToManyField("Character", related_name="films")
    starships = models.ManyToManyField("Starship", related_name="films")
    planets = models.JSONField()
    species = models.JSONField()
    vehicles = models.JSONField()
    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        """Returns the string representation of the film."""
        return self.title

    class Meta:
        ordering = ["title"]


class Character(models.Model):
    """Represents a character in the Star Wars universe.

    Attributes:
        name (str): The name of the character.
        birth_year (str): The birth year of the character.
        eye_color (str): The character's eye color.
        gender (str): The character's gender.
        hair_color (str): The character's hair color.
        height (str): The character's height.
        mass (str): The character's mass.
        skin_color (str): The character's skin color.
        homeworld (URL): The URL of the character's home planet.
        species (JSONField): List of species the character belongs to.
        vehicles (JSONField): List of vehicles associated with the character.
        starships (ManyToManyField): Related starships piloted by the character.
        created (DateTime): Timestamp when the character record was created.
        edited (DateTime): Timestamp of the last edit.
        url (URL): URL identifier for the character.
    """

    name = models.CharField(max_length=500)
    birth_year = models.CharField(max_length=20)
    eye_color = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    hair_color = models.CharField(max_length=50)
    height = models.CharField(max_length=20)
    mass = models.CharField(max_length=20)
    skin_color = models.CharField(max_length=50)
    homeworld = models.URLField()
    species = models.JSONField()
    vehicles = models.JSONField()
    starships = models.ManyToManyField("Starship", related_name="piloted_by")
    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        """Returns the string representation of the character."""
        return self.name

    class Meta:
        ordering = ["name"]


class Starship(models.Model):
    """Represents a starship in the Star Wars universe.

    Attributes:
        name (str): The name of the starship.
        model (str): The model of the starship.
        manufacturer (str): The manufacturer of the starship.
        cost_in_credits (str): The cost of the starship.
        length (str): The length of the starship.
        max_atmosphering_speed (str): The maximum speed.
        crew (str): The required number of crew members.
        passengers (str): The number of passengers.
        cargo_capacity (str): Cargo capacity.
        consumables (str): Duration starship can provide consumables.
        hyperdrive_rating (str): Hyperdrive rating.
        MGLT (str): Speed in MGLT (megalights per hour).
        starship_class (str): The class of the starship.
        pilots (ManyToManyField): Related characters who pilot the starship.
        created (DateTime): When the starship record was created.
        edited (DateTime): Timestamp of last edit.
        url (URL): URL identifier for the starship.
    """

    name = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    manufacturer = models.CharField(max_length=500)
    cost_in_credits = models.CharField(max_length=50, null=True, blank=True)
    length = models.CharField(max_length=50)
    max_atmosphering_speed = models.CharField(max_length=50)
    crew = models.CharField(max_length=20)
    passengers = models.CharField(max_length=20)
    cargo_capacity = models.CharField(max_length=50)
    consumables = models.CharField(max_length=100)
    hyperdrive_rating = models.CharField(max_length=50)
    MGLT = models.CharField(max_length=50)
    starship_class = models.CharField(max_length=100)
    pilots = models.ManyToManyField("Character", related_name="piloting_starships")
    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        """Returns the string representation of the starship."""
        return self.name

    class Meta:
        ordering = ["name"]
