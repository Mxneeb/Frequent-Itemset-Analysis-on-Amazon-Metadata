import json
from kafka import KafkaConsumer
from collections import Counter, defaultdict
from itertools import combinations

consumer = KafkaConsumer('preprocessed_data', bootstrap_servers='localhost:9092')


def apriori(rows, threshold):
    frequentIndividuals = []
    frequentPairs = []
    frequentTriples = []
    
    # finding unique items and counting their frequency
    itemCount = Counter(item for row in rows for item in set(row))
    # finding frequent items by comparing them to the threshold
    frequentItems = [(item, count) for item, count in itemCount.items() if count >= threshold]
    
    # generating frequent pairs
    for pair in combinations([item for item, _ in frequentItems], 2):
        pairCount = sum(1 for row in rows if set(pair).issubset(set(row)))
        if pairCount+1 > threshold:
            frequentPairs.append((pair, pairCount))
    
    # generating frequent triples
    for triple in combinations([item for item, _ in frequentItems], 3):
        countOfTriples = sum(1 for row in rows if set(triple).issubset(set(row)))
        if countOfTriples >= threshold:
            frequentTriples.append((triple, countOfTriples))
    
    return frequentItems, frequentPairs, frequentTriples


def dataGetter(dataOfRows, threshold):
	return apriori(dataOfRows, threshold)
	
        
def dataWriter(frequentItems, frequentPairs, frequentTriples):
	# Write frequent itemsets to file
	with open('Apriori.txt', 'a') as file:
		file.write("Individual Items:\n")
		for item, count in frequentItems:
	    		file.write(f"Item: {item}, Frequency: {count}\n")

		file.write("\nPairs:\n")
		for pair, count in frequentPairs:
		    file.write(f"Pair: {pair}, Frequency: {count}\n")

		file.write("\n\nTriples:\n")
		for triple, count in frequentTriples:
		    file.write(f"Triple: {triple}, Frequency: {count}\n")

	print("Frequent itemsets written to file.")

def processInput(threshold):
    dataOfRows = []
    dataOfRowCounter = 0
    
    for message in consumer:
        data = json.loads(message.value.decode('utf-8'))
        dataOfRows.append(data)  
        dataOfRowCounter += 1
        
        print(f"Received {dataOfRowCounter} rows out of 50")  # Print the count of received rows
        
        if dataOfRowCounter >= 50:  # Check if at least 50 rows received
            frequentItems, frequentPairs, frequentTriples = dataGetter(dataOfRows, threshold)
            
            dataWriter(frequentItems,frequentPairs,frequentTriples)

            
            # Reset accumulated rows and counter
            dataOfRows.clear()
            dataOfRowCounter = 0



if __name__ == "__main__":
    threshold = 7
    processInput(threshold)
