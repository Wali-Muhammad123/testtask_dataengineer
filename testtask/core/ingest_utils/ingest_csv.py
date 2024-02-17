from numpy import float16, int32
from pandas import read_csv
from pandas import DataFrame
from core.models import POI
from pandas.core.arrays.integer import Int32Dtype


def read_csv_data(file_path: str) -> DataFrame | None:
    """
    Read data from a csv file
    """
    try:
        df = read_csv(file_path,encoding='utf-8', dtype={'poi_id':int32,
                                                        'poi_name':str,
                                                        'poi_category':str,
                                                        'poi_latitude':float16,
                                                        'poi_longitude':float16,
                                                        'poi_rating':str,})
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df['poi_ratings'] = df['poi_ratings'].str.strip('{}').str.split(',').apply(lambda x: sum(map(float, x)) / len(x))
        print(df.head())
        return df
    except Exception as e:
        print(e)
        pass

def ingest_csv_data_db(df: DataFrame):
    """
    Ingest data into the database
    """
    try:
        objects_list = []
        for index, row in df.iterrows():
            poi = POI(
                internal_id=row['poi_id'],
                name=row['poi_name'],
                category=row['poi_category'],
                latitude=row['poi_latitude'],
                longitude=row['poi_longitude'],
                average_rating=row['poi_ratings']
            )
            objects_list.append(poi)
        POI.objects.bulk_create(objects_list)
        print("Successfully ingested data into the database")
    except Exception as e:
        print(e)
        pass
