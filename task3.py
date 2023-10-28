import pandas as pd
from sqlalchemy import create_engine
import numpy as np
from config import *

def processing_data(file_path):
    data = pd.read_csv(file_path, sep=';')
    #Rename columns of dataset into standard format
    renamed_columns = {
        'fixed acidity': 'fixed_acidity',
        'volatile acidity': 'volatile_acidity',
        'citric acid': 'citric_acid',
        'residual sugar': 'residual_sugar',
        'chlorides': 'chlorides',
        'free sulfur dioxide': 'free_sulfur_dioxide',
        'total sulfur dioxide': 'total_sulfur_dioxide',
        'density': 'density',
        'pH': 'ph',
        'sulphates': 'sulphates',
        'alcohol': 'alcohol',
        'quality': 'quality'
    }
    data.rename(columns=renamed_columns, inplace=True)
    top_variables = ['volatile_acidity', 'citric_acid', 'chlorides', 'total_sulfur_dioxide', 'density', 'sulphates', 'alcohol', 'quality']
    data = data[top_variables]
    data['quality'] = np.where(data['quality'] > 6, 'High', 'Low')
    return data

def initialize_database(database_name, tabel_schema):
    try:
        connection = get_connection(user, password, host, port)
        engine = create_engine(connection)
        con = engine.connect()
        con.execute("commit")
    
        #Create database named "wine"
        sql = f'CREATE DATABASE {database_name}'
        con.execute(sql)
    
        #Connect to "wine" database
        connection = get_connection(user, password, host, port, database_name)
        engine = create_engine(connection)
        con = engine.connect()
    
        #Create table
        sql = tabel_schema
        con.execute(tabel_schema)
        con.close()    
        print('Initialize database successful!')
    except Exception as e:
        print(f'Error: Initialize database {database_name}')
        print(e)

def transfer_data(databse_name, insert_table_sql, table_name, data):
    connection = get_connection(user, password, host, port, databse_name)
    engine = create_engine(connection)
    con = engine.connect()
    for i, row in data.iterrows():
        try:
            con.execute(insert_table_sql, row)
        except Exception as e:
            print(f"Error: Inserting row for table {table_name}")
            print(e)
    con.close()

def main():
    file_path = 'data/winequality-red.csv'
    database_name = 'wine'
    table_name = 'winequality_red'
    initialize_database(database_name, create_table_sql)
    data = processing_data(file_path)
    transfer_data(database_name, insert_table_sql, table_name, data)