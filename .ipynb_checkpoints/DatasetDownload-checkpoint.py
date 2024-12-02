import json
import os
from kaggle.api.kaggle_api_extended import KaggleApi
with open('../Artifacts/kaggle.json','r') as file:
    data = json.load(file)

os.environ['KAGGLE_USERNAME']=data['username']
os.environ['KAGGLE_KEY']=data['key']

api = KaggleApi()
api.authenticate()

