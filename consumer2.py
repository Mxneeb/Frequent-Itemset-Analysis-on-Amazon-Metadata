import json
from kafka import KafkaConsumer
from collections import Counter, defaultdict
from itertools import combinations

consumer = KafkaConsumer('preprocessed_data', bootstrap_servers='localhost:9092')


def pcy(rows, threshold, hashBucketSize):
    # counting items using hashtable
    countOfItems = defaultdict(int)
    for row in rows:
        for item in row:
            countOfItems[item] += 1
    
    # counting pairs using hash table
    countOfPairs = defaultdict(int)
    for row in rows:
        for pair in combinations(row, 2):
            hash_val = hash(tuple(sorted(pair))) % hashBucketSize
            countOfPairs[hash_val] += 1
    
    # generating frequent items
    frequentItems = [(item, count) for item, count in countOfItems.items() if count >= threshold]
    
    # generating frequent pairs with ASIN
    frequentPairs = []
    for pair_hash, count in countOfPairs.items():
        if count+1 > threshold:
            # hash to asin conversion
            asin_pair = tuple(sorted(pair))
            frequentPairs.append((asin_pair, count))
    
    return frequentItems, frequentPairs

def dataWriter(freqItems, freqPairs):
    with open('PCY.txt', 'a') as file:
        file.write("\n\n\nFrequent Items:\n")
        for item, count in freqItems:
            file.write(f"Item: {item}\n")
        
        file.write("\nFrequent Pairs:\n")
        for pair, count in freqPairs:
            file.write(f"Pair: {pair}\n")
    
    print("Frequent itemsets written to file.")


def processInput(threshold, hashBucketSize):
    dataCollected = []
    CountOfDataCollected = 0
    
    for message in consumer:
    
        data = json.loads(message.value.decode('utf-8'))
        
        dataCollected.append(data)  # Append each received row as a list
        CountOfDataCollected += 1
        
        if CountOfDataCollected >= 50:  
            frequentItems, frequentPairs = pcy(dataCollected, threshold, hashBucketSize)
            
            dataWriter(frequentItems,frequentPairs)
            
            dataCollected = []
            CountOfDataCollected = 0  # Reset batch count


if __name__ == "__main__":
    threshold = 7
    hashBucketSize = 20 
    processInput(threshold, hashBucketSize)
