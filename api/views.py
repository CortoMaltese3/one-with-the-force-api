from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Character, Film, Starship
from .serializers import CharacterSerializer, FilmSerializer, StarshipSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Set default page size
    page_size_query_param = "page_size"
    max_page_size = 100


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]


class StarshipViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
