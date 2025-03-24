
From the container:
    docker exec -it my_postgres psql -U myuser -d mydb
From your Mac (if you have psql installed):
    psql -h localhost -U myuser -d mydb


Inside the Docker container:
    docker exec -it my_redis redis-cli
    SET mykey "Hello, Redis!"
    GET mykey
From your Mac (if you have redis-cli installed):
    redis-cli -h localhost -p 6379


Inside the Docker container:
    docker exec -it my_mongodb mongosh -u admin -p adminpassword
From your Mac (if you have mongosh installed):
    mongosh "mongodb://admin:adminpassword@localhost:27017"


docker exec -it my_cassandra cqlsh

List Kafka Topics
    docker exec -it my_kafka kafka-topics --bootstrap-server localhost:9092 --list
Create a Kafka Topic
    docker exec -it my_kafka kafka-topics --bootstrap-server localhost:9092 --create --topic test-topic --partitions 1 --replication-factor 1
Publish a Message
    docker exec -it my_kafka kafka-console-producer --broker-list localhost:9092 --topic test-topic
Consume Messages
    docker exec -it my_k


docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Networks}}"

If your services are already in the default bridge network and your Flask app can't connect to Redis, the issue is likely due to how networking works in Docker. The default bridge network does NOT support automatic service name resolution, meaning you must use a custom bridge network or explicitly reference the Redis container’s IP.


Best Practice: Use a custom bridge network (Solution 1) so your services can communicate by name.
Avoid Using IP Addresses (Solution 2) because they can change.

docker network create my_custom_network

docker run -d --name my_redis --network my_custom_network redis
docker run -d --name my_flask_app --network my_custom_network my_flask_image

docker network inspect my_custom_network

docker network rm my_custom_network


by custom network can I use localhose?
No, you cannot use localhost when using a custom Docker network.
Why?
Inside a Docker container, localhost (127.0.0.1) refers to the container itself, NOT the host machine or other containers.
If you use a custom bridge network, containers must communicate using their service name (not localhost).





mkdir -p /Users/shivshankarkeshari/Documents/docker_volume/{grafana-data,postgres-data,kafka-data,mongodb-data,cassandra-data}
docker-compose up -d

