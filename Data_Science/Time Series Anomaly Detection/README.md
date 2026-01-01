# Time Series Anomaly Detection with Python
 ## 📌Project Overview

This project implements an end-to-end time series anomaly detection pipeline using Python.
The goal is to identify unusual or abnormal patterns in temporal data that deviate from expected system behavior.

The project follows a real-world data science workflow, from data exploration and feature engineering to multiple anomaly detection techniques and evaluation.

 ## 🎯 Problem Statement

Many real-world systems (web traffic, servers, sensors, energy consumption) generate time series data.
Unexpected spikes, drops, or pattern changes may indicate issues such as system failures, fraud, or abnormal usage.

Objective:
Detect anomalous observations in a univariate time series without relying solely on labeled data.

 ## 📊 Dataset Description

**Dataset Characteristics**

  * Each row represents a timestamp

  * The value column represents system behavior (e.g. traffic volume, load, activity level)

  * Data is ordered chronologically

  * The time series may exhibit:

    * Trends

    * Seasonality

    * Noise

**What Is an Anomaly?**

An anomaly is defined as:

  * An unusual spike or drop

  * A sudden deviation from normal temporal patterns

  * A behavior that is inconsistent with recent historical values

This definition guides all modeling and evaluation choices in the project.

## 🧠 Approach

The project is structured into the following steps:

**1- Data Exploration**

  * Time series visualization

  * Identification of trends, seasonality, and irregular patterns

  * Handling missing values and basic cleaning

**2- Feature Engineering**

  * Rolling statistics (mean, standard deviation)

  * Lag-based features

  * Differencing to capture changes over time

**3 -Baseline Methods**

  * Z-score based anomaly detection

  * Interquartile Range (IQR)

**4- Machine Learning Methods**

  * Isolation Forest

  * One-Class SVM

  * Local Outlier Factor (LOF)

**5- Evaluation**

  * Visual inspection of detected anomalies

  * Anomaly score analysis

  * Comparison between different methods

  * Discussion of strengths and limitations

## 🛠️ Technologies Used

* Python 3

* pandas, numpy

* matplotlib, seaborn

* scikit-learn

scipy
