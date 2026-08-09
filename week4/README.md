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
