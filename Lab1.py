from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
import pandas as pd
import psycopg2 as pg
from datetime import timedelta
dag = DAG(
 'Lab1_Nesterenko',
 description='A simple DAG',
 schedule_interval=timedelta(days=1),
 start_date=days_ago(90),
)
download_launches = BashOperator(
 task_id='download_launches',
 depends_on_past=False,
 bash_command='curl -o /home/vic/airflow/tmp/simpsonsGuests.csv 
https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2
019/2019-08-27/simpsons-guests.csv',
 dag=dag,
)
def add_to_db(**context):
 conn = pg.connect("host=127.0.0.1 dbname=airflow user=vic 
password=1111")
 #create table "simpsonsGuests" if not exists
 cur = conn.cursor()
 cur.execute("CREATE TABLE IF NOT EXISTS simpsonsGuests ("
 "season varchar, "
 "number varchar, "
 "production_code varchar, "
 "episode_title varchar, "
 "guest_star varchar, "
 "role varchar"
 ");")
 conn.commit()
 cur.close()
 #read csv and upload to DB
 df = pd.read_csv('/home/vic/airflow/tmp/simpsonsGuests.csv', 
error_bad_lines=False, sep='|')
 cur = conn.cursor()
 for index, row in df.iterrows():
 #if NAN in row, replace with NULL
 row = row.where(pd.notnull(row), None)
 cur.execute("INSERT INTO simpsonsGuests VALUES (%s, %s, %s, %s, %s, 
%s);",
 (row['season'], row['number'], row['production_code'], 
row['episode_title'], row['guest_star'], row['role']))
 conn.commit()
 cur.close()
 conn.close()
 #read data from csv
# add downloaded data to db
add_to_db = PythonOperator(
 task_id='add_to_db',
 depends_on_past=False,
 python_callable=add_to_db,
 dag=dag,
)
def checkValidity(**context):
 df = pd.read_csv('/home/vic/airflow/tmp/simpsonsGuests.csv', 
error_bad_lines = False, sep = '|')
 for index, row in df.iterrows():
 if "-" in row["season"]:
 raise Exception("error")
test = PythonOperator(
 task_id='checkValidity',
 depends_on_past=False,
 python_callable=checkValidity,
 dag=dag
)
def do_tasks_1_2(**context):
 conn = pg.connect("host=127.0.0.1 dbname=airflow user=vic 
password=1111")
 cur = conn.cursor()
 cur.execute("SELECT * FROM simpsonsGuests WHERE number = '553–2601';")
 rows = cur.fetchall()
 cur.close()
 conn.close()
 if len(rows) > 100:
 return 'task_1'
 else:
 return 'task_2'
do_tasks_1_2 = BranchPythonOperator(
 task_id='do_tasks_1_2',
 depends_on_past=False,
 python_callable=do_tasks_1_2,
 dag=dag,
)
def task_1(**context):
 conn = pg.connect("host=127.0.0.1 dbname=airflow user=vic 
password=1111")
 cur = conn.cursor()
 cur.execute("SELECT count(*) as guestsCount FROM simpsonsGuests where 
episode_title = 'Homer at the Bat' ")
 rows = cur.fetchall()
 cur.close()
 conn.close()
 print(rows)
task_1 = PythonOperator(
 task_id='task_1',
 depends_on_past=False,
 python_callable=task_1,
 dag=dag,
)
def task_2(**context):
 conn = pg.connect("host=127.0.0.1 dbname=airflow user=vic 
password=1111")
 cur = conn.cursor()
 cur.execute("SELECT max(guestsCount) FROM (select count(guest_star) AS 
guestsCount, number FROM simpsonsGuests GROUP BY number) As 
maxGuestsCountInNumber;")
 rows = cur.fetchall()
 cur.close()
 conn.close()
 print(rows)
task_2 = PythonOperator(
 task_id='task_2',
 depends_on_past=False,
 python_callable=task_2,
 dag=dag,
)
combine = DummyOperator(
 task_id='combine',
 depends_on_past=False,
 trigger_rule='none_failed',
 dag=dag,
)
end = DummyOperator(
 task_id='end',
 depends_on_past=False,
 dag=dag,
)
download_launches >> test
test >> add_to_db
add_to_db >> do_tasks_1_2
do_tasks_1_2 >> [task_1, task_2] >> combine
combine >> end