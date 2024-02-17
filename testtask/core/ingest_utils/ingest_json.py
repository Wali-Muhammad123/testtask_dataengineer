import pandas as pd
from core.models import POI

def read_json_data(file_path: str) -> pd.DataFrame | None:
    """
    Read data from a json file
    """
    try:
        df = pd.read_json(file_path, encoding='utf-8')
        print(df.head())
        df['pois_latitude'] = df['coordinates'].map(lambda x: x['latitude'])
        df['pois_longitude'] = df['coordinates'].map(lambda x: x['longitude'])
        df['ratings'] = df['ratings'].map(lambda x: sum(x) / len(x) if x else 0)
        df = df.drop(columns=['coordinates'])
        return df
    except Exception as e:
        print(e)
        pass

def ingest_json_data_db(df: pd.DataFrame):
    """
    Ingest data into the database
    """
    try:
        objects_list = []
        for index, row in df.iterrows():
            poi = POI(
                internal_id=row['id'],
                name=row['name'],
                category=row['category'],
                latitude=row['pois_latitude'],
                longitude=row['pois_longitude'],
                average_rating=row['ratings']
            )
            objects_list.append(poi)
        POI.objects.bulk_create(objects_list)
        print("Successfully ingested data into the database")
    except Exception as e:
        print(e)
        pass
