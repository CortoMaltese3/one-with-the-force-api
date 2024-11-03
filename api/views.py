from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import APIException, ValidationError
from .models import Character, Film, Starship
from .serializers import CharacterSerializer, FilmSerializer, StarshipSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Set default page size
    page_size_query_param = "page_size"
    max_page_size = 100


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()  # Reintroduce queryset attribute
    serializer_class = CharacterSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        try:
            return Character.objects.all()
        except Exception as e:
            raise APIException(f"An error occurred while fetching characters: {str(e)}")

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            raise APIException(f"An error occurred while listing characters: {str(e)}")

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Character.DoesNotExist:
            raise APIException("The requested character does not exist.")
        except Exception as e:
            raise APIException(
                f"An error occurred while retrieving the character: {str(e)}"
            )

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            raise ValidationError({"detail": f"Validation error: {str(e)}"})
        except Exception as e:
            raise APIException(
                f"An error occurred while creating the character: {str(e)}"
            )


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()  # Reintroduce queryset attribute
    serializer_class = FilmSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def get_queryset(self):
        try:
            return Film.objects.all()
        except Exception as e:
            raise APIException(f"An error occurred while fetching films: {str(e)}")

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            raise APIException(f"An error occurred while listing films: {str(e)}")

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Film.DoesNotExist:
            raise APIException("The requested film does not exist.")
        except Exception as e:
            raise APIException(f"An error occurred while retrieving the film: {str(e)}")

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            raise ValidationError({"detail": f"Validation error: {str(e)}"})
        except Exception as e:
            raise APIException(f"An error occurred while creating the film: {str(e)}")


class StarshipViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all()  # Reintroduce queryset attribute
    serializer_class = StarshipSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        try:
            return Starship.objects.all()
        except Exception as e:
            raise APIException(f"An error occurred while fetching starships: {str(e)}")

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            raise APIException(f"An error occurred while listing starships: {str(e)}")

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Starship.DoesNotExist:
            raise APIException("The requested starship does not exist.")
        except Exception as e:
            raise APIException(
                f"An error occurred while retrieving the starship: {str(e)}"
            )

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            raise ValidationError({"detail": f"Validation error: {str(e)}"})
        except Exception as e:
            raise APIException(
                f"An error occurred while creating the starship: {str(e)}"
            )
