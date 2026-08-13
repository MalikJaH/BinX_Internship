# Day 5 — Tuned End-to-End Pipeline Mini-Project

In this mini-project, I built a complete machine learning workflow using the Titanic dataset.

The main goal was to combine **feature engineering, preprocessing, model training, cross-validation, hyperparameter tuning, and final evaluation** into one clean Scikit-learn pipeline.

This project brings together the main ideas I learned during Week 4 and shows how to build a workflow that avoids data leakage and gives a more reliable estimate of model performance.

## Project Workflow

The complete workflow was:

**Raw Data → Train/Test Split → Feature Engineering → ColumnTransformer → Pipeline → Cross-Validation → GridSearchCV → Best Pipeline → Final Test Evaluation**

The dataset was split into:

* **80% training data**
* **20% held-out test data**

I also used `stratify=y` so that the survival class distribution stayed similar in both sets.

The final split contained:

* **712 training samples**
* **179 test samples**

## Preprocessing

I used `ColumnTransformer` to handle numeric and categorical columns differently.

### Numeric Features

The numeric features were:

* `Age`
* `SibSp`
* `Parch`
* `Fare`
* `FamilySize`

For these features, I used:

1. `SimpleImputer(strategy="median")`
2. `StandardScaler()`

### Categorical Features

The categorical features were:

* `Pclass`
* `Sex`
* `Embarked`

For these features, I used:

1. `SimpleImputer(strategy="most_frequent")`
2. `OneHotEncoder(handle_unknown="ignore")`

Keeping preprocessing inside the pipeline means that the imputer, scaler, and encoder are fitted only on the training portion of each cross-validation fold.

This helps prevent data leakage.

## Feature Engineering

I reused the `FamilySize` feature from Day 4.

```text
FamilySize = SibSp + Parch + 1
```

This feature represents the total number of family members traveling together, including the passenger.

The columns that were not used by the model were:

* `PassengerId`
* `Name`
* `Ticket`
* `Cabin`

## Baseline Model

Before tuning, I evaluated an untuned `RandomForestClassifier` using **5-fold stratified cross-validation**.

The baseline fold F1 scores were:

```text
0.7273
0.7273
0.7547
0.7027
0.7200
```

The baseline results were:

* **Mean F1:** `0.7264`
* **Standard deviation:** `0.0168`

This gave me a starting point to compare against the tuned model.

## Hyperparameter Tuning

I used `GridSearchCV` to tune the complete pipeline.

The Random Forest parameters tested were:

```python
n_estimators = [100, 200, 300]
max_depth = [5, 10, None]
min_samples_leaf = [1, 2, 4]
```

The search used:

* **5-fold cross-validation**
* **F1 score**
* the complete preprocessing and modeling pipeline

Because the model was inside a pipeline step called `model`, the parameters were written using names such as:

```text
model__n_estimators
model__max_depth
model__min_samples_leaf
```

## Best Model

The best parameters found by `GridSearchCV` were:

```text
n_estimators = 100
max_depth = None
min_samples_leaf = 2
```

The best mean cross-validation F1 score was:

```text
0.7573
```

Compared with the baseline CV F1 of `0.7264`, tuning improved the cross-validation score by approximately:

```text
+0.0309
```

## Final Test Evaluation

After all model-selection decisions were complete, I evaluated the best pipeline once on the held-out test set.

The final results were:

| Metric         |  Score |
| -------------- | -----: |
| Baseline CV F1 | 0.7264 |
| Best CV F1     | 0.7573 |
| Test Accuracy  | 0.7989 |
| Final Test F1  | 0.7143 |

The classification report showed:

* F1 of about **0.84** for class `0`
* F1 of about **0.71** for class `1`

The final test F1 was lower than the best cross-validation F1, but this is possible because the test set contains completely unseen examples.

The test set was not used for tuning, so the final score gives a more honest estimate of how the selected model generalizes to new data.

## What I Learned

This mini-project helped me understand how the different parts of a machine learning workflow work together.

The main lessons were:

* `Pipeline` can combine preprocessing and modeling into one object.
* `ColumnTransformer` can apply different preprocessing steps to different column types.
* preprocessing should happen inside the pipeline to reduce the risk of data leakage.
* cross-validation gives a more stable estimate than one validation split.
* `GridSearchCV` can tune parameters inside a complete pipeline.
* hyperparameters inside a pipeline use names such as `model__max_depth`.
* feature engineering can improve the information available to the model.
* the test set should remain untouched until the final evaluation.
* the best training or cross-validation score does not guarantee the same performance on unseen test data.
* generalization is more important than simply getting the highest possible training score.

## Final Result

The untuned pipeline started with a mean cross-validation F1 score of **0.7264**.

After tuning, the best cross-validation F1 increased to **0.7573**.

The final selected pipeline achieved:

* **79.89% test accuracy**
* **0.7143 test F1**

Overall, this mini-project gave me a better understanding of how to build a complete, reusable, and leak-free machine learning workflow using Scikit-learn.
