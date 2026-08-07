# BinX Internship — Week 1

During the first week of my internship, I focused on refreshing my Python knowledge and learning the basic tools used in data analysis.

The week started with setting up the development environment, then moved through Python fundamentals, NumPy, Pandas, and Matplotlib. Each day included practical tasks that helped me apply what I learned instead of only watching tutorials or reading explanations.

---

## Day 1 — Environment Setup

On the first day, I prepared the development environment and installed the required Python libraries.

I also created a `requirements.txt` file to keep track of the libraries used throughout the training. This makes it easier to install the same dependencies on another device or environment.

**Status: Done**

---

## Day 2 — Python Fundamentals

On Day 2, I refreshed some important Python concepts by completing four tasks.

### Step 1 — Working with Functions

The first task was to create a function that receives a list of numbers and returns the following values inside a dictionary:

* Mean
* Minimum value
* Maximum value

This task helped me review how to create functions, work with lists, calculate values, and return structured results.

### Step 2 — List Comprehension

The second task was to rewrite a regular loop that filters even numbers as a single list comprehension.

```python
[x for x in numbers if x % 2 == 0]
```

Although the task did not require creating a function, I decided to place the code inside one to keep the solution organized and reusable.

### Step 3 — Classes and Objects

The third task was to create a small class representing a data record.

I created a class named `BinX` with two attributes:

* `name`
* `age`

I also added a method named `greet`.

This task was a useful refresher on object-oriented programming, including classes, objects, attributes, methods, and constructors.

### Step 4 — Documentation

The final task was to document the work and explain the implemented solutions clearly.

**Status: Done**

---

## Day 3 — NumPy Fundamentals

On Day 3, I refreshed my knowledge of the **NumPy** library.

NumPy is one of the most important Python libraries for numerical operations and working with arrays. I enjoyed completing the practical tasks because they helped me understand how NumPy can perform operations using simple and efficient code.

During this day, I practiced:

* Creating arrays using `arange()`.
* Reshaping arrays into different dimensions.
* Accessing specific rows and columns.
* Calculating the mean of an array.
* Filtering values using Boolean conditions.
* Adding a one-dimensional array to a two-dimensional array.
* Understanding the basic idea of broadcasting.

The complete steps and solutions are available in `day3.ipynb`.

**Status: Done**

---

## Day 4 — Pandas: Tabular Data

On Day 4, I learned how to work with tabular data using the **Pandas** library.

For the practical work, I used the Titanic dataset. Working with a real dataset made the lesson more interesting because I could see how Pandas is used to explore, clean, and analyze data.

I started by loading the dataset and exploring its structure. I selected specific columns and checked information about the dataset, such as column names, data types, and missing values.

After that, I filtered the passengers based on age. The condition I used was to select passengers who were older than 30.

I also practiced cleaning missing values in columns such as:

* `Age`
* `Cabin`
* `Embarked`

After cleaning the data, I grouped it by `Sex` and performed several aggregation operations, including:

* Finding the maximum age.
* Calculating the average fare.
* Finding the most common embarkation port.

I used AI to improve the Markdown explanations and make the notebook easier to understand, while the data analysis and practical tasks were completed as part of my learning.

**Status: Done**

---

## Day 5 — Matplotlib and Week 1 Mini-Notebook

On Day 5, I learned the basics of data visualization using **Matplotlib**.

I practiced four common types of plots:

* Line plot
* Scatter plot
* Bar chart
* Histogram

I also learned how to use subplots to display more than one chart inside the same figure.

The lesson focused on the basic concepts of Matplotlib, but it gave me a good foundation for creating more advanced visualizations in the future.

### Hands-On Lab

For the hands-on lab, I worked with the Titanic dataset again.

I started by loading the dataset and cleaning its missing values, similar to the work I completed on Day 4.

After preparing the data, I created:

* Three different individual plots.
* One figure containing two subplots.

This task helped me understand that charts are not only used to make the data look better. They also make patterns, comparisons, and distributions easier to understand.

I used AI to improve the Markdown explanations so the notebook could communicate the results more clearly.

**Status: Done**

---

## Week 1 Summary

Week 1 was a valuable introduction to the main Python tools used in data analysis.

Throughout the week, I practiced:

* Setting up a Python development environment.
* Managing project dependencies.
* Writing functions and list comprehensions.
* Creating classes and methods.
* Working with NumPy arrays.
* Loading and cleaning datasets with Pandas.
* Filtering, grouping, and aggregating data.
* Creating basic data visualizations with Matplotlib.
* Documenting technical work clearly.

Some topics were a refresh of concepts I had learned before, while others helped me understand how Python can be used in real data-analysis tasks.

The practical exercises were especially useful because they allowed me to apply each concept directly. By the end of the week, I had built a stronger foundation in Python, NumPy, Pandas, and Matplotlib, which will help me during the next stages of the internship.

## Week 1 Completed 
