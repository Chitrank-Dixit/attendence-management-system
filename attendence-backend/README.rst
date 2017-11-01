PantoMath Backend Project
=========================


Technology Used
----------------
- Python 3.5.1
- Django 1.10.5
- PostGreSQL 9.5
- PostGis (for geolocation)

for server need to install some additional libraries:

for developer tools (virtualenv related problems)
http://stackoverflow.com/questions/26053982/error-setup-script-exited-with-error-command-x86-64-linux-gnu-gcc-failed-wit

for socket error in supervisor
http://stackoverflow.com/questions/18859063/supervisor-socket-error-issue

$ sudo apt-get install libgdal-dev postgis
sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update

in postgresql

postgres=# CREATE EXTENSION postgis;



Installtion Instructions
--------------------------


- <h3>Setup Development Environment </h3>
    - Create new python virtual environment use the following command <br>
    `$ pyevev ~/<your_preferred_virtualenv_directory>/pantomath-env` <br>
    after running the above command activate the virtualenv using the below command <br>
    `$ source ~/<your_preferred_virtualenv_directory>/pantomath-env/bin/activate` <br>
    To deactivate the virtualenv you can use the below command <br>
    `$ deactivate`

    - Now clone this repo switch to develop branch for now (because currently
    there is no proper release), in order to clone the repository use command <br>
    `$ git clone https://chitrank_dixit@bitbucket.org/pantomathtechnologies/pantomath-backend.git`

    - now activate your virtual environment and install the required packages to run the project , try the below command <br>
    `pip install requirements/base.txt` <br>
      - If you are on local machine also install the packages in `local.txt` <br>
      `$ pip install requirements/local.txt`
      - If you are on staging server also install the packages in `staging.txt` <br>
      `$ pip install requirements/staging.txt`
      - If you are on production server also install the packages in `production.txt` <br>
      `$ pip install requirements/production.txt`

      <b>Note # 1:</b> <i>In most of the cases `staging.txt` and `production.txt` contents would be same there may be some exceptions in future therefor these requirements are being separated </i><br>
      <b>Note # 2:</b> <i>Currently we have a module named `django-elasticsearch` that is not hosted on pypi so we can not install it from pip install django-elasticsearch so please use this command to install that package </i><br>
      `$ pip install git+https://github.com/liberation/django_elasticsearch.git`

    - The developers can make their own developer_specific settings file in `/pantomath/config/developer_specific/<developer_name>.py`
    but please remember to keep in the `.gitignore` file and never push this developer specific file.
     please copy the below sample to create your own developer specific file

     developer_1.py

     ```
     from ..local import *

     # local database settings below

     DATABASES = {
          'default': {
              'ENGINE': 'django.contrib.gis.db.backends.postgis',
              'NAME': 'pantomath_db',
              'USER': 'pantomath_admin',
              'PASSWORD': '<db_password>',
              'HOST': '127.0.0.1',
              'PORT': '5432',  # you can change this like: DATABASES['default']['PORT'] = 'some_other_port'
          }
     }
     ```
