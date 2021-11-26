import os
import airflow.utils.dates
from airflow import DAG
from airflow.contrib.sensors.python_sensor import PythonSensor
from airflow.operators.dummy_operator import DummyOperator

def _wait_for_file(region):
    file_path = "/usr/local/airflow/data/sales_data/sales_data_" + region + ".csv"
    isFile = os.path.isfile(file_path)
    return isFile

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="myPython_Sensor_dag", default_args=default_args, 
schedule_interval="@daily", catchup = False) as dag:

    wait = PythonSensor(
        task_id="wait_for_Sales_Data",
        python_callable=_wait_for_file,
        op_kwargs={'region': 'east'},        
        )
    clean_data = DummyOperator(task_id="clean_data")
    process_data = DummyOperator(task_id="process_data")

    wait >> clean_data >> process_data
