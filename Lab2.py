from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import pickle

# define the DAG
dag = DAG(
    'classification_model',
    description='Creating and evaluating a classification model',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
)


# preprocess the dataset
def preprocess_data(**context):
    url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-08-10/investment.csv'
    df = pd.read_csv(url, sep=',').replace('"', '', regex=True)

    # converting the category and meta_cat columns to categorical data type
    df['category'] = df['category'].astype('category')
    df['meta_cat'] = df['meta_cat'].astype('category')
    # creating dummy variables for the categorical columns
    df = pd.get_dummies(df, columns=['category', 'meta_cat'], prefix=['cat', 'meta'])
    # splitting data into features and target
    X = df.drop(['gross_inv', 'group_num', 'year'], axis=1)
    y = np.where(df['gross_inv'] >= df['gross_inv'].median(), 1, 0)
    # split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # store data in the context
    context['task_instance'].xcom_push(key='X_train', value=X_train.to_json(orient='split'))
    context['task_instance'].xcom_push(key='X_test', value=X_test.to_json(orient='split'))
    context['task_instance'].xcom_push(key='y_train', value=y_train.tolist())
    context['task_instance'].xcom_push(key='y_test', value=y_test.tolist())


preprocess_data = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    provide_context=True,
    dag=dag
)


# train the model
def train_model(**context):
    X_train = pd.read_json(context['task_instance'].xcom_pull(task_ids='preprocess_data', key='X_train'),
                           orient='split').values
    y_train = np.array(context['task_instance'].xcom_pull(task_ids='preprocess_data', key='y_train'))

    clf = LogisticRegression(random_state=42)
    clf.fit(X_train, y_train)

    # Save the model as a pickle file
    with open('logistic_regression_model.pkl', 'wb') as f:
        pickle.dump(clf, f)

    context['task_instance'].xcom_push(key='model_file_path', value='logistic_regression_model.pkl')


train_model = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag
)


# evaluate the model
def evaluate_model(**context):
    X_test = pd.read_json(context['task_instance'].xcom_pull(task_ids='preprocess_data', key='X_test'),
                 orient='split').values
    y_test = np.array(context['task_instance'].xcom_pull(task_ids='preprocess_data', key='y_test'))
    model_file_path = context['task_instance'].xcom_pull(task_ids='train_model', key='model_file_path')

    # Load the saved model
    with open(model_file_path, 'rb') as f:
        clf = pickle.load(f)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f"Accuracy score: {accuracy}")
    print(classification_report(y_test, y_pred))


evaluation = PythonOperator(
    task_id='evaluate_model',
    depends_on_past=False,
    python_callable=evaluate_model,
    dag=dag,
)

preprocess_data >> train_model
train_model >> evaluation
