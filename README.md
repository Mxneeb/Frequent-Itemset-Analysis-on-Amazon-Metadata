# Amazon Metadata Streaming and Frequent Itemset Mining

## Project Overview

This project utilizes the **Amazon Metadata Dataset** to build a real-time streaming pipeline for frequent itemset mining. The system employs a producer-consumer architecture to process data streams efficiently. Key features include implementing the **Apriori**, **PCY**, and **Bloom’s algorithms**, integrating a **Sliding Window** approach, and storing results in a **MongoDB** database. Additionally, a **bash script** simplifies project execution by initializing all components.

---

## Dataset Description

The dataset contains detailed product metadata in JSON format, with fields such as:

- **asin**: Product ID (e.g., `0000031852`).
- **title**: Name of the product.
- **feature**: Bullet-point format features of the product.
- **description**: Product description.
- **price**: Price in US dollars (at the time of crawl).
- **imageURL**: URL of the product image.
- **related**: Related products (e.g., "also bought," "also viewed").
- **salesRank**: Sales rank information.
- **brand**: Brand name.
- **categories**: List of categories the product belongs to.
- **similar**: Similar product table.

**Note:** The dataset expands from **12GB** to **105GB** upon extraction. A sampled version of at least **15GB** is required for analysis.

---

## Methodology

### 1. **Dataset Management**
- **Downloading and Extraction**: The Amazon Metadata dataset was downloaded and expanded to its full size.
- **Sampling**: A sample of at least **15GB** was created for processing.

---

### 2. **Preprocessing**
- Redundant columns were removed from the dataset to improve performance.
- Cleaned and formatted the data for analysis.
- Generated a new JSON file containing preprocessed data.
- **Bonus**: Batch processing was implemented to enable real-time preprocessing.

---

### 3. **Streaming Pipeline Setup**
- A **Producer Application** streams preprocessed data in real time.
- Three **Consumer Applications** subscribe to the producer’s data stream and process the data:
  1. **Consumer 1**: Implements the **Apriori algorithm** to mine frequent itemsets and prints real-time insights.
  2. **Consumer 2**: Implements the **PCY algorithm** for frequent itemset mining with real-time feedback.
  3. **Consumer 3**: Implements the **Bloom's algorithm** using the **Sliding Window** approach for innovative analysis.

---

### 4. **Frequent Itemset Mining**
- Adapted the Apriori and PCY algorithms for a streaming environment using:
  - **Sliding Window Approach**
  - **Approximation Techniques**
  - **Incremental Processing**
  - **Decaying Factor**
  - **Online Algorithms**
- Innovations in **Consumer 3** were designed to maximize marks with creative and advanced data analysis.

---

### 5. **Database Integration**
- Results from all consumers are stored in a **MongoDB** database for efficient querying and future analysis.

---

### 6. **Execution Simplification**
- A **Bash Script** automates the setup and execution of:
  - Kafka components (Producer, Consumers, Zookeeper, Kafka Connect, etc.)
  - Initialization of all required configurations.

---

## Step-by-Step Guide to Execution

### 1. Environment Setup
1.1 **Install Required Tools**
- Install Kafka, MongoDB, and any necessary dependencies.
- Ensure Python 3.x and libraries like `pandas` and `json` are installed.

1.2 **Prepare the Dataset**
- Download, extract, and sample the dataset to at least 15GB.

---

### 2. Code Setup
2.1 **Producer Application**
- Stream preprocessed data from the JSON file.

2.2 **Consumers**
- Each consumer subscribes to the producer's stream and applies its respective algorithm.

2.3 **Database Configuration**
- Update MongoDB configurations in the code to match your setup.

---

### 3. Bash Script Execution
- Use the provided bash script to:
  - Start Zookeeper and Kafka services.
  - Initialize the producer and all consumers.
  - Set up MongoDB connections.

---

## Results and Findings

### 1. Frequent Itemset Mining
- **Apriori** and **PCY algorithms** provided real-time insights into frequent itemsets.
- **Bloom’s algorithm** effectively managed sliding window operations for high-velocity data streams.

### 2. Database Integration
- MongoDB stored results efficiently, allowing seamless querying and data analysis.

### 3. Streamlining Execution
- The bash script significantly reduced manual effort in initializing and managing components.

---

## Conclusion

This project demonstrates the application of frequent itemset mining in a streaming context using real-world, large-scale data. By leveraging algorithms like **Apriori**, **PCY**, and **Bloom’s**, along with a **Sliding Window** approach, the system efficiently handles high-velocity data streams. The use of MongoDB ensures scalability and effective storage of results. The inclusion of a bash script further enhances usability and reproducibility. 

---
