from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, Airflow!")

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='simple_test_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['example'],
) as dag:
    task_hello = PythonOperator(
        task_id='hello_world_task',
        python_callable=hello_world,
    )