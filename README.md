# 🚀 Amazon Metadata Streaming and Frequent Itemset Mining 📊

## 🔍 Project Overview

This project leverages the **Amazon Metadata Dataset** to build a powerful, real-time streaming pipeline for **frequent itemset mining**. Using a producer-consumer architecture, the system efficiently processes massive data streams by applying advanced algorithms like **Apriori**, **PCY**, and **Bloom filters**. The use of a **Sliding Window** approach ensures timely, incremental insights, while results are stored in a **MongoDB** database for scalable and fast querying. To top it off, an all-in-one **bash script** automates setup and execution for maximum convenience. 🎉

---

## 📦 Dataset Description

The dataset contains rich product metadata in JSON format, including:

- 🆔 **asin**: Unique product identifier (e.g., `0000031852`)
- 🏷️ **title**: Product name
- ✨ **feature**: Bullet-point product features
- 📝 **description**: Detailed product description
- 💲 **price**: Price in US dollars (at crawl time)
- 🖼️ **imageURL**: Product image URL
- 🔗 **related**: Related products ("also bought", "also viewed")
- 📊 **salesRank**: Sales rank info
- 🏭 **brand**: Brand name
- 🗂️ **categories**: Product categories
- 🔄 **similar**: Similar product listings

> ⚠️ **Note:** Original compressed dataset is **12GB**, expanding to **105GB** upon extraction. A sampled subset of at least **15GB** is used for efficient analysis.

---

## 🛠️ Methodology

### 1. Dataset Management
- 📥 Downloaded & extracted full dataset.
- 🔍 Sampled a **15GB+** subset for processing efficiency.

---

### 2. Data Preprocessing
- 🗑️ Removed redundant columns to speed up processing.
- 🧹 Cleaned and normalized data for consistency.
- 💾 Exported a new preprocessed JSON file.
- ⚡ **Bonus:** Batch preprocessing to simulate real-time streaming.

---

### 3. Streaming Pipeline Architecture
- 🎥 **Producer Application**: Streams preprocessed JSON data into Kafka topics.
- 👥 **Consumers (3 total)**:
  1. **Consumer 1**: Runs the **Apriori algorithm** to discover frequent itemsets in real time.
  2. **Consumer 2**: Applies the **PCY algorithm** using hash-based bitmap compression for efficient mining.
  3. **Consumer 3**: Uses **Bloom filter** enhanced with a **Sliding Window** approach for dynamic temporal pattern detection.

---

### 4. Frequent Itemset Mining Techniques
- ⚙️ Adapted Apriori and PCY algorithms for streaming with:
  - 🕰️ **Sliding Window Model**: Focus on the freshest data.
  - 🔄 **Incremental Updates & Approximation**: Real-time, low-latency mining.
  - ⏳ **Decay Factor**: Older data weighted less for current trends.
  - 🌐 **Online Algorithms**: Continuous, seamless data processing.
- 💡 Consumer 3 innovates with Bloom filters + sliding windows for novel insights.

---

### 5. Database Integration
- 🗃️ All mining results are pushed live to a **MongoDB** database.
- 🚀 MongoDB schema optimized for rapid querying and future extensibility.

---

### 6. Execution Automation
- 🐚 A **bash script** automates:
  - ⚙️ Kafka & Zookeeper startup.
  - ▶️ Producer and all consumer services launch.
  - 🛢️ MongoDB initialization and config.
- 🔄 Ensures smooth, repeatable deployments with one command.

---

## ⚙️ Step-by-Step Guide to Execution

### 1. Environment Setup
1.1 **Install Prerequisites**
- ⚡ Kafka + Zookeeper latest versions.
- 🗄️ MongoDB configured on default ports.
- 🐍 Python 3.x + libraries (`pandas`, `json`, `kafka-python`, `pymongo`).

1.2 **Prepare Dataset**
- 📥 Download, extract, and sample Amazon Metadata dataset (≥15GB).

---

### 2. Code Setup
2.1 **Producer Application**
- Streams preprocessed JSON into Kafka topics.

2.2 **Consumers**
- Subscribe to Kafka and process data with their algorithms.
- Configure MongoDB connection parameters.

---

### 3. Run Everything with Bash Script
- 🔥 Run the bash script to:
  - Start Zookeeper & Kafka.
  - Launch Producer and Consumers.
  - Setup MongoDB connections.

---

## 📈 Results and Findings

### 1. Real-Time Frequent Itemset Mining
- ⚡ Apriori and PCY delivered instant, actionable insights on frequent co-occurring product features.
- 🌊 Bloom filter + Sliding Window consumer handled high-speed streams while capturing temporal shifts in trends.

### 2. Database Efficiency
- 💾 MongoDB stored results efficiently, enabling fast querying and multi-dimensional analysis.

### 3. Operational Simplicity
- 🎯 Bash script cut down manual setup time drastically.
- ⏱️ Achieved real-time mining with low latency.

---

## 🎯 Conclusion

This project showcases how to apply cutting-edge frequent itemset mining algorithms on large-scale, high-velocity data streams like Amazon Metadata. By combining **Apriori**, **PCY**, and **Bloom filters** with a smart **Sliding Window** model, it uncovers meaningful, timely product patterns. The MongoDB backend offers scalable storage and rapid querying, while the automation script maximizes usability and reproducibility. A solid blueprint for production-grade streaming data analytics! 🚀🔥

---
