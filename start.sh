#!/bin/sh

############################################
#
# File Name : start.sh
#
# Purpose :
#
# Creation Date : 16-09-2015
#
# Last Modified : Ср. 16 сент. 2015 12:21:59
#
# Created By : iandriyanov
#
############################################

PROJ_DIR=/var/www/django-site/


sudo apt-get update

apt-get upgrade -y

sudo apt-get install -y git python3 python3-dev python-virtualenv virtualenvwrapper postgresql-9.3 postgresql-server-dev-9.3

if [ ! -d $PROJ_DIR ]; then $(which mkdir) -p $PROJ_DIR; fi
$(which virtualenv) --no-site-packages --python=$(which python3) $PROJ_DIR

$PROJ_DIR/bin/pip install --upgrade pip setuptools distribute
$PROJ_DIR/bin/pip install django==1.8.4 psycopg2
sudo -u postgres psql -c "CREATE ROLE dbuser;"
sudo -u postgres psql -c "ALTER ROLE dbuser WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION PASSWORD '1q2w3e4r';"
sudo -u postgres $(which createdb) clinic -O dbuser

if [ ! -d $PROJ_DIR/project ]; then $(which mkdir) -p $PROJ_DIR/project; fi
git clone https://github.com/iandriyanov/ClinicEntry.git $PROJ_DIR/project/

cd $PROJ_DIR/project/
. $PROJ_DIR/bin/activate
$PROJ_DIR/bin/python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('myadmin', '', '1q2w3e4r')" | $PROJ_DIR/bin/python manage.py shell
