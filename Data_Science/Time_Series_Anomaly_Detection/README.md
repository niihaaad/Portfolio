# Time Series Anomaly Detection

## 📌 Project Overview

This project focuses on **detecting anomalies in time series data** using historical demand patterns. The goal is to identify unusual or unexpected behaviors that deviate from normal trends, which can be critical for monitoring systems, forecasting reliability, and operational decision-making.

The analysis is performed on the **NYC Taxi Demand dataset** from the Numenta Anomaly Benchmark (NAB), a well-known benchmark for evaluating anomaly detection algorithms on real-world time series data.

---

## 📊 Dataset

* **Source:** Numenta Anomaly Benchmark (NAB)
* **Domain:** New York City taxi demand
* **Granularity:** Time-indexed demand values
* **Columns:**

  * `timestamp` – time of observation
  * `value` – taxi demand

The dataset represents real-world demand patterns influenced by daily, weekly, and seasonal trends, making it well-suited for anomaly detection.

---

## 🔍 Exploratory Data Analysis

Several visualization strategies are used to better understand the structure of the data:

* Hourly, daily, and weekly aggregations
* Rolling statistics to highlight trends and volatility
* Demand patterns by day of week

These steps help distinguish **normal cyclical behavior** from potentially anomalous observations.

---

## 🛠 Feature Engineering

To improve anomaly detection performance, additional features are derived from the raw time series, including:

* Time-based features (hour, day, weekday)
* Rolling averages and statistics
* Aggregated demand metrics

These features provide context that helps models differentiate between seasonal effects and true anomalies.

---

## 🤖 Modeling Approach

The project uses Isolation Forest, an unsupervised anomaly detection algorithm well-suited for high-dimensional and time-based data.

**Why Isolation Forest?**

* Efficient on large datasets

* Does not assume any underlying data distribution

* Explicitly designed to isolate anomalies instead of profiling normal points

**How it works (briefly):**

* Randomly partitions the feature space using decision trees

* Anomalies are isolated faster (with fewer splits) than normal points

* Each observation receives an anomaly score based on average path length

**Key characteristics:**

* Model trained only on normal behavior patterns

* Each data point receives an anomaly score

* Lower scores indicate potential anomalies

The sensitivity of anomaly detection is controlled through a configurable threshold, allowing trade-offs between false positives and missed anomalies.

---

## 📈 Results & Visualization

* Anomaly scores are plotted over time
* Detected anomalies are highlighted on top of the demand curve
* Threshold tuning demonstrates how detection sensitivity affects results

This visual inspection is essential for validating whether detected anomalies are meaningful or noise-driven.

---

## ⚖️ Design Choices

* Unsupervised learning due to lack of labeled anomalies
* Multiple time-scale visualizations to avoid misclassification of seasonal spikes
* Threshold-based filtering for interpretability and flexibility

---


## 🚀 Future Improvements

* Compare multiple anomaly detection algorithms
* Incorporate domain-informed labeling for evaluation
* Automate threshold selection
* Extend to multivariate time series

---

## 🧰 Tech Stack

* Python
* NumPy, Pandas
* Scikit-learn
* Matplotlib / Seaborn
* Jupyter Notebook

---



## 📝 Conclusion

This project demonstrates an end-to-end workflow for **time series anomaly detection**, from exploratory analysis to feature engineering, modeling, and interpretation. It highlights the importance of understanding temporal patterns before applying machine learning models.



