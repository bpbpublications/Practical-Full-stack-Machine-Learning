from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "start_date": datetime(2019, 11, 1)
}

def _error_function():
    raise Exception('Alert!Alert!')

with DAG(dag_id="myEmail_dag", default_args=default_args,
    schedule_interval=None) as dag:
        send_completion_mail = EmailOperator(
            task_id="send_completion_mail", 
            to='receivers@mail.com',
            subject='Task Completion',
            html_content='<p> Your Job was completed <p>')    
          
        Dummy_task = PythonOperator(
            task_id='Dummy_task',
            python_callable=_error_function,
            email_on_failure=True,
            email='receivers@mail.com')

Dummy_task >> send_completion_mail