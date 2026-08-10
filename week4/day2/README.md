### Day 2: Cross-Validation

In this day of training, I learned how **Cross-Validation** gives a more reliable estimate of a model's performance compared with using only one validation split.

I learned how **k-fold cross-validation** divides the training data into multiple folds and trains the model several times. In each round, one fold is used for validation while the remaining folds are used for training.

[Day 2 Learning](day2.ipynb)

#### What I Learned

* Why one validation split can sometimes give a lucky or unlucky result.
* How **k-fold cross-validation** works.
* How to use `cross_val_score`.
* How to calculate and interpret the **mean cross-validation score**.
* How the **standard deviation** shows how stable the model is across different folds.
* Why **Stratified K-Fold** is important for classification tasks.
* How stratification keeps approximately the same class distribution in every fold.
* How to compare a cross-validation estimate with a single validation split.

For the hands-on lab, I used the Titanic dataset and a KNN classifier.

I tested different values of `n_neighbors` using **5-fold cross-validation** and calculated the mean accuracy and standard deviation for each value.

The best result was:

* `n_neighbors = 11`
* Mean Cross-Validation Accuracy = **0.8132**
* Standard Deviation = **0.0230**

The same value, `n_neighbors = 11`, was also selected using the single validation split from Day 1.

I also confirmed that the classification folds were stratified. Each fold kept approximately the same target distribution:

* Class `1` → **62.6%**
* Class `0` → **37.4%**

[Hands-on Lab](hands-on-lab.ipynb)

This day helped me understand why cross-validation gives a more stable and reliable estimate of model performance than relying on only one validation set.
