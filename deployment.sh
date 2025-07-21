#!/bin/bash

echo "Starting deployment script..."

fuser -k -n tcp 8000

rm -rf kindo-challenge-ui/build
rm -rf kindo-challenge-ui/static


mkdir sinhala-song-predictor-backend/static

cd kindo-challenge-ui/

npm install

npm run build

cp -r build/* static/

cd ../

cd kindochallengebackend/

source myenv/nv/bin/activate

uvicorn kindoapp.main:app --host 0.0.0.0 --port 8000 &

echo "Deployment completed"