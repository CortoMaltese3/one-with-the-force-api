"""
Django admin configuration for the Star Wars API application.
Registers models and configures list display, search fields, and filters.
"""

from django.contrib import admin
from .models import Film, Character, Starship


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """Admin panel configuration for the Film model."""

    list_display = ("title", "episode_id", "release_date", "director")
    search_fields = ("title", "director", "producer")
    list_filter = ("release_date", "director")


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "birth_year", "homeworld")
    search_fields = ("name", "gender", "eye_color")
    list_filter = ("gender", "eye_color", "hair_color")


@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "manufacturer", "starship_class")
    search_fields = ("name", "model", "manufacturer")
    list_filter = ("manufacturer", "starship_class")
