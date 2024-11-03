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
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single character by ID.

        :return: Serialized data of a single Character object.
        """
        obj = get_object_or_404(Character, pk=kwargs["pk"])
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Update a character by ID.

        :return: Updated Character object data.
        """
        obj = get_object_or_404(Character, pk=kwargs["pk"])
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a character by ID.

        :return: HTTP 204 status code upon successful deletion.
        """
        obj = get_object_or_404(Character, pk=kwargs["pk"])
        obj.delete()
        return Response(status=204)

    def create(self, request, *args, **kwargs):
        """
        Create a new character record.

        :raises ValidationError: If the input data is invalid.
        :raises APIException: If an unexpected error occurs.
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

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single film by ID.

        :return: Serialized data of a single Film object.
        """
        obj = get_object_or_404(Film, pk=kwargs["pk"])
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Update a film by ID.

        :return: Updated Film object data.
        """
        obj = get_object_or_404(Film, pk=kwargs["pk"])
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a film by ID.

        :return: HTTP 204 status code upon successful deletion.
        """
        obj = get_object_or_404(Film, pk=kwargs["pk"])
        obj.delete()
        return Response(status=204)

    def create(self, request, *args, **kwargs):
        """
        Create a new film record.

        :raises ValidationError: If the input data is invalid.
        :raises APIException: If an unexpected error occurs.
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

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single starship by ID.

        :return: Serialized data of a single Starship object.
        """
        obj = get_object_or_404(Starship, pk=kwargs["pk"])
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Update a starship by ID.

        :return: Updated Starship object data.
        """
        obj = get_object_or_404(Starship, pk=kwargs["pk"])
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a starship by ID.

        :return: HTTP 204 status code upon successful deletion.
        """
        obj = get_object_or_404(Starship, pk=kwargs["pk"])
        obj.delete()
        return Response(status=204)

    def create(self, request, *args, **kwargs):
        """
        Create a new starship record.

        :raises ValidationError: If the input data is invalid.
        :raises APIException: If an unexpected error occurs.
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
