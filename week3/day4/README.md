# Day 4 - Week 3: Classification Models Comparison

In this day of training, I learned about several important machine learning classification algorithms and compared how they perform on the Titanic dataset.

The main models I studied were:

* **Decision Tree**
* **Random Forest**
* **Support Vector Machine (SVM)**
* **K-Nearest Neighbors (K-NN)**

## Decision Tree

I learned that a Decision Tree works like a flowchart and makes predictions by asking a sequence of questions about the data.

A Decision Tree consists of:

* **Root Node** — the first decision or condition.
* **Internal Nodes** — additional questions used to split the data.
* **Branches** — the possible answers to each condition.
* **Leaf Nodes** — the final prediction.

Decision Trees can be used for both classification and regression.

One of their main advantages is that they usually do not require feature scaling. However, one of their biggest disadvantages is that they can easily suffer from **overfitting**.

## Random Forest

Random Forest combines many Decision Trees instead of relying on only one.

Each tree makes its own prediction, and the final classification is usually decided by voting across all trees.

I learned that Random Forest:

* Can reduce the overfitting problem found in individual Decision Trees.
* Can capture complex and nonlinear relationships.
* Usually produces more stable predictions.
* Can show which features are most important using `feature_importances_`.

Some disadvantages are that it can be slower, require more memory, and be more complex than a single Decision Tree.

## Support Vector Machine (SVM)

SVM tries to find the best decision boundary that separates different classes while keeping the largest possible margin between them.

I learned about two important SVM parameters:

* **C**

  * A large value tries harder to classify training samples correctly but can increase the risk of overfitting.
  * A smaller value allows more mistakes and can improve generalization.

* **Gamma**

  * A large value can produce a more complex decision boundary.
  * A small value produces a smoother decision boundary.

I also learned that SVM usually requires **feature scaling** and can become slow when working with large datasets.

## K-Nearest Neighbors (K-NN)

K-NN classifies a new data point based on the classes of its nearest neighbors.

The value of **K** represents how many neighboring points are considered when making the prediction.

Because K-NN relies on calculating distances between points, feature scaling is very important.

## Hands-On Lab

For the practical tasks, I used the Titanic dataset and trained all four models using the same train/test split.

I completed the following steps:

1. Prepared the Titanic dataset by removing unnecessary columns, handling missing values, and converting categorical features into numerical values.

2. Trained:

   * Decision Tree
   * Random Forest
   * SVM
   * K-NN

3. Applied `StandardScaler` to the features used by SVM and K-NN because both models depend on distances or feature magnitudes.

4. Generated predictions for all four models.

5. Evaluated every model using the same **F1-score** metric.

6. Created a comparison table and sorted the models according to their F1-score.

7. Used the Random Forest model to identify the most important features in the Titanic dataset.

8. Identified the best-performing model and explained why it achieved the strongest result.

## Best-Performing Model

In my experiment, **Random Forest** achieved the highest F1-score among the four models.

It likely performed better because it combines predictions from multiple Decision Trees, which makes the model more stable and helps reduce overfitting.

It can also learn complex and nonlinear relationships between the passenger features and survival outcome.

## What I Learned

This day helped me understand the differences between several popular classification algorithms and when feature scaling is important.

I practiced:

* Decision Trees
* Random Forests
* Support Vector Machines
* K-Nearest Neighbors
* Feature scaling with `StandardScaler`
* Model training and prediction
* F1-score evaluation
* Comparing multiple models fairly
* Feature importance
* Overfitting and generalization
* Selecting the best-performing model
