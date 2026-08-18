# Day 3 — Week 5: Dimensionality Reduction with PCA

## Overview

This notebook focuses on **Principal Component Analysis (PCA)**, a dimensionality reduction technique used to transform a dataset with multiple features into a smaller number of principal components while preserving as much information as possible.

The main goals of this day were to understand the **curse of dimensionality**, apply PCA to a high-dimensional dataset, analyze explained variance, choose an appropriate number of principal components, and visualize the data in two dimensions.

---

## Learning Objectives

By the end of this lab, I was able to:

* Explain the curse of dimensionality and why dimensionality reduction is useful.
* Understand how PCA creates principal components.
* Scale numerical features before applying PCA.
* Interpret explained variance ratios.
* Calculate cumulative explained variance.
* Choose the number of components required to preserve approximately 95% of the variance.
* Reduce the dataset to two dimensions for visualization.
* Understand the advantages and limitations of PCA.

---

## Dataset

The PCA analysis was performed using a synthetic cardiac-style dataset.

The selected numerical features were:

* `age`
* `resting_bp`
* `cholesterol`
* `bmi`
* `fasting_blood_sugar`
* `max_heart_rate`

The dataset contained:

* **1,215 observations**
* **6 input features**

The `cardiac_risk` column was not included as an input feature in PCA. It was used only to color the points in the final 2D visualization.

---

## Step 1 — Data Preprocessing and Scaling

Before applying PCA, the selected numerical features were preprocessed.

Missing values were handled using median imputation, and the features were standardized using `StandardScaler`.

Scaling is especially important for PCA because PCA is based on variance. Without scaling, features with larger numerical ranges could dominate the principal components even if they are not actually more informative.

The final data shape after preprocessing remained:

```text
Original shape: (1215, 6)
Scaled shape:   (1215, 6)
```

---

## Step 2 — Explained Variance Analysis

PCA was first fitted using all six possible principal components.

The explained variance ratios were:

| Principal Component | Explained Variance |
| ------------------- | -----------------: |
| PC1                 |             33.37% |
| PC2                 |             17.83% |
| PC3                 |             15.71% |
| PC4                 |             14.22% |
| PC5                 |             12.96% |
| PC6                 |              5.90% |

The cumulative explained variance was:

| Number of Components | Cumulative Variance |
| -------------------: | ------------------: |
|                    1 |              33.37% |
|                    2 |              51.20% |
|                    3 |              66.92% |
|                    4 |              81.13% |
|                    5 |              94.10% |
|                    6 |             100.00% |

A cumulative explained variance plot was created to visualize how much information is retained as additional principal components are included.

A horizontal reference line at **95% variance** was used to help determine the appropriate number of components.

---

## Step 3 — Choosing the Number of Components

A common PCA approach is to retain enough components to preserve approximately **95% of the total variance**.

In this dataset:

```text
5 components → 94.10%
6 components → 100.00%
```

Because five components preserve only 94.10%, they do not satisfy the strict 95% threshold.

Therefore:

```text
Number of components required for 95% variance: 6
```

Since the original dataset already contained six features, PCA did not reduce the dimensionality when using a strict 95% variance threshold.

This suggests that the selected features contain relatively distinct information, and removing one complete principal component would result in losing more than 5% of the total variance.

---

## Step 4 — Two-Dimensional PCA Visualization

PCA was also applied using only two principal components to create a two-dimensional representation of the dataset.

The first two components explained:

```text
PC1: 33.37%
PC2: 17.83%
```

Together:

```text
Total retained variance: 51.20%
```

The transformed dataset therefore changed from:

```text
6 dimensions
      ↓
     PCA
      ↓
2 dimensions
```

The PCA coordinates were stored in two new columns:

* `PC1`
* `PC2`

A scatter plot was then created using:

* PC1 on the x-axis
* PC2 on the y-axis
* `cardiac_risk` as the point color

The `cardiac_risk` variable was used only for visualization and was not included when PCA calculated the principal components.

The 2D representation is useful for identifying possible patterns, clusters, and separation between known groups.

However, the first two components retain only **51.20%** of the original variance, meaning that approximately **48.80%** of the variance is not represented in the 2D plot.

---

## Step 5 — Interpretation

The PCA analysis showed that the dataset cannot be strongly compressed while preserving at least 95% of its total variance.

All six principal components are required to retain at least 95%, meaning that a strict 95% PCA threshold provides no dimensionality reduction for these six selected features.

However, PCA is still useful for visualization.

Reducing the dataset to two principal components allows the original six-dimensional data to be displayed in a 2D scatter plot while preserving the two strongest directions of variation.

### What PCA Preserved

PCA preserved:

* The strongest directions of variance in the dataset.
* Relationships and shared variation among the original numerical features.
* 100% of the variance when all six components were retained.
* 51.20% of the variance in the two-dimensional visualization.

### What PCA Cost

The main trade-offs were:

* Reducing to two components removed approximately 48.80% of the total variance from the visualization.
* Principal components are combinations of the original features and are therefore harder to interpret directly.
* PCA mainly captures linear patterns in the data.
* The strict 95% threshold did not provide dimensionality reduction for this particular dataset.

---

## Key Concepts

### Curse of Dimensionality

As the number of features increases, the feature space becomes increasingly sparse.

High dimensionality can make distance-based algorithms less effective, increase computational cost, increase the risk of overfitting, and make visualization difficult.

Dimensionality reduction attempts to reduce these problems while preserving important information.

### Principal Components

PCA creates new features called **principal components**.

The components are ordered according to the amount of variance they capture:

```text
PC1 → largest variance
PC2 → second-largest variance
PC3 → third-largest variance
...
```

Each principal component is a linear combination of the original features.

### Explained Variance Ratio

The explained variance ratio represents the proportion of total dataset variance captured by each principal component.

For example:

```text
PC1 = 33.37%
```

means that the first principal component captures 33.37% of the total variance in the standardized data.

### Cumulative Explained Variance

Cumulative explained variance measures the total variance retained after combining multiple principal components.

For example:

```text
PC1 + PC2 + PC3 + PC4 + PC5 = 94.10%
```

This value helps determine how many components should be retained.

---

## PCA Workflow

The general workflow used in this lab was:

```text
Select numerical features
        ↓
Handle missing values
        ↓
StandardScaler
        ↓
Fit PCA
        ↓
Calculate explained variance
        ↓
Calculate cumulative variance
        ↓
Choose number of components
        ↓
Transform the dataset
        ↓
Visualize / use in downstream models
```

---

## Libraries Used

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
```

---

## Main Results

```text
Dataset shape:                  (1215, 6)

PC1 explained variance:         33.37%
PC2 explained variance:         17.83%

2D retained variance:           51.20%

5-component variance:           94.10%
6-component variance:           100.00%

Components required for ≥95%:  6
```

---

## Conclusion

This lab demonstrated how PCA can be used to analyze and reduce the dimensionality of a dataset.

For the selected cardiac features, five principal components preserved 94.10% of the total variance, while all six components were required to satisfy a strict 95% threshold.

Therefore, PCA did not provide meaningful dimensionality reduction at the 95% threshold for this dataset.

Nevertheless, reducing the dataset to two principal components provided a useful visualization of the observations in two-dimensional space. The first two components retained 51.20% of the total variance, making the plot useful for exploratory analysis while also showing the trade-off between dimensionality reduction and information preservation.

The key lesson from this exercise is that **PCA does not always guarantee a large reduction in dimensions**. The number of components that can be removed depends on how much redundant or correlated information exists in the original features.
