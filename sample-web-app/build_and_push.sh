#! /bin/bash
echo "Building..."
docker build -t gmsantos3/sample-web-app:dev4 .

echo "Pushing..."
docker push gmsantos3/sample-web-app:dev4

echo "Done!"