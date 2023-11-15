
from sensor import utils 
from sensor.entity import config_entity, artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self, data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f'Exporting collection data as pandas dataframe')
            df:pd.DataFrame= utils.get_collection_as_dataframe(database_name='aps', collection_name='sensor')
            


        except Exception as e:
            raise SensorException(error_message=e, error_detail=sys)


