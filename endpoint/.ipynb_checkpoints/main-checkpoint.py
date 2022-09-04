from fastapi import FastAPI
from pydantic import BaseModel
from typing import *

import joblib

import sys
sys.path.append('..') #import module from ../src/
from src.feat_eng import feat_eng_obj, feat_eng_list

app = FastAPI()

'''
load trained model
'''
model = joblib.load('../saved_models/ver1.sav')

'''
create class using BaseModel
'''
class IrisObj(BaseModel):
    ''' 
    allow mutation set to True
    '''
    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.__config__.allow_mutation = True
        
    '''
    prevent mutatition can also be prevent too
    '''
    def build(self):
        self.__config__.allow_mutattion = False
        
    '''
    instance variables
    '''
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    
class IrisList(BaseModel):
    data: List[float]
    
'''
endpoint path(s)
'''
@app.post('/predict_obj/')
def predict_obj(iris: IrisObj) -> List[int]:
    '''
    do feature engineering
    '''
    sepal_area, petal_area = feat_eng_obj(iris)
    
    instance = [iris.sepal_length, iris.sepal_width, 
                                  iris.petal_length, iris.petal_width,
                                  sepal_area, petal_area]
    prediction = model.predict([instance])
    
    '''
    need to convert the result from a numpy array to native array
    '''
    return {'prediction': prediction.tolist()}

@app.post('/predict_list/')
def predict_list(iris: IrisList) -> List[int]:
    '''
    do feature engineering
    '''
    sepal, petal = feat_eng_list(iris)
    instance = iris.data + [sepal] + [petal]
    
    prediction = model.predict([instance])
    
    '''
    need to convert the result from a numpy array to native array
    '''
    return {'prediction': prediction.tolist()}        