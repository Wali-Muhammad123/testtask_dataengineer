from  django.core.management.base import BaseCommand
from core.ingest_utils.ingest_xml import read_xml_data, injest_xml_data_db


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)
    def handle(self,*args,**options):
        try:
            import time
            start = time.time()
            df = read_xml_data(options['file_path'])
            print("Injesting XML data into the DB")
            injest_xml_data_db(df)
            print(f"Time taken {time.time() - start}")
        except KeyError:
            raise Exception("Please provide a file path")
