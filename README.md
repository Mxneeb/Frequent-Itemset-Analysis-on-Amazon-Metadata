# Amazon Metadata Streaming and Frequent Itemset Mining

## Project Overview

This project leverages the **Amazon Metadata Dataset** to design and implement a robust real-time streaming pipeline for **frequent itemset mining**. Utilizing a producer-consumer architecture, the system efficiently processes massive data streams by integrating advanced algorithms such as **Apriori**, **PCY**, and **Bloom filters**. A **Sliding Window** approach ensures timely, incremental analysis, while results are persistently stored in a **MongoDB** database for scalable querying. To streamline deployment, an all-in-one **bash script** orchestrates the initialization and execution of all components.

---

## Dataset Description

The dataset comprises extensive product metadata in JSON format, including:

- **asin**: Unique product identifier (e.g., `0000031852`).
- **title**: Product name.
- **feature**: Bullet-point product features.
- **description**: Detailed product descriptions.
- **price**: Price in US dollars at the time of crawling.
- **imageURL**: Product image URL.
- **related**: Related product metadata (e.g., "also bought", "also viewed").
- **salesRank**: Sales rank information.
- **brand**: Brand name.
- **categories**: Hierarchical list of categories.
- **similar**: Table of similar products.

> **Note:** Original compressed dataset is **12GB**, expanding to **105GB** upon extraction. A sampled subset of at least **15GB** is used for practical analysis.

---

## Methodology

### 1. Dataset Management
- **Download & Extraction**: Full dataset downloaded and decompressed.
- **Sampling**: Created a representative 15GB+ subset for processing efficiency.

---

### 2. Data Preprocessing
- Removed redundant and irrelevant columns to optimize data throughput.
- Cleaned and normalized JSON entries for consistency.
- Exported a new preprocessed JSON file.
- **Bonus**: Implemented batch preprocessing to simulate real-time streaming ingestion.

---

### 3. Streaming Pipeline Architecture
- **Producer Application**: Reads the preprocessed JSON and streams data in real time to Kafka topics.
- **Consumer Applications**: Three distinct consumers subscribe to the Kafka topic, each applying a different mining algorithm:
  1. **Consumer 1**: Implements **Apriori algorithm** for mining frequent itemsets, outputting real-time patterns.
  2. **Consumer 2**: Uses **PCY algorithm**, optimizing frequent itemset mining with hash-based bitmap compression.
  3. **Consumer 3**: Applies **Bloom filter-based** frequent itemset mining enhanced with a **Sliding Window** model to capture temporal dynamics.

---

### 4. Frequent Itemset Mining Techniques
- Adapted classical Apriori and PCY algorithms for streaming data using:
  - **Sliding Window Model**: Ensures analysis focuses on recent data, adapting to evolving trends.
  - **Approximation and Incremental Updates**: Supports efficient, real-time updates without full re-computation.
  - **Decay Factor**: Gradually reduces the influence of older data for dynamic pattern detection.
  - **Online Algorithm Design**: Enables continuous data processing with minimal latency.
- Consumer 3 introduces innovative Bloom filter strategies combined with sliding windows for novel insights.

---

### 5. Database Integration
- Real-time mining results from all consumers are pushed to a **MongoDB** database.
- MongoDB schema designed for efficient querying and future extensibility.

---

### 6. Execution Automation
- Developed a **bash script** that automates:
  - Kafka ecosystem startup (Zookeeper, Kafka broker).
  - Producer and consumer application launches.
  - MongoDB service initialization and configuration.
- This automation minimizes manual setup and ensures reproducibility.

---

## Step-by-Step Guide to Execution

### 1. Environment Setup
1.1 **Install Prerequisites**
- Kafka and Zookeeper (latest stable versions).
- MongoDB (configured with default ports).
- Python 3.x with necessary libraries (`pandas`, `json`, `kafka-python`, `pymongo`).

1.2 **Prepare Dataset**
- Download and extract the Amazon Metadata dataset.
- Sample at least 15GB of data for streaming input.

---

### 2. Code Configuration
2.1 **Producer Application**
- Configure to stream preprocessed JSON records into Kafka topics.

2.2 **Consumer Applications**
- Each consumer connects to Kafka, processes incoming data with its respective algorithm.
- Configure MongoDB connection parameters for result storage.

---

### 3. Automated Execution
- Run the provided **bash script** which:
  - Starts Zookeeper and Kafka brokers.
  - Launches the producer streaming service.
  - Initializes all three consumers.
  - Connects and configures MongoDB instance.

---

## Results and Findings

### 1. Real-Time Frequent Itemset Mining
- **Apriori and PCY consumers** delivered immediate insights on frequently co-occurring product features and categories.
- **Bloom filter consumer** successfully handled high-throughput streams with sliding window semantics, revealing temporal shifts in purchasing patterns.

### 2. Database Integration Efficiency
- MongoDB facilitated scalable storage and fast retrieval of mining results.
- Enabled multi-dimensional queries across time windows and algorithms.

### 3. Operational Efficiency
- The bash script drastically reduced startup complexity.
- Real-time data flow and mining were achieved with minimal latency.

---

## Conclusion

This project successfully demonstrates large-scale, real-time frequent itemset mining on the Amazon Metadata Dataset using cutting-edge streaming algorithms. Through the seamless integration of **Apriori**, **PCY**, and **Bloom filter** methods combined with a **Sliding Window** model, the system dynamically uncovers meaningful product patterns. The MongoDB backend ensures results are stored efficiently for immediate or future analysis. Finally, automation via a bash script enhances reproducibility and operational simplicity, making this solution practical for production-scale data streaming environments.

---
