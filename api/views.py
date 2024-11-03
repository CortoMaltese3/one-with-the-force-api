"""
ViewSets for the Star Wars API application.

This module provides Django REST framework viewsets to manage and expose data
for Star Wars films, characters, and starships, each with pagination, search, 
and detailed exception handling.

Classes:
    StandardResultsSetPagination: Configures pagination settings for API responses.
    CharacterViewSet: API viewset to manage `Character` resources with custom error handling.
    FilmViewSet: API viewset to manage `Film` resources with custom error handling.
    StarshipViewSet: API viewset to manage `Starship` resources with custom error handling.
"""

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import APIException, ValidationError
from .models import Character, Film, Starship
from .serializers import CharacterSerializer, FilmSerializer, StarshipSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    Configures pagination settings for API responses.

    Attributes:
        page_size (int): Default number of records to display per page.
        page_size_query_param (str): Parameter to customize the page size in requests.
        max_page_size (int): Maximum number of records allowed per page.
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API viewset to manage `Character` resources with custom error handling.

    Attributes:
        queryset (QuerySet): Queryset of all `Character` records.
        serializer_class (Serializer): Serializer class for Character.
        pagination_class (Pagination): Pagination configuration.
        filter_backends (list): List of filter backends to apply.
        search_fields (list): Fields to apply search filters.
    """

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        """
        Fetch all characters with error handling.

        :raises APIException: If an error occurs while fetching characters.
        :return: Queryset of Character objects.
        :rtype: QuerySet
        """
        try:
            return Character.objects.all()
        except Exception as e:
            raise APIException(f"An error occurred while fetching characters: {str(e)}")

    def list(self, request, *args, **kwargs):
        """
        List all characters with pagination.

        :raises APIException: If an error occurs while listing characters.
        :return: Paginated list of Character objects.
        """
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            raise APIException(f"An error occurred while listing characters: {str(e)}")

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single character by ID.

        :raises APIException: If the character does not exist or another error occurs.
        :return: A single Character object.
        """
        try:
            return super().retrieve(request, *args, **kwargs)
        except Character.DoesNotExist:
            raise APIException("The requested character does not exist.")
        except Exception as e:
            raise APIException(
                f"An error occurred while retrieving the character: {str(e)}"
            )

    def create(self, request, *args, **kwargs):
        """
        Create a new character record.

        :raises ValidationError: If the input data is invalid.
        :raises APIException: If another error occurs during creation.
        :return: The created Character object.
        """
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            raise ValidationError({"detail": f"Validation error: {str(e)}"})
        except Exception as e:
            raise APIException(
                f"An error occurred while creating the character: {str(e)}"
            )


class FilmViewSet(viewsets.ModelViewSet):
    """
    API viewset to manage `Film` resources with custom error handling.

    Attributes:
        queryset (QuerySet): Queryset of all `Film` records.
        serializer_class (Serializer): Serializer class for Film.
        pagination_class (Pagination): Pagination configuration.
        filter_backends (list): List of filter backends to apply.
        search_fields (list): Fields to apply search filters.
    """

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def get_queryset(self):
        """
        Fetch all films with error handling.

        :raises APIException: If an error occurs while fetching films.
        :return: Queryset of Film objects.
        :rtype: QuerySet
        """
        try:
            return Film.objects.all()
        except Exception as e:
            raise APIException(f"An error occurred while fetching films: {str(e)}")

    def list(self, request, *args, **kwargs):
        """
        List all films with pagination.

        :raises APIException: If an error occurs while listing films.
        :return: Paginated list of Film objects.
        """
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            raise APIException(f"An error occurred while listing films: {str(e)}")

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single film by ID.

        :raises APIException: If the film does not exist or another error occurs.
        :return: A single Film object.
        """
        try:
            return super().retrieve(request, *args, **kwargs)
        except Film.DoesNotExist:
            raise APIException("The requested film does not exist.")
        except Exception as e:
            raise APIException(f"An error occurred while retrieving the film: {str(e)}")

    def create(self, request, *args, **kwargs):
        """
        Create a new film record.

        :raises ValidationError: If the input data is invalid.
        :raises APIException: If another error occurs during creation.
        :return: The created Film object.
        """
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            raise ValidationError({"detail": f"Validation error: {str(e)}"})
        except Exception as e:
            raise APIException(f"An error occurred while creating the film: {str(e)}")


class StarshipViewSet(viewsets.ModelViewSet):
    """
    API viewset to manage `Starship` resources with custom error handling.

    Attributes:
        queryset (QuerySet): Queryset of all `Starship` records.
        serializer_class (Serializer): Serializer class for Starship.
        pagination_class (Pagination): Pagination configuration.
        filter_backends (list): List of filter backends to apply.
        search_fields (list): Fields to apply search filters.
    """

    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        """
        Fetch all starships with error handling.

        :raises APIException: If an error occurs while fetching starships.
        :return: Queryset of Starship objects.
        :rtype: QuerySet
        """
        try:
            return Starship.objects.all()
        except Exception as e:
            raise APIException(f"An error occurred while fetching starships: {str(e)}")

    def list(self, request, *args, **kwargs):
        """
        List all starships with pagination.

        :raises APIException: If an error occurs while listing starships.
        :return: Paginated list of Starship objects.
        """
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            raise APIException(f"An error occurred while listing starships: {str(e)}")

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single starship by ID.

        :raises APIException: If the starship does not exist or another error occurs.
        :return: A single Starship object.
        """
        try:
            return super().retrieve(request, *args, **kwargs)
        except Starship.DoesNotExist:
            raise APIException("The requested starship does not exist.")
        except Exception as e:
            raise APIException(
                f"An error occurred while retrieving the starship: {str(e)}"
            )

    def create(self, request, *args, **kwargs):
        """
        Create a new starship record.

        :raises ValidationError: If the input data is invalid.
        :raises APIException: If another error occurs during creation.
        :return: The created Starship object.
        """
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            raise ValidationError({"detail": f"Validation error: {str(e)}"})
        except Exception as e:
            raise APIException(
                f"An error occurred while creating the starship: {str(e)}"
            )
