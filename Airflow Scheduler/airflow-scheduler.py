from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.email_operator import EmailOperator

# Function to create airflow-scheduler
def my_pipeline_dag(mysql_conn_id, postgres_conn_id, email_to):
    default_args = {
        'owner': 'airflow',
        'start_date': datetime(2022, 1, 1),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5)
    }

    dag = DAG('my_pipeline_dag', default_args=default_args, schedule_interval='@daily')

    # Task 1: Extract data from MySQL database
    t1 = MySqlOperator(
        task_id='extract_data',
        mysql_conn_id=mysql_conn_id,
        sql='SELECT * FROM mytable;',
        dag=dag
    )

    # Task 2: Clean and transform data using Python
    def clean_data():
        # TODO: Implement data cleaning and transformation logic here
        print("Cleaning and transforming data...")

    t2 = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
        dag=dag
    )

    # Task 3: Load data into PostgreSQL database
    t3 = PostgresOperator(
        task_id='load_data',
        postgres_conn_id=postgres_conn_id,
        sql='INSERT INTO mytable VALUES (...);',
        dag=dag
    )

    # Task 4: Send notification email
    t4 = EmailOperator(
        task_id='send_notification',
        to=email_to,
        subject='Data pipeline complete',
        html_content='<p>The data pipeline has finished running.</p>',
        dag=dag
    )

    # Set task dependencies
    t1 >> t2 >> t3 >> t4

    return dag
