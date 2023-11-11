import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATAFILE_PATH = '/config/workspace/aps_failure_training_set1.csv'
DATABASE_NAME = 'aps'
COLLECTION_NAME = 'sensor'

if __name__=="__main__":
    df = pd.read_csv(DATAFILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    # Convert dataframe to json to dump the records into mongoDB
    df.reset_index(drop=True, inplace=True)

    json_records = list(json.loads(df.T.to_json()).values())
    print(json_records[0])
    
    #insert converted json into mongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)


