# Sherktna - شركتنا

### Smart E-Commerce Analytics & AI System

Sherketna is an end-to-end **Data Analytics and Artificial Intelligence project** built around a simulated e-commerce company.

The project follows the complete data-to-decision pipeline, starting from raw business data and ending with **AI-powered predictions and business recommendations**.

---

## 📌 Project Overview

E-commerce companies generate large amounts of data from customers, products, orders, and reviews.

The goal of **Sherketna** is to transform this raw data into meaningful business insights and intelligent decisions using:

* Data Cleaning
* Exploratory Data Analysis
* SQL
* Excel
* Power BI
* Statistics
* Machine Learning
* Neural Networks
* Expert Systems

The project is designed as a practical implementation of the skills learned throughout my **Data Analysis and AI learning journey**.

---

## 🎯 Business Problem

Sherketna has a large amount of customer and sales data, but raw data alone cannot answer important business questions.

The company needs a system that can:

* Understand its sales performance
* Identify its best-selling products
* Understand customer behavior
* Identify valuable customers
* Detect customers who may stop purchasing
* Predict customer churn
* Convert AI predictions into actionable business recommendations

---

## ❓ Business Questions

The project aims to answer questions such as:

### Sales

* What is the total revenue?
* How does revenue change over time?
* Which countries generate the highest revenue?
* Which products generate the most revenue?
* Which product categories perform best?

### Customers

* Who are the most valuable customers?
* How frequently do customers purchase?
* What is the average customer spending?
* Which customers are at risk of churn?

### Products

* What are the best-selling products?
* Which products generate the highest revenue?
* Which products have low performance?

### Reviews

* What is the average review score?
* Is there a relationship between customer reviews and purchasing behavior?

---

# 🔄 Project Architecture

```text
                    Raw Data
                       │
                       ▼
              Data Cleaning
              Python / Pandas
                       │
                       ▼
                 Clean Data
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        Excel         SQL       Python EDA
          │            │            │
          └────────────┼────────────┘
                       ▼
              Statistics & EDA
                       │
                       ▼
                Power BI
                       │
                       ▼
             Business Insights
                       │
                       ▼
            Machine Learning
                       │
                       ▼
             Neural Network
                       │
                       ▼
              Expert System
                       │
                       ▼
         Business Recommendations
```

---

# 📊 Dataset

The project uses e-commerce data organized into several related tables.

| Dataset     | Description                     |
| ----------- | ------------------------------- |
| Customers   | Customer information            |
| Products    | Product information             |
| Orders      | Customer orders                 |
| Order Items | Products included in each order |
| Reviews     | Customer reviews and ratings    |

### Data Preparation

The raw datasets will be cleaned and prepared before analysis.

The cleaning process includes:

* Handling missing values
* Removing duplicate records
* Correcting data types
* Detecting invalid values
* Handling inconsistent data
* Detecting potential outliers
* Creating useful features
* Validating the final dataset

---

# 🧹 Data Cleaning

Data cleaning will be performed using **Python and Pandas**.

The main objectives are:

1. Understand the structure of the datasets.
2. Identify data quality problems.
3. Clean and transform the data.
4. Create useful analytical features.
5. Export clean datasets for further analysis.

Main notebook:

```text
notebooks/01_data_cleaning.ipynb
```

---

# 🔎 Exploratory Data Analysis

Exploratory Data Analysis will be performed using:

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Statistics

The analysis will follow a:

> **Question → Analysis → Visualization → Insight**

approach.

Example:

```text
Business Question
        ↓
Data Analysis
        ↓
Visualization
        ↓
Business Insight
```

Main notebook:

```text
notebooks/02_eda.ipynb
```

---

# 🗄️ SQL Analysis

SQL will be used to analyze the cleaned e-commerce data and answer business questions.

Examples include:

* Total revenue
* Revenue by country
* Top customers
* Top products
* Monthly sales
* Customer purchase frequency
* Ranking products and customers
* Customer-level aggregations

SQL files:

```text
sql/schema.sql
sql/analysis_queries.sql
```

---

# 📗 Excel Analysis

Excel will be used for additional data analysis and dashboarding.

The Excel analysis will include:

* Pivot Tables
* Charts
* KPIs
* Sales analysis
* Customer analysis
* Product analysis

File:

```text
excel/sales_analysis.xlsx
```

---

# 📈 Power BI Dashboard

Power BI will be used to create interactive dashboards for business decision-making.

The dashboard will focus on:

### Sales Overview

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value
* Revenue Trends

### Product Analysis

* Top Products
* Product Categories
* Product Revenue

### Customer Analysis

* Customer Spending
* Customer Activity
* Customer Segmentation

### Geographic Analysis

* Revenue by Country
* Orders by Country

Power BI file:

```text
powerbi/Smart_Ecommerce_Analytics.pbix
```

---

# 🤖 Machine Learning

One of the main AI problems in Sherketna is **Customer Churn Prediction**.

## Business Problem

Customer churn occurs when a customer stops purchasing from the company.

The goal is to build a machine learning model that predicts whether a customer is likely to churn.

### Example Features

Potential features include:

* Total Spending
* Number of Orders
* Average Order Value
* Days Since Last Purchase
* Average Review Score
* Purchase Frequency
* Discount Usage

