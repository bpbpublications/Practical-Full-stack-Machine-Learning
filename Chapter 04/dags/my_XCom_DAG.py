import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
}

def _push_xcom_return_value():
    return 'Hello_XCom'

def _get_xcom_return_value(**kwargs):
    print(kwargs['ti'].xcom_pull(task_ids='task0')) 

def _push_next_task(**kwargs):
    kwargs['ti'].xcom_push(key='next_task', value='task3')

def _get_next_task(**kwargs):
    return kwargs['ti'].xcom_pull(key='next_task')

def _get_multiple_xcoms(**kwargs):
    print(kwargs['ti'].xcom_pull(key=None, task_ids=['t0', 'task2']))

with DAG(dag_id='my_xcom_dag', default_args=args, schedule_interval=None) as dag:
    
    task0 = PythonOperator(
        task_id='task0',
        python_callable=_push_xcom_return_value
    )

    task1 = PythonOperator(
        task_id='task1',
        provide_context=True,
        python_callable=_get_xcom_return_value
    )

    task2 = PythonOperator(
        task_id='task2',
        provide_context=True,
        python_callable=_push_next_task
    )

    branching = BranchPythonOperator(
        task_id='branching',
        provide_context=True,
        python_callable=_get_next_task,
    )

    task3 = DummyOperator(task_id='task3')

    task4 = DummyOperator(task_id='task4')

    task5 = PythonOperator(
        task_id='task5',
        trigger_rule='one_success',
        provide_context=True,
        python_callable=_get_multiple_xcoms
    )

    task6 = BashOperator(
        task_id='task6',
        bash_command="echo value from xcom: {{ ti.xcom_pull(key='next_task') }}"
    )

    task0 >> task1
    task1 >> task2 >> branching
    branching >> task3 >> task5 >> task6
    branching >> task4 >> task5 >> task6