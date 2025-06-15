import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder , OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute  import SimpleImputer

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig :
    preprocessor_obj_file_path = os.path.join('artifacts' , 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        '''
        this  funtion is responsible for returning a function 
        used  for transforming our data set
        by handling missing values using:
            imputer
        by using Standard Scaler ,  OneHotEncodder.
        
        '''
        try:
            num_feat = ['reading score', 'writing score']
            cat_feat = ['gender',
                        'race/ethnicity',
                        'parental level of education',
                        'lunch',
                        'test preparation course']
            
            num_pipeline = Pipeline(
                steps = [
                    ("imputer" , SimpleImputer(strategy='median') ),
                    ("Scaler" , StandardScaler())
                ])
            
            logging.info("numerical columns have been transformed")

            cat_pipeline = Pipeline(
                steps = [
                    ("imputer" , SimpleImputer(strategy='most_frequent')),
                    ("OneHotEncoding", OneHotEncoder(handle_unknown='ignore', sparse_output=False)),
                    ("scaler", StandardScaler(with_mean=False))
                ])
            
            logging.info("categorical columns encodding completed")


            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat_features' ,  cat_pipeline , cat_feat),
                    ("num_features" , num_pipeline , num_feat)
                ]
            )
            
            return preprocessor


        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_transformation(self,train_path,test_path):
        
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            logging.info("read train and test data")
            logging.info("obtaing preprocessing object")
            preprocessor = self.get_data_transformer_obj()
            target_column_name = 'math score'
            num_feat = ['reading score', 'writing score']
            cat_feat = ['gender',
                        'race/ethnicity',
                        'parental level of education',
                        'lunch',
                        'test preparation course']
            input_train_data = train_data.drop(target_column_name , axis=1)
            input_test_data = test_data.drop(target_column_name , axis =1)
            target_feat_train_data = train_data[target_column_name]
            target_feat_test_data = test_data[target_column_name]

            logging.info("Appllying my preprocessing on my train and test dataset")

            input_feature_train_array = preprocessor.fit_transform(input_train_data)
            input_feature_test_array = preprocessor.transform(input_test_data)

            logging.info("Preprocessing done")

            train_array = np.c_[input_feature_train_array , np.array(target_feat_train_data)]
            test_array =  np.c_[input_feature_test_array , np.array(target_feat_test_data)]

            save_object(
                file_name  = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor
            )

            return(
                train_array,test_array,self.data_transformation_config.preprocessor_obj_file_path
            )
        

            




        except Exception as e:
            raise CustomException(e,sys)