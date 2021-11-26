import airflow.utils.dates
from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

def _download_sales_data():
    print("Downloaing the sales data")

def _download_region_sales_data(region):
    print(f"Downloaing the sales data for {region}")


default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(2)
    }

with DAG(dag_id="myPython1_dag", default_args=default_args, 
schedule_interval=None) as dag:

    download_sales_data = PythonOperator( 
            task_id="download_sales_data",
            python_callable=_download_sales_data
        )

    download_region_sales_data = PythonOperator( 
            task_id="download_region_sales_data",
            python_callable=_download_region_sales_data,
            op_kwargs={'region': 'east'},

        )
    
    process_sales_data = BashOperator( 
            task_id="process_sales_data",
            bash_command="echo process_data"
        )
    
    download_sales_data >> download_region_sales_data >> process_sales_data 
