# BinX Internship **readme**

## Week 1

## Day 1 

Ive setup the environment and the requierd libraries, then Ive create the requirements file

**Done**

## Day 2
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

## Day 3 

in this day I refresh my memory using the numpy library it was very useful for me.

and it was very excited to solve the 4 tasks (steps).


**steps and soltuions are in the day3.ipynb**

**Done**

## Day 4: Pandas: Tabular Data

I completed all of the learning objectives for Day 4.

I loaded a real dataset which was the titanic then I select the columns see the metadata after that I filter them 
by the age so my condition was each passenger who's older than 30

I cleaned the null values like **age**, **cabin**, and **Embarked**, then I grouped them by the **Sex** after that I performed an aggregate operations such as **max** for **Age**, **mean** for **Fare**, and finally **mode** for **Embarked**.

then I let the **AI** to write the markdowns cuz I think **AI** doing this job better than me.

so can say **Day 4 IS Done**

## Day 5: **Matplotlib & Week 1 Mini-Notebook**

I learned about four basic types of plots in **Matplotlib**: **line**, **scatter**, **bar**, and **histogram**
then I learned how to combine two plots in the same figure by using subplots

day 5 was only talking about basics, but I know in the future it will be more advanced and benefit

For the **hands-on lab**, I loaded the **Titanic dataset** clean it from missing values, just as I did in the day before. After that,
I created 3 different plots and 1 figure containing 2 subplots.

Markdowns written with AI to illustrate the work better.


## Week 2

## Day 1: Descriptive Statistics

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

**Mean**: The average passenger age.
**Median**: The middle passenger age after sorting the values.
**Mode**: The most frequently occurring age.
**Standard deviation**: Shows how spread out the passenger ages are around the mean.
**Interquartile range (IQR)**: Measures the spread of the middle 50% of the ages.
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
Mean or Median?

I believe the median gives a better representation of a typical passenger's age.

The median age is 28, while the mean is approximately 29.7. The mean is slightly higher because some older passengers increase the overall average.

Since the median is less affected by unusually high or low values, it provides a more accurate representation of the typical passenger's age in this dataset.

**What I Completed**
I loaded the Titanic train.csv dataset.
I selected the numerical Age column and removed its missing values.
I calculated the mean, median, mode, standard deviation, and interquartile range.
Most of the calculations were familiar to me, but the IQR was a new concept.
I used GPT to understand how the IQR is calculated, why it is useful, and what its result means.
I compared the mean and median and concluded that the median better represents a typical passenger's age.

This task helped me understand how descriptive statistics can summarize a dataset and explain how its values are distributed.

**Day 1 is complete.**


## Day 2: Probability & Distributions

On the second day of Week 2, I learned the fundamentals of probability and probability distributions, which are basic concepts in statistics and machine learning.

For the hands-on lab, I completed the following tasks:

- Simulated **10,000 coin flips** using NumPy and verified that the proportion of heads approaches **0.5** as the number of trials increases.
- Generated **10,000 samples** from a normal distribution using `np.random.normal()` and plotted a histogram to observe the characteristic **bell-shaped (Gaussian) distribution**.
- Calculated a **conditional probability** by hand and verified the result using a simulation. The simulated probability closely matched the theoretical probability.
- Documented each step with Markdown explanations describing what each experiment demonstrates.

**Day 2 is complete.**


## Day 3: **Linear Algebra for ML**

On the third day of Week 2, I learned the fundamental linear algebra concepts used in machine learning, including vectors, matrices, the dot product, and matrix multiplication.

For the hands-on lab, I completed the following tasks:

- Represented three data samples as a NumPy matrix, where each row is a sample and each column is a feature.
- Computed the dot product of a sample vector and a weight vector manually, then verified the result using np.dot().
- Used matrix multiplication (@) to generate predictions for all three samples simultaneously.
- Created a shape mismatch error during matrix multiplication, analyzed the error message, and explained why it occurred and how to fix it using the correct matrix dimensions.
- Documented each step with Markdown explanations.

**Day 3 is complete.**

## Day 4: **EDA Part 1 – Distributions & Outliers**

On the fourth day of Week 2, I learned the fundamentals of **Exploratory Data Analysis (EDA)** and why it is an essential step before building any machine learning model. I explored data distributions using statistical visualizations and learned how to detect potential outliers using the IQR method.

For the hands-on lab, I completed the following tasks:

- Loaded the **Titanic** dataset and explored its numeric and categorical features.
- Created **histograms** for the `Age` and `Fare` columns to understand their distributions.
- Generated **box plots** to visualize the spread of the data and identify potential outliers.
- Applied the **Interquartile Range (IQR)** method to detect outliers in the `Age` column. The detected outliers represented elderly passengers rather than data errors, so I decided to keep them.
- Created a **count plot** for the `Sex` column and observed that the dataset contains more male passengers than female passengers.
- Documented the observations from each visualization using Markdown explanations.

**Day 4 is complete.**

## Day 5: **EDA Part 2 – Correlation & Data Storytelling**

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

what I learned: 

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

What I learned:

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
