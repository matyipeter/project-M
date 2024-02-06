#!/bin/bash
set -e

echo -e "\n>>> Copying Django project files to server"

echo -e "\n>>> Preparing scripts locally"
rm -rf deploy
mkdir deploy
cp -r config deploy
cp -r scripts deploy
cp -r appdev deploy
cp requirements.txt deploy

echo -e "\n>>> Copying files to the server"
ssh server "rm -rf /root/deploy/"
scp -r deploy server:/root/

echo -e "\n>>> Cleaning up deployed files on the server"
ssh server /bin/bash << EOF
    set -e
    find /root/deploy/ -name *.pyc -delete
    find /root/deploy/ -name __pycache__ -delete
EOF

echo -e "\n>>> Finished"