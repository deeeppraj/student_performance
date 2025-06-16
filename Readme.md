# Student Exam Performance Indicator

A machine learning project that predicts a student’s **Math score** based on various demographic and academic factors using Python, scikit-learn pipelines, and Flask for a web interface.

---

## Project Overview

This project takes input features such as gender, race/ethnicity, parental level of education, lunch type, test preparation course status, reading score, and writing score to predict the math exam performance of students. It uses data preprocessing pipelines to handle both numerical and categorical data efficiently and then trains a regression model for prediction.

---

## Features

- Data preprocessing using scikit-learn Pipelines (handling missing values, encoding categorical variables, scaling features)
- Modular Python classes with custom exception handling and logging
- Model training, saving, and loading functionality
- Flask web app for users to enter student data and get instant math score predictions
- Clean and maintainable code structure

---

## Tech Stack

- Python 3.12 
- pandas, NumPy  
- scikit-learn  
- Flask  
- dill (for object serialization)

---

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed.  
Install required packages using:

```bash
pip install -r requirements.txt


'''
Hosted on : Azure
website : https://student-performance-epe5gsatfxafbsaq.centralus-01.azurewebsites.net/predictdata