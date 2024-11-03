from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=500)
    episode_id = models.IntegerField(unique=True)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=500)
    producer = models.CharField(max_length=500)
    release_date = models.DateField()

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
    name = models.CharField(max_length=500)
    birth_year = models.CharField(max_length=20)
    eye_color = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    hair_color = models.CharField(max_length=50)
    height = models.CharField(max_length=20)
    mass = models.CharField(max_length=20)
    skin_color = models.CharField(max_length=50)
    homeworld = models.URLField()

    # JSON fields to store lists of URLs
    species = models.JSONField()
    vehicles = models.JSONField()

    # This is a hybrid solution that creates table relationships
    # While keeping the JSON fields in irrelevant fields.
    starships = models.ManyToManyField("Starship", related_name="piloted_by")

    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.name


class Starship(models.Model):
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

    # This is a hybrid solution that creates table relationships
    # While keeping the JSON fields in irrelevant fields.
    pilots = models.ManyToManyField("Character", related_name="piloting_starships")

    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.name
