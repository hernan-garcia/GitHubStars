# Builds the Dockerfile
docker build -t bench/fetch_github:3.0 .

#docker network create spark_network
#########

# When executed, console is inside the docker instance
docker run --rm -it --name fetch_github --hostname fetch_github \
    -v /mnt/c/Users/hgarcia/Documents/Repos/GitHubStars/output:/output \
    -p 8080:8080  \
    bench/fetch_github:3.0
# Inside such docker instance launch the master inastance
#/spark/bin/spark-class org.apache.spark.deploy.master.Master --ip `hostname` --port 7077 --webui-port 8080

# docker stop spark-master
# docker rm spark-master
#########

