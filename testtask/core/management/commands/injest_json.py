from  django.core.management.base import BaseCommand
from core.ingest_utils.ingest_json import read_json_data, ingest_json_data_db

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)
    def handle(self, *args, **options):
        try:
            import time
            start = time.time()
            df = read_json_data(options['file_path'])
            ingest_json_data_db(df)
            print(df.info())
            print(f"Time taken {time.time() - start}")
        except KeyError:
            raise Exception("Please provide a file path")
