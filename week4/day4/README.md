# Day 4 — Feature Engineering & Hyperparameter Tuning

## What I Learned

Today I learned about **feature engineering** and **hyperparameter tuning**.

I learned that improving the features given to a model can sometimes be more useful than changing to a more complicated model. Feature engineering means creating or transforming input features so that they can provide better information to the model.

I also learned the difference between **parameters** and **hyperparameters**:

- **Parameters** are learned by the model during training.
- **Hyperparameters** are values that we choose before training, such as `n_estimators`, `max_depth`, and `min_samples_leaf` in a Random Forest.

I learned how `GridSearchCV` can test different combinations of hyperparameters using cross-validation instead of trying values manually.

## Hands-On Lab

[Day 4 Hands-on Lab](hands-on-lab.ipynb)

For the practical work, I continued using the **Titanic dataset** and a **Random Forest classifier**.

I created two new engineered features:

- `FamilySize`, created from `SibSp` and `Parch`.
- `IsAlone`, created from `FamilySize`.

I then created a hyperparameter grid for:

- `n_estimators`
- `max_depth`
- `min_samples_leaf`

I used `GridSearchCV` with **5-fold cross-validation** and `F1` as the scoring metric to search for the best combination.

I also compared the tuned model with a baseline Random Forest model.

Finally, I used Random Forest feature importance to compare the engineered features. `FamilySize` had a higher importance than `IsAlone`.

From the GridSearchCV results, `min_samples_leaf` had the biggest effect on the average F1 score among the hyperparameters that I tested.

## What I Took From This Day

This day helped me understand that improving a machine learning model is not only about selecting another algorithm.

The features used by the model and the hyperparameters selected before training can both affect the final performance.

I also learned how GridSearchCV makes hyperparameter tuning more systematic by combining the search process with cross-validation.

**Day 4 Done**
