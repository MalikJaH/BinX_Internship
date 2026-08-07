# Day 1 - Week 3: Pipelines, Grid Search, and Train/Test Split

In this day of training, I learned how to organize machine learning steps using a **Pipeline**, how to search for better model parameters using **GridSearchCV**, and why separating training and testing data is important.

## Machine Learning Pipeline

I learned how to use a Scikit-learn `Pipeline` to combine multiple steps into one workflow.

In my example, the pipeline contained:

1. `StandardScaler` to scale the features.
2. `KNeighborsClassifier` to train the K-NN model.

Using a pipeline makes the workflow cleaner and ensures that preprocessing and model training are applied in the correct order.

## GridSearchCV

I also learned how to use **GridSearchCV** to search for the best values.

For K-NN, one of the most important parameters is:

`n_neighbors`

Instead of choosing this value manually, I tested values from `1` to `10`.

I used:

`cv = 3`

which means that GridSearchCV used **3-fold cross-validation** for each parameter value.

Since I tested 10 different values of `n_neighbors` with 3 folds, the model was trained approximately:

`10 × 3 = 30 times`

This allows the different parameter values to be compared more reliably than using only one split.

## Train/Test Split

For the hands-on lab, I used the Titanic dataset and separated it into:

* `X` — the input features.
* `y` — the target variable, `Survived`.

I then created an:

* **80% training set**
* **20% test set**

using a fixed `random_state` so the same split can be reproduced.

I also checked the shapes of:

* `X_train`
* `X_test`
* `y_train`
* `y_test`

to make sure the data was split correctly.

## Why the Test Set Must Stay Unseen

One of the most important things I learned is that the model should never train on the test set.

The purpose of the test set is to simulate **new and unseen data**.

If information from the test set is used during training or model selection, the final performance can look better than it really is. This is called **data leakage**.

A proper workflow should be:

`Training Data → Train / Tune Model → Test on Unseen Data`

The test set should only be used after the training and model-selection process is complete.

## Hands-On Lab

For the practical tasks, I completed the following steps:

1. Loaded the Titanic dataset.
2. Separated the features `X` and target `y`.
3. Created an 80/20 train/test split.
4. Checked the shapes of the training and testing data.
5. Explained why the test set must remain unseen during training.
6. Practiced using a machine learning `Pipeline`.
7. Used `GridSearchCV` to search for the best number of neighbors for K-NN.

## What I Learned

This day helped me understand some important parts of the machine learning workflow.

I practiced:

* Scikit-learn Pipelines
* StandardScaler
* K-Nearest Neighbors
* Hyperparameters
* GridSearchCV
* Cross-validation
* Train/test splitting
* Reproducibility using `random_state`
* Data leakage
* Keeping the test set unseen

**Day 1 - Week 3 Completed**
