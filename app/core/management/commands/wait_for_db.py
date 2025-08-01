import time

from django.core.management.base import BaseCommand
from django.db import connections

from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB Connections ...')
        is_db_connected=None
        while not is_db_connected:
            try:
                is_db_connected=connections['default']
            except(OperationalError, Psycopg2OperationalError):
                self.stdout.write('Retry DB Connections ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Success to PostgreSQL connection'))