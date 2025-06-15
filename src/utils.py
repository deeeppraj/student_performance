import os
import sys
import pandas as pd
import numpy as np
import dill
import sklearn.metrics as m

from src.exception import CustomException

def  save_object(file_name , obj):
    try:
        dir_path =  os.path.dirname(file_name)
        os.makedirs(dir_path , exist_ok=True)
        with open (file_name , "wb") as file:
            dill.dump(obj , file)
    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_model(x_train,x_test,y_train,y_test,models):
    try:
        model = list(models.values())
        model_keys = list(models.keys())
        for i in range(len(model)):
            curr_model = model[i]
            curr_model.fit(x_train,y_train)
            train = curr_model.predict(x_train)
            test = curr_model.predict(x_test)

            train_model_score =  m.r2_score(y_train,train)
            test_model_score = m.r2_score(y_test , test)

            report = {model_keys[i] : test_model_score}

            return report


    except Exception as e:
        raise CustomException(e,sys)