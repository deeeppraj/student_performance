import os
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

import pandas as pd
import numpy as np


# MODELING:


from sklearn.metrics import mean_squared_error, r2_score , mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree  import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor , AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression , Ridge , Lasso , ElasticNet
from sklearn.model_selection import RandomizedSearchCV , train_test_split
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from src.utils import evaluate_model,save_object


@dataclass
class model_trainer_config:
    trained_model_file_path = os.path.join('artifacts' , 'model_triner.pkl')

class model_trainer:
    def __init__(self):
        self.model_trainer_config = model_trainer_config()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting training and test input data")
            x_train,y_train,x_test,y_test = (train_array[:,:-1] , train_array[:,-1], test_array[:,:-1],test_array[:,-1])

            models = {
                'LinearRegression': LinearRegression(),
                'Ridge': Ridge(),
                'Lasso': Lasso(),
                'ElasticNet': ElasticNet(),
                'KNN': KNeighborsRegressor(),
                'DecisionTree': DecisionTreeRegressor(),
                'Random Forest': RandomForestRegressor(),
                'AdaBoost': AdaBoostRegressor(),
                'Catboost': CatBoostRegressor(verbose=0),
                'XGBoost': XGBRegressor()
            }


            model_report = evaluate_model(x_train=x_train
                                          ,x_test= x_test,
                                          y_train=y_train,
                                          y_test= y_test,
                                          models=models)
            
            best_model_score = max(list(model_report.values()))

            
            best_model_name = next(filter(lambda a: model_report[a] == best_model_score, model_report))
            bm = models[best_model_name]

            if(best_model_score < 0.6):
                raise CustomException("No best model found" , sys)
            
            logging.info("best  model found for training and test data")
            
            save_object(
                file_name= self.model_trainer_config.trained_model_file_path,
                obj=  bm
            )

            predicted = bm.predict(x_test)
            r2 = r2_score(y_test,predicted)
            return r2




        except Exception as e:
            raise CustomException(e,sys)
            

