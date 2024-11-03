from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import CharacterViewSet, FilmViewSet, StarshipViewSet

router = DefaultRouter()
router.register(r"characters", CharacterViewSet)
router.register(r"films", FilmViewSet)
router.register(r"starships", StarshipViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
