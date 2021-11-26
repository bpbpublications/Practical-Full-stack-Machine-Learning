import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
import pendulum

from datetime import datetime, timedelta

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(12)
    }

def _decide_task(**context):
    year = context["execution_date"].year
    if year < 2022:
        return 'task_2a'
    else:
        return 'task_3a'

with DAG(dag_id="myPython_branch_dag", default_args=default_args, 
schedule_interval="@daily") as dag:

    start = BashOperator( 
            task_id="start",
            bash_command="echo Start"
        )
    decide_task = BranchPythonOperator(
       task_id='decide_task',
       provide_context=True,
       python_callable=_decide_task,
        )    
    task_2a = BashOperator( 
            task_id="task_2a",
            bash_command="echo execute task_2a"
        )

    task_2b = BashOperator( 
                task_id="task_2b",
                bash_command="echo execute task_2b"
            )
    task_3a = BashOperator( 
            task_id="task_3a",
            bash_command="echo execute task_3a"
        )

    task_3b = BashOperator( 
                task_id="task_3b",
                bash_command="echo execute task_3b"
            )
    
    finish = BashOperator( 
                task_id="finish",
                trigger_rule = "one_success",
                bash_command="echo Finish"
            )
    
start >> decide_task >> task_2a >> task_2b
start >> decide_task >> task_3a >> task_3b
task_2b >> finish
task_3b >> finish