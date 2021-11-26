import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(12)
    }

with DAG(dag_id="myFirst_dag", default_args=default_args, 
max_active_runs=2, schedule_interval="@daily", catchup = True) as dag:

    t1 = BashOperator( 
            task_id="t1",
            bash_command="echo Hello"
        )

    t2 = BashOperator( 
            task_id="t2",
            bash_command="echo World"
        )
    
    t1 >> t2 
