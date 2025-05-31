from configparser import ConfigParser
import pandas as pd
def read_config():
    config=ConfigParser()
    config.read('config.ini')
    return config 

def load_dataset(dataset_path):
    df=pd.read_csv(dataset_path)
    return df

def value_counts(df):
    pass