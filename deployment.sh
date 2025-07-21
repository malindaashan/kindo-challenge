#!/bin/bash

echo "Starting deployment script..."

fuser -k -n tcp 8000
cd /opt/kindo-challenge/kindo-challenge-ui/

rm -rf kindo-challenge-ui/build
rm -rf kindo-challenge-ui/static


mkdir kindo-challenge-ui/static


npm install

npm run build

cp -r build/* static/*

cd ../

cd kindochallengebackend/

source myenv/nv/bin/activate

uvicorn kindoapp.main:app --host 0.0.0.0 --port 8000 &

sudo systemctl status nginx.service

echo "Deployment completed"