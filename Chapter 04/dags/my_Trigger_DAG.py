from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

############################### Controller DAG #################
dag_controller = DAG(
    dag_id="trigger_controller_dag",
    default_args={"owner": "airflow"},
    start_date=days_ago(2),
    schedule_interval="@once"
)

def send_msg(context, dag_run_obj):
    dag_run_obj.payload = {'message': 'Hello World'}
    if True:
        return dag_run_obj

trigger = TriggerDagRunOperator(
    task_id="trigger_dagrun",
    trigger_dag_id="trigger_target_dag",  # Ensure this equals the dag_id of the DAG to trigger
    python_callable=send_msg,
    dag=dag_controller,
)
############################### Target DAG #################

dag_target = DAG(
    dag_id="trigger_target_dag",
    default_args={"owner": "airflow"},
    start_date=days_ago(2),
    schedule_interval=None
)

def run_this_func(**kwargs):
    print("Remote value of {} for key=message".format(kwargs["dag_run"].conf["message"]))


run_this = PythonOperator(task_id="run_this", provide_context=True,
    python_callable=run_this_func, dag=dag_target)

bash_task = BashOperator(
    task_id="bash_task",
    bash_command='echo "Here is the message: $message"',
    env={'message': '{{ dag_run.conf["message"] if dag_run else "" }}'},
    dag=dag_target,
)

run_this >> bash_task