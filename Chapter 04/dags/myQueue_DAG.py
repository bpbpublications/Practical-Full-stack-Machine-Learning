import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(12)
    }

with DAG(dag_id="myQueue_dag", default_args=default_args, 
max_active_runs=2, schedule_interval="@daily", catchup = True) as dag:

    t1_IO = BashOperator( 
            task_id="t1_IO",
            bash_command="echo Hello IO",
            #queue="worker_IO"
        )

    t2_CPU = BashOperator( 
            task_id="t2_CPU",
            bash_command="echo World of CPU",
            #queue="worker_CPU"
        )
    
    t3_Default = BashOperator( 
            task_id="t3_Default",
            bash_command="echo Default Of the World"            
        )
    
    t1_IO >> t2_CPU >> t3_Default 
