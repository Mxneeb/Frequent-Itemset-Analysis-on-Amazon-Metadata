from kafka import KafkaConsumer


import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    def __contains__(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True



# Initialize Kafka consumer
consumer = KafkaConsumer('preprocessed_data', bootstrap_servers=['localhost:9092'])

# Initialize Bloom Filter
size = 1000000
hash_count = 5
bloom_filter = BloomFilter(size, hash_count)

# Function to check if product IDs are in Bloom Filter
def check_product_ids(product_ids):
    for product_id in product_ids:
        if bloom_filter.__contains__(product_id):
            print(f"Product ID {product_id} may be in the list.")
        else:
            print(f"Product ID {product_id} is definitely not in the list.")

# Read product IDs from Kafka producer in batches
window_size = 10
product_ids_window = []

for message in consumer:
    product_id = message.value.decode('utf-8')
    product_ids_window.append(product_id)
    
    if len(product_ids_window) == window_size:
        # Check product IDs against Bloom Filter
        check_product_ids(product_ids_window)
        # Clear the window for the next batch
        product_ids_window = []

# If there are remaining product IDs not forming a full window
if product_ids_window:
    check_product_ids(product_ids_window)

