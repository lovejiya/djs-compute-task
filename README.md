#Asthma Prediction Using Machine Learning

This project has 2 set of codes, one using encoding with one_hot and other using label

Project Overview

This project aims to predict whether a patient has asthma based on various health and lifestyle factors. The dataset contains both numeric features (e.g., Age, BMI) and categorical features (e.g., Gender, Smoking Status, Comorbidities).

Machine learning models used in this project:

Logistic Regression

Support Vector Machine (SVM)

Random Forest Classifier


Target Variable:

Has_Asthma (0 = No, 1 = Yes)

Preprocessing Steps

Handle Missing Values

Fill or remove missing data for both numeric and categorical features.

One-Hot/label Encoding of Categorical Features
Ordinal Encoding of the rest features

Categorical variables are converted to numeric using OneHotEncoder/label encoder.

drop='first' is used to avoid multicollinearity for linear models.

Scaling Numeric Features

Continuous features are scaled using StandardScaler.

Scaling is essential for distance-based models like SVM and improves convergence for Logistic Regression.

Combine Features

Numeric and encoded categorical features are combined into a single dataset for training.

Model Training

Logistic Regression: Used as a linear baseline model.

SVM (RBF Kernel): Captures non-linear patterns in the data.

Random Forest: Tree-based ensemble model that handles non-linearities and feature interactions.

Training Process:

Split the dataset into training (80%) and testing (20%) sets.

Fit each model on the training set.

Evaluate using accuracy score on the test set.

Random Forest had the best accuracy so we used it as a final model

Making a condusion matrix and accuracy report to show the results for data visualization

