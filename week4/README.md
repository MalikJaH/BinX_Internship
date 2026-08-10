## Week 4 

### Day 1: Train / Validation / Test Splits
This week, I started learning more about how to properly evaluate and tune machine learning models.

I learned why the usual **train/test split** can become a problem when the test set is repeatedly used while changing model settings.

To solve this, I learned how to divide the data into:

* **Training set** for learning.
* **Validation set** for tuning and model selection.
* **Test set** for the final evaluation.
[Day1 learning](day1/day1.ipynb)

For the practical work, I created a **60/20/20 split**, trained a KNN classifier, tested different values of `n_neighbors` using only the validation set, selected the best setting, and then evaluated the final model on the untouched test set.
[Hadns-on Lab](day1/hands-on-lab.ipynb)

This helped me better understand that evaluating a machine learning model is not only about getting a high score, but also about making sure that the score is a fair and honest estimate of how the model performs on unseen data.

The topic also introduced the limitation of using only one validation split and prepared me for learning about **Cross-Validation**.

### Day 2: Cross-Validation

On Day 2, I learned how Cross-Validation improves model evaluation by using multiple validation folds instead of relying on only one validation split.

I learned how k-fold cross-validation works and how every fold is used once for validation while the remaining folds are used for training.

I also learned how to use cross_val_score and interpret:

- The individual fold scores.  
- The mean score as the overall performance estimate.  
- The standard deviation as a measure of how stable the model is across different folds.  

[Day 2 Learning](day2/day2.ipynb)

For the hands-on lab, I used KNN with the Titanic dataset and tested several values of `n_neighbors` using 5-fold cross-validation.

The best value was again `n_neighbors` = 11, with a mean cross-validation accuracy of approximately 0.8132.

I compared this result with the single validation score from Day 1 and learned why the two estimates can be different.

I also used Stratified K-Fold and confirmed that the class proportions remained approximately the same in every fold.

[Hands-on Lab](day2/hands-on-lab.ipynb)

After these two days, I have a clearer understanding of the progression from using one validation set to using cross-validation for a more reliable estimate of model performance.