"""Dag to inspect the context variables.

Created on: 17/11/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="listing_4_03",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
)


def _print_context(**kwargs):
    print(kwargs)
    kwargs


print_context = PythonOperator(
    task_id="print_context", python_callable=_print_context, dag=dag
)

if __name__ == "__main__":
    dag.test()
