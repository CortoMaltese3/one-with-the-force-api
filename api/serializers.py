from rest_framework import serializers
from .models import Character, Film, Starship


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = "__all__"
