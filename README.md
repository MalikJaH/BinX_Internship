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