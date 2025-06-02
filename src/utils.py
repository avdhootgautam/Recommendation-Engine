from configparser import ConfigParser
import pandas as pd
import json
def read_config():
    config=ConfigParser()
    config.read('config.ini')
    return config 

def load_dataset(dataset_path):
    df=pd.read_csv(dataset_path)
    return df

def count_null_values(df):
    return df.isnull().sum()

def count_duplicate_values(df):
    return df.duplicated().sum()

def preprocessing_on_a_column_genres(obj):
    l=[]
    for i in json.loads(obj):
        l.append(i["name"])
    return l