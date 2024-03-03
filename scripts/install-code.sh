#!/bin/bash
# Install DJango app on server

set -e

echo -e "\n>>> Installing Django project files on server"

ssh server /bin/bash << EOF
set -e
echo -e "\n>>>Stop gunicorn"
cd /app2/
source env/bin/activate

echo -e "\n>>>Delete old files"
rm -rf /app2/appdev
rm -rf /app2/scripts
rm -rf /app2/config
rm requirements.txt

echo -e "\n>>>Copy new files"
cp -r /root/deploy/appdev /app2/
cp -r /root/deploy/scripts /app2/
cp -r /root/deploy/config /app2/
cp /root/deploy/requirements.txt /app2/

echo -e "\n>>>Install python packages"
pip install -r requirements.txt

echo -e "\n>>>Run Django migrations"
cd appdev
./manage.py makemigrations
./manage.py migrate

echo -e "\n>>>Collect staticfiles"
./manage.py collectstatic
cd ..

echo -e "\n>>>Re-read Systemd config"

echo -e "\n>>>Start gunicorn"
systemctl restart gunicorn

EOF

echo -e "\n>>> Finished installing Django project files on server"
