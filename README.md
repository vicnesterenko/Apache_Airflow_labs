# Apache_Airflow_labs

## Building data processing pipelines in Apache Airflow/ELT pattern

_This repository showcases the results of the labs completed during my first semester at Igor Sikorsky Kyiv Polytechnic Institute, where I pursued a Master's degree in Informatics and Software Engineering🎓_ - ![Link of faculty](https://fiot.kpi.ua/)


_The labs primarily focus on Apache Airflow and demonstrate data processing pipelines built using the ELT pattern. Through this repository, I aim to share my practical experiences and learnings from these labs with others interested in data engineering and workflow automation using Apache Airflow._

### Installation

1. Before proceeding, ensure you have Apache Airflow installed on your PC. If you are using a Windows system, you can use the Ubuntu subsystem available at https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6. Make sure to enable developer mode in Windows Developer Settings and activate the Windows Subsystem for Linux component in Windows Features.

![Ubuntu Subsystem](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/337f98ea-2967-469c-b3d5-bac2362765d1)

2. Install the required packages by running the following commands:

```bash
sudo apt-get update
sudo apt-get install libmysqlclient-dev
sudo apt-get install libkrb5-dev
sudo apt-get install libsasl2-dev
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start
sudo nano /etc/postgresql/*/main/pg_hba.conf
```

![PostgreSQL Configuration](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/5cfedbe4-6189-4890-afa6-825180b4838c)

```bash
sudo service postgresql restart
sudo apt install python3-pip
pip install apache-airflow
```

![Install Apache Airflow](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/c119b70e-4842-4c4f-8ffb-8472d07d5409)

```bash
sudo pip install apache-airflow
airflow db init
```

![Initialize Airflow Database](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/a5162d61-3ba4-4f07-84f0-28980a32741b)

```bash
sudo apt-get install build-dep python-psycopg2
pip install psycopg2-binary
```

![Install psycopg2-binary](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/f01e5968-c352-4dc0-aa72-9641f6d4b31a)

### Setting up DAGs

3. Place your DAGs in the following folder path: C:/Users/vicwa/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/vic/airflow/dags

![DAGs Path](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/46ca20aa-926a-4116-8e46-32139f2a55b9)

### Creating the database

4. Create a database using the following command:

```bash
psql -h 127.0.0.1 -d airflow -U vic
```

![Create Database](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/75ceeca1-0eac-427d-a31c-ab9a2faa6851)

### Running Airflow

5. Run the following commands in the Ubuntu console:

```bash
sudo service postgresql restart
airflow db init
airflow webserver -p 8080
airflow scheduler
sudo service postgresql restart
```

![Start Airflow Services](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/dd971cac-6da8-446c-8b99-9959ce434290)

### Lab1 Results

6. Results for Lab1:

![Result 1](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/6cf7000d-f5e1-4c8c-a1ab-3eeea626b964)

![Result 2](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/40104034-f325-47ad-9324-818564eef9c7)

![Result 3](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/aa55f2eb-67ca-456f-8489-0f69549520c8)

Please note that the provided links to images may need to be updated with the correct URLs to ensure they work correctly in the repository. Also, ensure the indentation and formatting are consistent to maintain readability.


 


