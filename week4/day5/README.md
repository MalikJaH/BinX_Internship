# Day 5 — Tuned End-to-End Pipeline

Today I focused on building a complete machine learning workflow using Scikit-learn pipelines.

The main goal was to combine **feature engineering, preprocessing, model training, and hyperparameter tuning** into one end-to-end pipeline while keeping the evaluation process leak-free.

## What I Learned

I learned how `Pipeline` and `ColumnTransformer` can be used together to handle different types of features correctly.

For the numeric features, I used:

* `SimpleImputer` with the median strategy to handle missing values.
* `StandardScaler` to scale the numeric values.

For the categorical features, I used:

* `SimpleImputer` with the most frequent strategy.
* `OneHotEncoder` to convert categorical values into numerical features.

Keeping these preprocessing steps inside the pipeline makes sure that preprocessing is learned only from the training data during each cross-validation fold.

## Feature Engineering

I also added the engineered features from Day 4 directly into the workflow using `FunctionTransformer`.

The two engineered features were:

* `FamilySize` — the total number of family members traveling with the passenger, including the passenger.
* `IsAlone` — indicates whether the passenger was traveling alone.

The formula used for `FamilySize` was:

```text
FamilySize = SibSp + Parch + 1
```

I also removed `PassengerId`, `Name`, `Ticket`, and `Cabin` because they were not used as model features.

By placing feature engineering inside the pipeline, the complete transformation process stays reusable and organized in one workflow.

## Hyperparameter Tuning

After building the complete pipeline, I used `GridSearchCV` with **5-fold cross-validation** to tune the Random Forest model.

The hyperparameters tested were:

* `n_estimators`: 100, 200, 300
* `max_depth`: 5, 10, None
* `min_samples_leaf`: 1, 2, 4

The tuning process used **F1 score** as the main evaluation metric.

The best parameters were:

```text
max_depth: None
min_samples_leaf: 2
n_estimators: 100
```

The best mean cross-validation F1 score was:

```text
0.75996
```

## Final Evaluation

The held-out test set was kept untouched during feature engineering, preprocessing, and hyperparameter tuning.

At the end, I compared the tuned pipeline with an untuned Random Forest baseline.

### Results

| Model                  | F1 Score |
| ---------------------- | -------: |
| Baseline Random Forest |   0.7132 |
| Tuned Pipeline         |   0.7317 |

The tuned pipeline improved the test F1 score by:

```text
+0.0185
```

This shows that combining feature engineering and hyperparameter tuning improved the model compared with the original untuned baseline.

## Key Takeaways

* Pipelines help organize the complete machine learning workflow.
* `ColumnTransformer` makes it easy to preprocess numeric and categorical columns differently.
* Feature engineering can also be included directly inside a pipeline.
* `GridSearchCV` can tune model parameters while repeating the complete pipeline inside every cross-validation fold.
* Keeping preprocessing inside the pipeline helps prevent data leakage.
* The test set should remain untouched until the final evaluation.
* The tuned model achieved a better F1 score than the baseline model.

Overall, this lab helped me understand how to build a cleaner, reusable, and more reliable end-to-end machine learning workflow.
