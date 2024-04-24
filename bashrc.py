#!/bin/bash

echo "Starting Zookeeper..."
zookeeper-server-start.sh /config/zookeeper.properties &

echo "Starting Kafka Server..."
kafka-server-start.sh /config/server.properties &

# Run Producer
echo "Running Producer..."
python producer.py &

# Run Consumer1 (Apriori)
echo "Running Consumer1 (Apriori)..."
python consumer1.py &

# Run Consumer2 (PCY)
echo "Running Consumer2 (PCY)..."
python consumer2.py &

# Run Consumer3 (Bloom Filter)
echo "Running Consumer3 (Bloom Filter)..."
python consumer3.py &

# Wait for all processes to finish
wait

echo "All processes have finished."

