# Day 5 Mini-Project: Titanic Survival Classification

In this mini-project, I built a complete supervised machine learning workflow using the Titanic dataset.

The main goal was to predict whether a passenger survived based on features such as age, sex, passenger class, fare, and family information.

## What I Did

First, I explored the dataset and checked the available columns, missing values, data types, and class distribution.

I removed some columns that were not useful for this small project, such as:

* `PassengerId`
* `Name`
* `Ticket`
* `Cabin`

I also used visualizations to better understand the relationship between survival and features such as:

* Sex
* Passenger class
* Fare

## Data Preprocessing

The dataset was split into training and testing sets before preprocessing.


The preprocessing included:

* Filling missing numerical values using the mean.
* Filling missing categorical values using the most frequent value.
* Converting categorical features using one-hot encoding.
* Standardizing numerical features using `StandardScaler`.

## Models

I compared three classifiers:

1. **Dummy Classifier**

   * Used as a simple baseline.
   * Always predicts the most frequent class.

2. **Logistic Regression**

   * A simple and interpretable model for binary classification.

3. **Random Forest**

   * A more flexible model that can learn nonlinear relationships and interactions between features.

## Model Evaluation

I used **5-fold Stratified Cross-Validation** on the training set to compare the models.

The main evaluation metric was the **F1-score**, because it provides a balance between precision and recall.

I also evaluated the final models using:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

The final model was selected based on the best average cross-validation F1-score, not based on the test set results.

The test set was kept unseen during model selection and was used only for the final evaluation.

## Confusion Matrix

After selecting the final model, I created a confusion matrix to better understand the model's predictions.

The confusion matrix shows:

* True Positives
* True Negatives
* False Positives
* False Negatives

This helped me understand not only how accurate the model was, but also what types of mistakes it made.

## What I Learned

This project helped me understand the complete workflow of a supervised machine learning classification problem.

I practiced:

* Exploratory Data Analysis
* Train/test splitting
* Handling missing values
* One-hot encoding
* Feature scaling
* Cross-validation
* Comparing multiple models
* Using a baseline model
* Classification metrics
* Confusion matrices
* Final model evaluation on unseen data

The most important thing I learned was that the test set should not be used to select the best model. Model selection should be done using the training data and cross-validation, while the test set should remain untouched until the final evaluation.