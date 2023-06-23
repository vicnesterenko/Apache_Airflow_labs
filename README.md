# Apache_Airflow_labs
Building data processing pipelines in Apache Airflow/ELT patern

1. Firstly, you should install Apache Airflow on your PC. If ypu use Windows system, you can use Ubuntu subsystem - https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6. Don't forget to go to Windows Developer Settings and install developer mode (Developer Mode). Also in Windows tools (Windows Features) you need to enable the Windows Subsystem for Linux component.

![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/337f98ea-2967-469c-b3d5-bac2362765d1)

  Then, you should install all packages by following commands below:

   sudo apt-get update
   
   sudo apt-get install libmysqlclient-dev
   
   sudo apt-get install libkrb5-dev
   
   sudo apt-get install libsasl2-dev

   sudo apt-get install postgresql postgresql-contrib

   sudo service postgresql start

   sudo nano /etc/postgresql/*/main/pg_hba.conf

   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/5cfedbe4-6189-4890-afa6-825180b4838c)

   sudo service postgresql restart

   sudo apt install python3-pip

   pip install apache-airflow

   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/c119b70e-4842-4c4f-8ffb-8472d07d5409)

   sudo pip install apache-airflow

   airflow db init

   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/a5162d61-3ba4-4f07-84f0-28980a32741b)
   
   sudo apt-get install build-dep python-psycopg2
   
   pip install psycopg2-binary 
   
   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/f01e5968-c352-4dc0-aa72-9641f6d4b31a)

2. For the next step, ypu should check or put your DAGs in folder by this path C:/Users/vicwa/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/vic/airflow/dags:
   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/46ca20aa-926a-4116-8e46-32139f2a55b9)
3. Create database:

   psql -h 127.0.0.1 -d airflow -U vic

   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/75ceeca1-0eac-427d-a31c-ab9a2faa6851)

4. Write following commands in Ubuntu console:

   sudo service postgresql restart

   airflow db init

   airflow webserver -p 8080

   airflow scheduler

   sudo service postgresql restart

   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/dd971cac-6da8-446c-8b99-9959ce434290)

5. Results for Lab1:

   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/6cf7000d-f5e1-4c8c-a1ab-3eeea626b964)

   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/40104034-f325-47ad-9324-818564eef9c7)

   ![image](https://github.com/vicnesterenko/Apache_Airflow_labs/assets/136901590/aa55f2eb-67ca-456f-8489-0f69549520c8)


   


 


