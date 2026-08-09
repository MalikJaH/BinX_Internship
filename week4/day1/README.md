## Train / Validation / Test Splits

In this day of training, I learned why using only a **train/test split** is not always enough when we start tuning models.

I learned the purpose of the three different datasets:

* **Training set**: used to train the model.
* **Validation set**: used to compare different model settings and choose the best one.
* **Test set**: used only once at the end for the final evaluation.

The most important thing I learned is that we should not tune the model using the test set, because this makes the test result less reliable.
[Day1 learning](./day1.ipynb)

For the hands-on lab, I:

* Created a **60/20/20 train/validation/test split** using two `train_test_split()` calls.
* Used a fixed `random_state` to keep the split reproducible.
* Trained a KNN model using only the training set.
* Tried different values of `n_neighbors`.
* Used the validation set to select the best value.
* Evaluated the final model on the test set only after finishing the tuning process.
* Explained why tuning against the test set can produce misleading results.
[Hadns-on Lab](./hands-on-lab.ipynb)

I also learned that one validation split can still be affected by the way the data was randomly divided, which leads to the idea of **Cross-Validation**.

**Day completed.**
