# 🚗 Predictive Collision Avoidance System

## 📌 Project Overview

The Predictive Collision Avoidance System is a Machine Learning-based application that predicts road accident severity using accident, weather, location, and traffic-related features.

The system analyzes historical accident records and estimates the severity level of a potential accident, helping drivers, transportation agencies, and traffic management systems identify high-risk situations and take preventive measures.

The project follows a complete Machine Learning lifecycle including data preprocessing, feature engineering, model training, evaluation, deployment, and real-time prediction through a Streamlit web application.

---

## 🎯 Problem Statement

Road accidents are one of the major causes of injuries and fatalities worldwide. Factors such as weather conditions, road infrastructure, visibility, traffic signals, and geographical location significantly influence accident severity.

The objective of this project is to develop a predictive system that can estimate accident severity based on various environmental and road-related conditions.

---

## 📊 Dataset Information

**Dataset:** US Accidents Dataset

**Source:** Kaggle

**Original Dataset Size:** 7.7+ Million Records

**Sample Used for Training:** 500,000 Records

### Features Used

* Source
* Start Latitude
* Start Longitude
* Distance
* State
* Timezone
* Temperature
* Wind Chill
* Humidity
* Pressure
* Visibility
* Wind Direction
* Wind Speed
* Precipitation
* Weather Condition
* Road Infrastructure Features
* Time-based Features

### Target Variable

**Severity**

| Severity | Description   |
| -------- | ------------- |
| 1        | Low Risk      |
| 2        | Moderate Risk |
| 3        | High Risk     |
| 4        | Critical Risk |

---

## ⚙️ Project Workflow

### 1. Data Understanding

* Dataset exploration
* Missing value analysis
* Statistical analysis
* Feature inspection

### 2. Data Preprocessing

* Handling missing values
* Removing unnecessary columns
* Data cleaning
* Feature selection

### 3. Feature Engineering

* Hour extraction
* Month extraction
* Day of week extraction
* Weekend identification
* Day/Night identification
* Rush hour detection
* Accident duration calculation

### 4. Encoding

* Label Encoding of categorical variables

### 5. Model Training

* Random Forest Classifier

### 6. Model Evaluation

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

### 7. Deployment

* Streamlit Web Application

---

## 🤖 Machine Learning Model

### Algorithm Used

Random Forest Classifier

### Model Performance

| Metric       | Value             |
| ------------ | ----------------- |
| Accuracy     | 86.11%            |
| Dataset Size | 500,000 Records   |
| Features     | 39                |
| Classes      | 4 Severity Levels |

---

## 📈 Important Features

Top contributing features identified by the Random Forest model:

1. Accident Duration Minutes
2. Start Longitude
3. Start Latitude
4. Source
5. Distance
6. Year
7. Pressure
8. Humidity
9. Temperature
10. Hour

---

## 🖥️ Streamlit Application Features

* Interactive User Interface
* Real-time Severity Prediction
* Risk Classification
* Safety Recommendations
* Project Statistics Sidebar
* Dynamic User Inputs

---

## 📂 Project Structure

```text
Predictive-Collision-Avoidance-System/
│
├── app/
│   ├── app.py
│   ├── predict.py
│   └── utils.py
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_deployment.ipynb
│
├── models/
│
├── data/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/manojyadav1222/Predictive-Collision-Avoidance-System.git
```

### Move into Project Folder

```bash
cd Predictive-Collision-Avoidance-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app/app.py
```

---

## 📸 Application Screenshots

### Home Page

Add screenshot here

### Prediction Results

Add screenshot here

### Project Statistics Sidebar

Add screenshot here

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit
* Git
* GitHub

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Data Cleaning and Preprocessing
* Feature Engineering
* Machine Learning Model Development
* Model Evaluation
* Streamlit Deployment
* Git Version Control
* End-to-End ML Project Development

---

## 👨‍💻 Author

**Manoj Yadav**

B.Tech – Computer Science Engineering (AI & ML)

Sri Venkateswara College of Engineering and Technology,Chittoor

GitHub: https://github.com/manojyadav1222

---

## 📜 License

This project is developed for educational and learning purposes.
