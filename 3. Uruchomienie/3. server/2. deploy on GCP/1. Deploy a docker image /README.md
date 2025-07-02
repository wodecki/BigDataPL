0. Create a `.dockerignore` file with only 1 line:
Dockerfile
1. Build the image: 
docker build . --platform linux/amd64 -t iowa
3. Tag the image:
docker tag iowa:latest europe-west4-docker.pkg.dev/bigdata2024-420908/bigdata/iowa:latest
4. Push the image to the registry:
docker push europe-west4-docker.pkg.dev/bigdata2024-420908/bigdata/iowa:latest
5. Query:
curl "https://iowa-fne6tu3xva-ez.a.run.app/predict/BLACK%20VELVET" < change the servise address!

5. Push to dockerhub
  6.1. Tag the image:
  docker tag iowa:latest andrzejwodecki/bigdata:iowa
  6.2. Push the image
  docker push andrzejwodecki/bigdata:iowa
  6.3. Run the image (from some linux/intel machine)
  6.3.1. Pull the image from dockerhub
  docker pull andrzejwodecki/bigdata:iowa
  6.3.2. Run the container
  docker run -d -p 8003:8003 andrzejwodecki/bigdata:iowa
  6.3.3. query (from another machine, like Your notebook)

  ##### curl "http://34.141.246.254:8003/predict/BLACK%20VELVET"  < change the address of Your server