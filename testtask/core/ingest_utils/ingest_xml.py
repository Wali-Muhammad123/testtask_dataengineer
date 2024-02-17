import pandas as pd
from core.models import POI

def read_xml_data(filepath: str) -> pd.DataFrame | None:
    """
    Read data from a json file
    """
    try:
        df = pd.read_xml(filepath)
        df['pratings'] = df['pratings'].apply(lambda x: [int(i) for i in x.split(',')])
        df['avg_ratings'] = df['pratings'].apply(lambda x: sum(x) / len(x) if x else 0)
        df = df.drop(columns=['pratings'])
        return df
    except Exception as e:
        print(e)
        pass

def injest_xml_data_db(df: pd.DataFrame):
    """
    Ingest data into the database
    """
    try:
        objects_list = []
        for index, row in df.iterrows():
            poi = POI(
                internal_id=row['pid'],
                name=row['pname'],
                category=row['pcategory'],
                latitude=row['platitude'],
                longitude=row['plongitude'],
                average_rating=row['avg_ratings']
            )
            objects_list.append(poi)
        POI.objects.bulk_create(objects_list)
        print("Successfully ingested data into the database")
    except Exception as e:
        print(e)
        pass
