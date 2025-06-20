import os
import sys
from src.exception  import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import model_trainer, model_trainer_config


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts' , 'train.csv')
    test_data_path  : str = os.path.join('artifacts','test.csv')
    raw_data_path  : str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiator(self):
        logging.info("Entered the data ingestion method or component")
        try:
            data = pd.read_csv(r"C:\Users\Deepraj\Desktop\Projects\src\notebook\data\data.csv")
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path , index=False,header=True)
            logging.info("Train Test Spit Initiated")
            train_set , test_set = train_test_split(data,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index = False , header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False , header = True)
            logging.info("Data ingestion complete")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )         
        except Exception as e:
            raise CustomException(e,sys)
        


if __name__ ==  "__main__":
    obj = DataIngestion()
    train,test = obj.initiator()

    data_transform = DataTransformation()
    train_arr,test_arr,_, = data_transform.initiate_transformation(train,test)
    modeltrainer = model_trainer()
    print(modeltrainer.initiate_model_trainer(train_array=train_arr , test_array= test_arr))

