from django.core.management.base import BaseCommand
from django.utils import timezone

from api.src.scraper import Scraper


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        Scraper().scrape()
