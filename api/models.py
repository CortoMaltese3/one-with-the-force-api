from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=255)
    episode_id = models.IntegerField(unique=True)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    release_date = models.DateField()

    # Direct relationships with Character and Starship models
    # This is a hybrid solution that creates table relationships
    # While keeping the JSON fields in irrelevant fields.
    characters = models.ManyToManyField("Character", related_name="films")
    starships = models.ManyToManyField("Starship", related_name="films")

    # JSON fields to store lists of URLs for other related resources
    planets = models.JSONField()
    species = models.JSONField()
    vehicles = models.JSONField()

    # Additional metadata
    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.CharField(max_length=10)
    eye_color = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=20)
    height = models.CharField(max_length=10)
    mass = models.CharField(max_length=10)
    skin_color = models.CharField(max_length=20)
    homeworld = models.URLField()

    # JSON fields to store lists of URLs
    species = models.JSONField()
    vehicles = models.JSONField()

    # Direct relationships with Starship model
    # This is a hybrid solution that creates table relationships
    # While keeping the JSON fields in irrelevant fields.
    starships = models.ManyToManyField("Starship", related_name="piloted_by")

    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.name


class Starship(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    cost_in_credits = models.CharField(max_length=20, null=True, blank=True)
    length = models.CharField(max_length=20)
    max_atmosphering_speed = models.CharField(max_length=20)
    crew = models.CharField(max_length=10)
    passengers = models.CharField(max_length=10)
    cargo_capacity = models.CharField(max_length=20)
    consumables = models.CharField(max_length=50)
    hyperdrive_rating = models.CharField(max_length=10)
    MGLT = models.CharField(max_length=10)
    starship_class = models.CharField(max_length=50)

    # JSON field for list of pilot URLs (if additional external data required)
    pilots = models.JSONField()

    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.name