### Target

```text
Churn
0 → Customer is not likely to churn

1 → Customer is likely to churn
```

---

# 🧠 Machine Learning Models

Different machine learning models will be trained and compared.

Possible models include:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost

The models will be evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

The final model will be selected based on both **model performance and business usefulness**.

Main notebook:

```text
notebooks/03_churn_prediction.ipynb
```

---

# 🧠 Neural Network

A Neural Network will also be developed to solve the churn prediction problem.

The Neural Network will be compared with traditional Machine Learning models.

The comparison will help answer:

> Does a Neural Network provide better performance for this business problem?

The trained model will be stored in:

```text
models/neural_network.keras
```

---

# 🧩 Expert System

The project will combine Machine Learning predictions with an **Expert System**.

The Machine Learning model provides a prediction, while the Expert System converts that prediction into a business action.

### Example

```text
Customer Data
      ↓
Machine Learning Model
      ↓
Churn Probability = 82%
      ↓
Expert System
      ↓
Risk Level = HIGH
      ↓
Business Recommendation
      ↓
Send Retention Campaign
```

Example rules:

```text
IF churn_probability > 0.75
AND customer_value = HIGH
THEN recommend_priority_retention_campaign
```

The Expert System is implemented using rule-based reasoning.

Files:

```text
expert_system/
├── rules.py
└── recommendations.py
```

---

# 💡 Business Recommendations

The final system will transform analytical and AI results into business recommendations.

Examples include:

* Launch retention campaigns for high-risk customers.
* Prioritize high-value customers.
* Investigate low-performing products.
* Focus marketing efforts on high-performing categories.
* Create personalized offers.
* Improve customer experience based on review patterns.

The final recommendations will be based on **actual results obtained from the dataset**, rather than predefined assumptions.

---

# 📁 Project Structure

```text
Sherketna/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   ├── order_items.csv
│   │   └── reviews.csv
│   │
│   └── cleaned/
│       ├── customers_clean.csv
│       ├── products_clean.csv
│       ├── orders_clean.csv
│       ├── order_items_clean.csv
│       └── reviews_clean.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_churn_prediction.ipynb
│
├── python/
│   ├── data_cleaning.py
│   ├── data_analysis.py
│   └── feature_engineering.py
│
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── excel/
│   └── sales_analysis.xlsx
│
├── powerbi/
│   └── Smart_Ecommerce_Analytics.pbix
│
├── models/
│   ├── churn_model.pkl
│   └── neural_network.keras
│
├── expert_system/
│   ├── rules.py
│   └── recommendations.py
│
├── screenshots/
│   ├── excel_dashboard.png
│   ├── powerbi_overview.png
│   ├── customer_dashboard.png
│   └── product_dashboard.png
│
└── reports/
    ├── data_quality_report.md
    ├── eda_findings.md
    └── model_evaluation.md
```

---

# 🛠️ Technologies & Tools

### Programming & Data Analysis

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn

### Databases

* SQL

### Business Intelligence

* Microsoft Excel
* Power BI
* DAX
* Power Query

### Machine Learning

* Scikit-learn
* XGBoost

### Deep Learning

* TensorFlow
* Keras

### AI

* Neural Networks
* Expert Systems

### Version Control

* Git
* GitHub

---

# 📚 Learning Approach

Sherketna is being developed as a **learning-by-building project**.

Instead of studying each technology separately, every new concept will be applied directly to the project.

For example:

```text
Pandas groupby
      ↓
Revenue by Country

SQL Window Functions
      ↓
Top Customers per Country

Power BI / DAX
      ↓
Revenue Growth Dashboard

Machine Learning
      ↓
Churn Prediction

Neural Network
      ↓
Model Comparison

Expert System
      ↓
Business Recommendation
```

This approach connects theoretical knowledge with a complete real-world workflow.

---

# 📌 Project Status

The project is being developed incrementally.

### Current Roadmap

* [ ] Dataset Collection
* [ ] Project Setup
* [ ] Data Cleaning
* [ ] Exploratory Data Analysis
* [ ] Statistical Analysis
* [ ] SQL Analysis
* [ ] Excel Dashboard
* [ ] Power BI Dashboard
* [ ] Feature Engineering
* [ ] Machine Learning
* [ ] Neural Network
* [ ] Expert System
* [ ] Business Recommendations
* [ ] Final Documentation

---

# 🚀 Future Improvements

Possible future extensions include:

* Customer Segmentation
* Recommendation System
* Sentiment Analysis for Reviews
* NLP-based Customer Feedback Analysis
* Real-Time Analytics
* Model Deployment
* REST API using FastAPI
* Cloud Deployment
* Automated Data Pipelines

---

# 👩‍💻 Author

**Rawan Ahmed Elmorsy AbdelHaleem**

Computer Science Student
Cairo University

---

## ⭐ Project Goal

The ultimate goal of **Sherketna** is to demonstrate how raw business data can be transformed into:

```text
Data
 ↓
Information
 ↓
Insights
 ↓
Predictions
 ↓
Intelligent Decisions
```

**Sherketna — From Data to Intelligent Business Decisions.**

