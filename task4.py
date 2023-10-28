from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
from datetime import datetime
from config import *

def transfer_data(databse_name, table_name):
    try:
        connection = get_connection(user, password, host, port, databse_name)
        engine = create_engine(connection)
        data = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
        data_values = data.values.tolist()
        data_columns = data.columns.tolist()
        client = get_client(ch_host, ch_port, ch_username, ch_password)
        client.insert(table_name, data_values, column_names=data_columns)
        print('Transfer data sucessful')
    except Exception as e:
        print(f'Error: Transfer data to table {table_name}')
        print(str(e))
        
new_dag = DAG(
    dag_id = 'update_winequality',
    start_date=datetime(2023, 10, 24),
    schedule_interval='@hourly'
)

python_task = PythonOperator(
    task_id='python_update_winequality',
    python_callable=transfer_data,
    op_kwargs = {'databse_name':'wine', 'table_name':'winequality_red'},
    dag=new_dag
)