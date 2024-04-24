from kafka import KafkaProducer
import json
import time

# Define Kafka producer configuration
producer_config = {
    'bootstrap_servers': 'localhost:9092',  # Kafka broker address
    # Add any additional configuration parameters here
}

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Function to send data to Kafka with a delay
def send_data_to_kafka(data):
    try:
        # Produce the data to Kafka topic named 'preprocessed_data'
        producer.send('preprocessed_data', value=data.encode('utf-8'))
        print("Data sent to Kafka:", data)
    except Exception as e:
        print(f"Error sending data to Kafka: {e}")

# Open the preprocessed data JSON file and send each line to Kafka with a delay
with open('preprocessed_data.json', 'r') as infile:
    for line in infile:
        # Parse JSON data
        data = json.loads(line)
        # Extract the "also_buy" field
        also_buy = data.get('also_buy', [])
        # Convert the "also_buy" field to JSON string
        also_buy_json = json.dumps(also_buy)
        # Send "also_buy" data to Kafka
        send_data_to_kafka(also_buy_json)
        # Introduce a 2-second delay between sending each line
        time.sleep(1)

