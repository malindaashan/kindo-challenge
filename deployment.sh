#!/bin/bash

echo "Starting deployment script..."

fuser -k -n tcp 8000
cd /opt/kindo-challenge/kindo-challenge-ui/

sudo rm -rf /opt/kindo-challenge/kindo-challenge-ui/kindo-challenge-ui/build


sudo mkdir /opt/kindo-challenge/kindo-challenge-ui/static


npm install

npm run build

sudo cp -r /opt/kindo-challenge/kindo-challenge-ui/build/* /opt/kindo-challenge/kindo-challenge-ui/static

sudo chown -R ec2-user:ec2-user /opt/kindo-challenge/kindo-challenge-ui/static

source /opt/kindo-challenge/kindochallengebackend/myenv/bin/activate

cd  /opt/kindo-challenge/kindochallengebackend

uvicorn kindoapp.main:app --host 0.0.0.0 --port 8000 &

sudo systemctl status nginx.service

echo "Deployment completed"