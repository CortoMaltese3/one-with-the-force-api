from celery import shared_task
from django.core.management import call_command


@shared_task
def fetch_swapi_data_periodically(limit=None):
    call_command("fetch_swapi_data", limit=limit)
