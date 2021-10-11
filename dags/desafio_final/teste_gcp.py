import json
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from google.cloud import storage

json_account_info = json.loads(Variable.get("GOOGLE_APPLICATION_CREDENTIALS_JSON"))
google_storage = storage.Client.from_service_account_info(json_account_info)


def list_buckets():
    print(google_storage.list_buckets())


with DAG(
        'google_sdk_test',
        default_args=dict(start_date=days_ago(1)),
        schedule_interval='@once',
        tags=['example'],
) as dag:
    list_buckets_python_operator = PythonOperator(
        task_id="list_buckets",
        python_callable=list_buckets
    )
