# BinX Internship **readme**

## Contents

- [Week 1](#week-1)
- [Week 2](#week-2)
- [Week 3](#week-3)
- [Week 4](#week-4)

## Week 1

### Day 1

Ive setup the environment and the requierd libraries, then Ive create the requirements file

**Done**

### Day 2

in this day I have finished 3 steps (tasks)

1. **step 1** asked to write a function that takes a list of numbers and returns the mean, min, and max as a dictionary.

    and Ive create a func that recive list of numbers and with the help of .mean() .max() .min() I solve the step

2. **setp 2** asked to rewrite a given for-loop that filters even numbers as a single list comprehension.

    and I created also a func I know it dont ask me for a func but to make everything organized easy

    ```python
    [x for x in numbers if x % 2 == 0]
    ```

3. **step 3** asked me to  Define a small class representing a data record with at least two attributes and one method

    it was a good refresh to my memory I created the class named **BinX** with 2 attributes **name** and **age** finally with a method

    named **greet**

4. **step 4** asked for documentation

**Done**

### Day 3

in this day I refresh my memory using the numpy library it was very useful for me.

and it was very excited to solve the 4 tasks (steps).


**steps and soltuions are in the day3.ipynb**

**Done**

### Day 4: Pandas: Tabular Data

I completed all of the learning objectives for Day 4.

I loaded a real dataset which was the titanic then I select the columns see the metadata after that I filter them 
by the age so my condition was each passenger who's older than 30

I cleaned the null values like **age**, **cabin**, and **Embarked**, then I grouped them by the **Sex** after that I performed an aggregate operations such as **max** for **Age**, **mean** for **Fare**, and finally **mode** for **Embarked**.

then I let the **AI** to write the markdowns cuz I think **AI** doing this job better than me.

so can say **Day 4 IS Done**

### Day 5: **Matplotlib & Week 1 Mini-Notebook**

I learned about four basic types of plots in **Matplotlib**: **line**, **scatter**, **bar**, and **histogram**
then I learned how to combine two plots in the same figure by using subplots

day 5 was only talking about basics, but I know in the future it will be more advanced and benefit

For the **hands-on lab**, I loaded the **Titanic dataset** clean it from missing values, just as I did in the day before. After that,
I created 3 different plots and 1 figure containing 2 subplots.

Markdowns written with AI to illustrate the work better.


## Week 2

### Day 1: Descriptive Statistics

On the first day of Week 2, I learned about descriptive statistics and how they can be used to understand the center and spread of numerical data.

For this task, I used the Titanic dataset and selected the Age column for analysis.

First, I loaded the dataset and removed the missing age values:

```python
import pandas as pd
import numpy as np

data = pd.read_csv("../../week1/day4/train.csv")

age = data["Age"]
age = age.dropna()

age.info()
```

After cleaning the data, I calculated the following statistical measures:

- **Mean**: The average passenger age.
- **Median**: The middle passenger age after sorting the values.
- **Mode**: The most frequently occurring age.
- **Standard deviation**: Shows how spread out the passenger ages are around the mean.
- **Interquartile range (IQR)**: Measures the spread of the middle 50% of the ages.

```python
mean = np.mean(age)
median = np.median(age)

v, c = np.unique(age, return_counts=True)
mode = v[np.argmax(c)]

std = np.std(age)

q1, q3 = np.percentile(age, [25, 75])
iqr = q3 - q1

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std)
print("IQR:", iqr)
```

#### Mean or Median?

I believe the median gives a better representation of a typical passenger's age.

The median age is 28, while the mean is approximately 29.7. The mean is slightly higher because some older passengers increase the overall average.

Since the median is less affected by unusually high or low values, it provides a more accurate representation of the typical passenger's age in this dataset.

#### What I Completed

- I loaded the Titanic train.csv dataset.
- I selected the numerical Age column and removed its missing values.
- I calculated the mean, median, mode, standard deviation, and interquartile range.
- Most of the calculations were familiar to me, but the IQR was a new concept.
- I used GPT to understand how the IQR is calculated, why it is useful, and what its result means.
- I compared the mean and median and concluded that the median better represents a typical passenger's age.

This task helped me understand how descriptive statistics can summarize a dataset and explain how its values are distributed.

**Day 1 is complete.**


### Day 2: Probability & Distributions

On the second day of Week 2, I learned the fundamentals of probability and probability distributions, which are basic concepts in statistics and machine learning.

For the hands-on lab, I completed the following tasks:

- Simulated **10,000 coin flips** using NumPy and verified that the proportion of heads approaches **0.5** as the number of trials increases.
- Generated **10,000 samples** from a normal distribution using `np.random.normal()` and plotted a histogram to observe the characteristic **bell-shaped (Gaussian) distribution**.
- Calculated a **conditional probability** by hand and verified the result using a simulation. The simulated probability closely matched the theoretical probability.
- Documented each step with Markdown explanations describing what each experiment demonstrates.

**Day 2 is complete.**


### Day 3: **Linear Algebra for ML**

On the third day of Week 2, I learned the fundamental linear algebra concepts used in machine learning, including vectors, matrices, the dot product, and matrix multiplication.

For the hands-on lab, I completed the following tasks:

- Represented three data samples as a NumPy matrix, where each row is a sample and each column is a feature.
- Computed the dot product of a sample vector and a weight vector manually, then verified the result using np.dot().
- Used matrix multiplication (@) to generate predictions for all three samples simultaneously.
- Created a shape mismatch error during matrix multiplication, analyzed the error message, and explained why it occurred and how to fix it using the correct matrix dimensions.
- Documented each step with Markdown explanations.

**Day 3 is complete.**

### Day 4: **EDA Part 1 – Distributions & Outliers**

On the fourth day of Week 2, I learned the fundamentals of **Exploratory Data Analysis (EDA)** and why it is an essential step before building any machine learning model. I explored data distributions using statistical visualizations and learned how to detect potential outliers using the IQR method.

For the hands-on lab, I completed the following tasks:

- Loaded the **Titanic** dataset and explored its numeric and categorical features.
- Created **histograms** for the `Age` and `Fare` columns to understand their distributions.
- Generated **box plots** to visualize the spread of the data and identify potential outliers.
- Applied the **Interquartile Range (IQR)** method to detect outliers in the `Age` column. The detected outliers represented elderly passengers rather than data errors, so I decided to keep them.
- Created a **count plot** for the `Sex` column and observed that the dataset contains more male passengers than female passengers.
- Documented the observations from each visualization using Markdown explanations.

**Day 4 is complete.**

### Day 5: **EDA Part 2 – Correlation & Data Storytelling**

On the fifth day of Week 2, I expanded my **EDA** by examining relationships between variables and summarizing the findings in a complete **EDA** notebook. I learned how to identify correlations, interpret their meaning, and communicate insights through data storytelling.

For the hands-on lab, I completed the following tasks:

- Performed **bivariate analysis** using scatter plots and grouped box plots to explore relationships between features.
- Computed a **correlation matrix** and visualized it with a **heatmap** to identify the strongest relationships between numeric variables.
- Used a **pair plot** to quickly inspect relationships and distributions across multiple numeric features.
- Identified and interpreted the strongest correlations, including the relationship between `Fare` and `Pclass`, and between `SibSp` and `Parch`.
- Combined the descriptive statistics, univariate analysis, outlier detection, bivariate analysis, and correlation analysis into a **complete narrated EDA notebook**.
- Documented the key findings using Markdown to create a clear **data storytelling** narrative.

**Day 5 is complete.**



## Week 3

### Day 1:

I watched in this day of training part of the **Scikit-learn Crash Course - Machine Learning Library for Python**
like half an hour it was really useful and refreshs my memory.
I love how he simplify the **scikit-learn** library, he talked also about the **Pipeline** and why to use it, also he mention **GridSearchCV** it was really useful for the model

For the hands-on lab, I completed the following tasks:

- I loaded the **train.csv** dataset that I used in day 4 week 1 which is for titanic, then separate it into features X and target y, the target was `Survived`
- Then I split the dataset into 80/20 train/test with a random_state = 42.
- I confirmed that the X_train, y_train, X_test, and y_test.

### Day 2:
I watched in this day of training part of the **Linear Regression in Machine Learning | Linear Regression Tutorial [With Project] | Intellipaat**

it was really useful and I put everything I learned from the vedio in the `day2.ipynb` 

he says that after the explanation student in high school gonna understands the linear regression, to be honest he was quitly right
his explanation to the topic was very easy.

#### What I learned:

- How to calculate the mean of x and y
- Why we calculate them, and it was to get the inputs to solve the formula y = mx + c, i mean to calculate the value of m and c
- After we got the initial values of m and c, i thought that we finish no, it was only the start, cuz we need to change both of them to get the best fit line.
- We knew which line is better by calculating the **Residuals** for each line and comparing 

For the hands-on lab, I completed the following tasks:

- Trained a Linear Regression model using the California Housing dataset.
- Displayed the model coefficients and identified the feature with the strongest effect.
- Evaluated the model using MAE, RMSE, and R².
- Compared the model’s RMSE with a mean baseline to check whether it added value.
- Summarized and interpreted the results in a Markdown cell.


### Day 3:
I watched in this day of training part of the **Logistic Regression in Machine Learning: The Easiest Explanation Ever! | ML Tutorial | Intellipaat**

I learned the fundamentals of **Logistic Regression in Machine Learning** and how it is different from Linear Regression.

Before this day, I thought that Logistic Regression was just another type of regression that predicts numbers, but I learned that it is actually used for **classification problems**. Instead of predicting a continuous value, it predicts a probability between 0 and 1, which is then converted into a class.

#### What I learned:

- The difference between **Regression** and **Classification** problems.
- Why Linear Regression is not suitable for classification tasks.
- How Logistic Regression uses the **Sigmoid Function** to convert outputs into probabilities.
- How the model decides between classes using a classification threshold (usually 0.5).
- The meaning of **True Positive (TP), True Negative (TN), False Positive (FP), and False Negative (FN)** and how they form the confusion matrix.
- How to evaluate classification models using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - AUC-ROC
- The difference between Precision and Recall:
  - Precision focuses on how reliable the positive predictions are.
  - Recall focuses on how many of the actual positive cases the model was able to find.
- Why choosing between Precision and Recall depends on the problem. For example, in the Titanic survival prediction problem, Recall can be more important because we want to identify as many survivors as possible.

For the hands-on lab, I completed the following tasks:

- Prepared the Titanic dataset for Logistic Regression.
- Handled missing values and converted categorical features into numerical values.
- Trained a Logistic Regression model.
- Generated predictions on the test set.
- Evaluated the model using:
  - Confusion Matrix
  - Classification Report
  - Precision, Recall, and F1-score
  - AUC score
- Interpreted the model's performance and documented the results.


### Day 4: Decision Trees, Random Forests, SVM, and k-NN

On this day of training, I learned about four important machine learning algorithms: **Decision Tree, Random Forest, Support Vector Machine (SVM), and k-Nearest Neighbors (k-NN)**.

I completed the learning and practice examples in the **`day4.ipynb`** notebook, while the hands-on lab and model comparison tasks were completed in the **`tasks.ipynb`** notebook.

#### What I Learned

* A **Decision Tree** works like a flowchart and makes predictions using a series of questions or conditions.
* A Decision Tree consists of a root node, internal nodes, branches, and leaf nodes.
* Decision Trees can be used for both classification and regression.
* Decision Trees usually do not require feature scaling, but they can suffer from overfitting when they become too deep.
* A **Random Forest** combines the predictions of multiple Decision Trees to produce more stable and accurate results.
* Random Forest can reduce overfitting compared with using a single Decision Tree.
* Random Forest provides feature importance values that show which features had the greatest influence on its predictions.
* **SVM** finds the best boundary that separates different classes while keeping the largest possible margin between them.
* SVM usually requires feature scaling because its performance is affected by the ranges of the features.
* **k-NN** classifies a new data point based on the classes of its nearest neighbors.
* The value of **k** determines how many neighboring points are considered when making a prediction.
* k-NN also requires feature scaling because it depends on calculating distances between data points.

#### Hands-on Lab

For the hands-on lab, I completed the following tasks in **`tasks.ipynb`**:

* Used the same Titanic dataset and train/test split from Day 3.
* Trained a Decision Tree model.
* Trained a Random Forest model.
* Scaled the data before training SVM and k-NN.
* Trained an SVM model.
* Trained a k-NN model.
* Generated predictions using all four models.
* Evaluated all models using the same metric, which was the **F1-score**.
* Created a comparison table containing the F1-score of each model.
* Reported the most important features identified by the Random Forest model.
* Interpreted how the most important features influenced the model's predictions.
* Identified the best-performing model based on the highest F1-score.
* Explained why the best-performing model likely achieved better results on this dataset.


### Day 5:

In this day of training, I worked on a **Titanic Survival Classification Mini-Project** and applied the full supervised machine learning workflow.

I learned how to prepare the data, compare multiple models, and evaluate their performance using cross-validation and an unseen test set.

#### What I learned:

* How to split the dataset before preprocessing.
* How to handle missing values and categorical features.
* How to use **StandardScaler** and **One-Hot Encoding**.
* How to compare a **Dummy Classifier, Logistic Regression, and Random Forest**.
* How to use **5-fold Stratified Cross-Validation** for model selection.
* How to evaluate classification models using:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * ROC-AUC
* How to use a **Confusion Matrix** to understand prediction errors.
* Why the test set should only be used for final evaluation and not for choosing the best model.

For the mini-project, I completed the following tasks:

* Explored and cleaned the Titanic dataset.
* Compared three classification models.
* Selected the best model using cross-validation F1-score.
* Evaluated the models on unseen test data.
* Created a confusion matrix and documented the final results.

**Day 5 Mini-Project Completed**

## Week 4

### Day 1: Train / Validation / Test Splits

In Week 4, I started going deeper into how machine learning models should be evaluated during development.

I learned the difference between:

- Training data for learning.
- Validation data for tuning and selecting settings.
- Test data for the final evaluation.

[Day1 learning](week4/day1/day1.ipynb)

I created a 60/20/20 train/validation/test split, trained a KNN model, tuned n_neighbors using the validation set, and kept the test set untouched until the final evaluation.

[Hadns-on Lab](week4/day1/hands-on-lab.ipynb)

This helped me understand why repeatedly tuning against the test set can give misleading results and why proper validation is important when building reliable machine learning models.

### Day 2: Cross-Validation

I learned how **k-fold cross-validation** provides a more reliable evaluation than relying on a single validation split.

I used `cross_val_score` to evaluate a KNN model across five folds and learned how to interpret the **mean score** and **standard deviation**.

I also learned why **Stratified K-Fold** is useful for classification because it keeps approximately the same class distribution in each fold.

[Day 2 Learning](week4/day2/day2.ipynb)

For the hands-on lab, I tested multiple values of `n_neighbors` using **5-fold cross-validation**. The best value was `n_neighbors = 11`, with a mean accuracy of approximately **0.8132**.

I compared this result with the single validation split from Day 1 and saw why cross-validation provides a more stable estimate of the model's expected performance.

[Day 2 Hands-on Lab](week4/day2/hands-on-lab.ipynb)


### Day 3: Bias-Variance & Diagnosing Model Fit

On Day 3, I learned how to recognize **underfitting and overfitting** by comparing the training and validation scores.

I learned that:

* Low training and validation performance can indicate underfitting.
* Very high training performance with lower validation performance can indicate overfitting.
* A smaller train-validation gap with good scores usually indicates better generalization.

I also learned about the **bias-variance trade-off** and how regularization techniques such as **Ridge and Lasso** can help control model complexity.

For the hands-on lab, I used the Breast Cancer dataset and created three different model situations.

I used an unrestricted Decision Tree to demonstrate overfitting, a simple `DummyClassifier` to demonstrate underfitting, and then reduced the complexity of the Decision Tree using `max_depth=4` and `min_samples_leaf=10`.

After reducing the complexity, the model achieved **0.9626 training accuracy** and **0.9473 validation accuracy**, with a much smaller gap of **0.0152**.

This helped me understand that the goal is not to get the highest training score, but to create a model that also performs well on unseen data.

[Day 3 Hands-on Lab](week4/day3/hands-on-lab.ipynb)


### Day 4: Feature Engineering & Hyperparameter Tuning

On Day 4, I learned about **feature engineering** and **hyperparameter tuning**, and how both can improve a machine learning model.

I learned that feature engineering means creating new features or transforming existing ones to give the model more useful information.

I also learned the difference between:

* **Parameters**, which are learned by the model during training.
* **Hyperparameters**, which are selected before training, such as `n_estimators`, `max_depth`, and `min_samples_leaf`.

I also learned how **GridSearchCV** can test different hyperparameter combinations automatically using cross-validation instead of trying them manually.

For the hands-on lab, I continued working with the **Titanic dataset** and a **Random Forest classifier**.

I created two new engineered features:

* `FamilySize`, created by combining `SibSp` and `Parch`.
* `IsAlone`, created from `FamilySize` to indicate whether a passenger was traveling alone.

I then created a hyperparameter grid for:

* `n_estimators`
* `max_depth`
* `min_samples_leaf`

I used **GridSearchCV with 5-fold cross-validation** and the **F1-score** to search for the best Random Forest settings.

I also compared the tuned model with a baseline Random Forest model and analyzed the effect of the tested hyperparameters.

From the feature importance results, **`FamilySize`** had a higher importance than `IsAlone`.

From the GridSearchCV results, **`min_samples_leaf`** had the biggest effect on the average F1-score among the hyperparameters I tested.

This day helped me understand that improving a machine learning model is not only about choosing a different algorithm. Creating better features and selecting better hyperparameters can also improve the model's performance.

[Day 4 Hands-on Lab](week4/day4/hands-on-lab.ipynb)

### Day 5: Scikit-learn Pipelines

On Day 5, I learned how to combine preprocessing and modeling into one complete workflow using `Pipeline` and `ColumnTransformer`.

I handled numeric and categorical columns separately, added feature engineering inside the pipeline, and used `GridSearchCV` with 5-fold cross-validation to tune the full workflow without data leakage.

This helped me understand how pipelines make machine learning projects cleaner, safer, and easier to reuse.

[Day 5 Hands-on Lab](day5/hands-on-lab.ipynb)

### Mini-Project: Tuned End-to-End Pipeline

For the mini-project, I combined the main ideas from Week 4 into one complete Titanic classification workflow.

I built a leak-free pipeline, added engineered features, tuned a Random Forest model with `GridSearchCV`, and evaluated the final selected pipeline on the untouched test set.

The baseline cross-validation F1 score was **0.7264**, the best tuned cross-validation F1 was **0.7573**, and the final test F1 was **0.7143**.

This project helped me connect data splitting, cross-validation, feature engineering, tuning, pipelines, and final evaluation into one complete machine learning process.

[Mini-Project](mini-project/week4-mini-project.ipynb)

## Week 5

### Day 1: Unsupervised Learning & K-Means

In Week 5, I started learning about **unsupervised learning** and how it differs from the supervised learning methods I worked with before.

I learned that in unsupervised learning there is no target `y`. Instead, the model works only with the input features and tries to discover hidden structure in the data.

I focused on **K-Means clustering**, which groups similar data points together based on distance.

I also learned that scaling is very important for K-Means, so I used `StandardScaler` before clustering.

For the hands-on lab, I used the **Iris dataset** and tested values of `k` from 1 to 10.

I used the **Elbow Method** to find good candidate values for the number of clusters, then compared `k = 2` and `k = 3` using the **Silhouette Score**.

The results were:

* `k = 2`: **0.581750**
* `k = 3`: **0.459948**

I selected `k = 2`, trained the final K-Means model, visualized the clusters, and examined their average feature values to understand what each group represented.

This helped me understand how clustering can discover meaningful groups in data without using any known labels.

[Day 1 Hands-on Lab](week5/day1/hands-on-lab.ipynb).


