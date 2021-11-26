import airflow.utils.dates
from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def _download_region_sales_data(**kwargs):
    
    region = kwargs.get('templates_dict', None).get('region', None)
    sales_date = kwargs.get('templates_dict', None).get('region_executing_date', None)


    print(f"Downloaing the {region }sales data for {sales_date}")


default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(2)
    }

with DAG(dag_id="myPython_templ_dict_dag", default_args=default_args, 
schedule_interval=None) as dag:

    download_region_sales_data = PythonOperator( 
            task_id="download_region_sales_data",
            python_callable=_download_region_sales_data,
            templates_dict={"region": "EAST",
                        "region_executing_date": "{{ds}}"
                        },
            provide_context=True
        )
    
    process_sales_data = BashOperator( 
            task_id="process_sales_data",
            bash_command="echo process_data"
        )
    
    download_region_sales_data >> process_sales_data 
