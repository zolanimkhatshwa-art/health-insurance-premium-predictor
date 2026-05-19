# Health Insurance Premium Predictor
### An End-to-End Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.8.0-orange?style=flat&logo=scikit-learn)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat&logo=flask)

---

## Overview

This project builds a machine learning model that predicts a customer's annual health insurance premium based on their demographic and lifestyle information.

---

## Business Problem

Health insurance companies need to accurately price premiums to remain profitable. This model helps insurers:

- Estimate the appropriate annual premium for a new customer
- Classify customers into risk tiers (Low, Medium, High)
- Understand which factors drive premium costs the most

---

## Dataset

**Source:** [US Health Insurance Dataset - Kaggle](https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset)

- 1,338 records
- Features: age, sex, bmi, children, smoker, region
- Target: charges (annual premium)

---

## Model Comparison

| Model | MAE | R2 Score |
|---|---|---|
| Linear Regression | $4,186.51 | 0.7833 |
| Random Forest | $2,533.67 | 0.8643 |
| **Gradient Boosting** | **$2,447.95** | **0.8780** |

---

## Feature Importance

1. **Smoker status** - biggest driver of high premiums
2. **Age** - older customers attract higher charges
3. **BMI** - higher BMI linked to chronic health conditions
4. **Children** - more dependants slightly increases premiums
5. **Region** - minor geographic cost differences
6. **Sex** - least influential factor

---

## Key Business Insights

- Smokers are charged on average 3-4x more than non-smokers
- Customers over 50 with high BMI who smoke fall in the High Risk tier
- Gender has minimal impact on premiums
- Southeast region shows slightly higher average charges

---

## How To Run Locally

1. Clone the repository
2. Install dependencies: pip install pandas numpy matplotlib seaborn scikit-learn flask
3. cd flaskapp
4. python app.py
5. Open http://127.0.0.1:5000

---

## Sample Prediction

Input: 45-year-old male smoker, BMI 28.5, 2 children, Northeast region

Estimated Annual Premium: $26,187.59 | Risk Tier: High Risk

---

## Technologies Used

| Tool | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Pandas and NumPy | Data manipulation |
| Matplotlib and Seaborn | Data visualisation |
| Scikit-Learn | Model building and evaluation |
| Flask | Web application framework |

---

## Author

**Zolani Mkhatshwa**
GitHub: [@zolanimkhatshwa-art](https://github.com/zolanimkhatshwa-art)

---

## Acknowledgements

- Dataset: [Teertha Biswas - Kaggle](https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset)
- Inspired by: [IBM Telco Customer Churn on ICP4D](https://github.com/IBM/telco-customer-churn-on-icp4d)

---

## Live Demo

**Deployed on AWS Elastic Beanstalk:**

http://health-insurance-env.eba-xxxxxxxx.us-east-1.elasticbeanstalk.com

---

## Live Demo

**Deployed on AWS Elastic Beanstalk:**

http://health-insurance-env.eba-gsunhtm6.us-east-1.elasticbeanstalk.com/
