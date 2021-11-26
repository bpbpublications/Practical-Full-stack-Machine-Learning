import airflow.utils.dates
from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator import DummyOperator

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="myFile_Sensor_dag", default_args=default_args, 
schedule_interval="@daily", catchup = False) as dag:


# for supermarket_id in [1, 2, 3, 4]:
#     wait = FileSensor(
#         task_id=f"wait_for_supermarket_{supermarket_id}",
#         filepath=f"/data/supermarket{supermarket_id}/data.csv",
#         dag=dag,
#     )

    wait = FileSensor(
        task_id="wait_for_Sales_Data",
        filepath="/usr/local/airflow/data/sales_data/sales_data_east.csv"        
        )
    clean_data = DummyOperator(task_id="clean_data")
    process_data = DummyOperator(task_id="process_data")

    wait >> clean_data >> process_data
