# Day 3 - Week 3: Logistic Regression and Classification Metrics

In this day of training, I learned more about **Logistic Regression** and how it is used for binary classification problems.

I used the Titanic dataset to predict whether a passenger survived or not and learned how to evaluate a classification model using different metrics.

## Logistic Regression

Logistic Regression is mainly used for **classification problems**.

Unlike Linear Regression, which predicts continuous numerical values, Logistic Regression predicts the probability that a sample belongs to a certain class.

For the Titanic dataset:

* `0` means the passenger did not survive.
* `1` means the passenger survived.

I trained a Logistic Regression model and used it to generate both class predictions and survival probabilities.

## Data Preparation

Before training the model, I prepared the Titanic dataset by:

* Removing unnecessary columns:

  * `PassengerId`
  * `Name`
  * `Ticket`
  * `Cabin`
* Handling missing values in `Age`.
* Converting categorical features into numerical values using one-hot encoding.
* Separating the target `Survived` from the input features.
* Splitting the data into training and testing sets.

## Confusion Matrix

I learned how to use a **Confusion Matrix** to understand the predictions made by the model.

It contains four important values:

* **True Positive (TP)** — predicted positive and actually positive.
* **True Negative (TN)** — predicted negative and actually negative.
* **False Positive (FP)** — predicted positive but actually negative.
* **False Negative (FN)** — predicted negative but actually positive.

The confusion matrix helped me understand the types of mistakes the model was making instead of looking only at the overall accuracy.

## Precision vs Recall

One of the main topics I focused on was understanding the difference between **Precision** and **Recall**.

### Precision

Precision tells us how many of the positive predictions made by the model were actually correct.

For example, if the model predicts 8 passengers as survivors but only 6 actually survived, the precision would be:

`6 / 8 = 0.75`

So Precision focuses on the reliability of the model's positive predictions.

### Recall

Recall tells us how many of the actual positive cases the model was able to find.

In simple words:

**Recall = Positive cases found / Total actual positive cases**

For the Titanic problem, recall can be important because it tells us how many of the actual survivors were successfully identified by the model.

## Model Evaluation

I evaluated the Logistic Regression model using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Classification Report
* AUC-ROC

The model achieved around **81% accuracy**.

For the survivor class, it achieved approximately:

* **Precision:** 0.79
* **Recall:** 0.74
* **F1-score:** 0.76

This showed that the model performed reasonably well, although it still missed some actual survivors.

## AUC-ROC

I also learned about the **AUC-ROC score**, which measures how well a classification model can distinguish between the two classes.

The Logistic Regression model achieved an AUC score of approximately **0.88**.

Since:

* `0.5` represents performance similar to random guessing.
* `1.0` represents perfect separation.

An AUC of `0.88` shows that the model has a good ability to distinguish between passengers who survived and those who did not.

## Hands-On Lab

For the practical tasks, I completed the following steps:

1. Loaded and prepared the Titanic dataset.
2. Trained a Logistic Regression model.
3. Generated class predictions and survival probabilities.
4. Created and interpreted the confusion matrix.
5. Calculated Precision, Recall, and F1-score using `classification_report`.
6. Compared Precision and Recall and understood when each metric is important.
7. Decided that Recall can be more important for identifying survivors in this specific example.
8. Calculated the AUC-ROC score and interpreted the model's ability to separate the two classes.

## What I Learned

This day helped me better understand how classification models are evaluated.

I practiced:

* Logistic Regression
* Binary classification
* Confusion Matrix
* True Positive and True Negative
* False Positive and False Negative
* Accuracy
* Precision
* Recall
* F1-score
* Classification Report
* Probability predictions
* AUC-ROC
* Interpreting model performance

**Day 3 - Week 3 Completed**
