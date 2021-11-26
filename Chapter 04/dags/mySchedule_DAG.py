import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(12)
    }

with DAG(dag_id="mySchedule_dag", default_args=default_args, 
schedule_interval="@daily") as dag:

    download_sales_data = BashOperator( 
            task_id="download_sales_data",
            bash_command="echo Downlad Data"
        )

    process_sale_data = BashOperator( 
            task_id="process_sales_data",
            bash_command="echo process_data"
        )
    
    download_sales_data >> process_sale_data 
