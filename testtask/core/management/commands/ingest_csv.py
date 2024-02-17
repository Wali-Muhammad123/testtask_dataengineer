from django.core.management.base import BaseCommand
from core.ingest_utils.ingest_csv import read_csv_data, ingest_csv_data_db
import pandas as pd
import sqlite3

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)
    def handle(self,*arg, **options):
        try:
            import time
            start = time.time()
            df = read_csv_data(options['file_path'])
            print("Injesting CSV data in the database")
            ingest_csv_data_db(df)
            print(f"Time taken {time.time() - start}")
        except KeyError:
            raise Exception("Please provide a file path")
