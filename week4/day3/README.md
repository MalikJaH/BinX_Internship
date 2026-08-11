# Day 3: Bias-Variance & Diagnosing Model Fit

In this day, I learned about **underfitting, overfitting, the bias-variance trade-off, and how to diagnose model fit** by comparing training and validation scores.

I also watched a video about **overfitting, underfitting, and regularization**, which helped me understand that getting a very high training score does not always mean that the model is good.

## What I Learned

* **Underfitting** happens when the model is too simple and cannot learn enough from the training data.
* **Overfitting** happens when the model learns the training data too closely but does not perform as well on new data.
* A large gap between the training and validation scores can be a sign of overfitting.
* Low performance on both training and validation data can be a sign of underfitting.
* The **bias-variance trade-off** is about finding a balance between a model that is too simple and one that is too complex.
* Regularization can help reduce overfitting.
* **Ridge (L2)** reduces the size of model coefficients.
* **Lasso (L1)** can reduce some coefficients to zero.
* The `alpha` value controls the strength of regularization.

## Hands-On Lab

For the practical work, I used the **Breast Cancer dataset** from Scikit-learn and tested different model behaviors.

First, I trained a Decision Tree without limiting its depth to deliberately create an overfitting model.

The model achieved:

* Training Accuracy: **1.0000**
* Validation Accuracy: **0.9123**
* Gap: **0.0877**

The perfect training score and lower validation score showed that the model was learning the training data too closely.

Then, I used a very simple `DummyClassifier` to demonstrate underfitting.

It achieved:

* Training Accuracy: **0.6263**
* Validation Accuracy: **0.6315**

Both scores were much lower than the Decision Tree models because the model was too simple to learn the important patterns in the features.

Finally, I reduced the complexity of the Decision Tree using:

```python
max_depth=4
min_samples_leaf=10
```

The new model achieved:

* Training Accuracy: **0.9626**
* Validation Accuracy: **0.9473**
* Gap: **0.0152**

The validation accuracy improved and the gap became much smaller, showing that reducing the model complexity helped it generalize better.

## Conclusion

This day helped me understand that the goal of machine learning is not to get the highest possible training score.

A good model should learn enough from the training data while still performing well on unseen data.

I now have a better understanding of how training and validation scores can be used to diagnose **underfitting, overfitting, and good model fit**.
