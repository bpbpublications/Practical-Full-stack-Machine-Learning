import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(12)
    }

with DAG(dag_id="myPool_dag", default_args=default_args, 
max_active_runs=2, schedule_interval="@daily", catchup = False) as dag:

    t1 = BashOperator( 
            task_id="t1",
            pool='api_pool',
            priority_weight = 1,
            bash_command="echo Hello t1"
        )

    t2 = BashOperator( 
            task_id="t2",
            pool='api_pool',
            priority_weight = 2,
            bash_command="echo Hello t2"
        )
    
    t3 = BashOperator( 
            task_id="t3",
            pool='api_pool',
            priority_weight = 3,
            bash_command="echo Hello t3"
        )

    t4 = BashOperator( 
            task_id="t4",
            pool='api_pool',
            priority_weight = 4,
            bash_command="echo Hello t4"
        )

    t5 = BashOperator( 
            task_id="t5",
            bash_command="echo Finally All."
        )
    [t1,t2,t3,t4] >> t5 
