# Day 4 — t-SNE & Anomaly Detection

Today, I continued learning about **unsupervised learning** by exploring two techniques with different purposes: **t-SNE** for visualizing high-dimensional data and **Isolation Forest** for detecting unusual observations.

## What I Learned

I started with **t-SNE (t-distributed Stochastic Neighbor Embedding)**, a dimensionality-reduction technique designed mainly for visualization.

Like PCA, t-SNE can reduce a dataset with many features into two dimensions. However, the two methods focus on different aspects of the data.

**PCA** focuses on preserving the overall variance and global structure of the dataset, while **t-SNE** focuses more strongly on preserving local neighborhoods. This means that observations that are similar in the original high-dimensional space tend to appear close together in the t-SNE visualization.

I also learned that t-SNE is mainly used for **exploration and visualization**. Its axes do not have a direct interpretation, and it is generally not used as a preprocessing step for a machine-learning model.

The second topic was **anomaly detection**, which aims to identify observations that differ significantly from the majority of the dataset.

I learned about **Isolation Forest**, an unsupervised anomaly-detection algorithm based on the idea that unusual observations are easier to isolate than normal observations.

One of its important parameters is:

* `contamination`: the expected proportion of anomalies in the dataset.

Isolation Forest returns:

* `1` for normal observations.
* `-1` for detected anomalies.

## Hands-On Lab

For the hands-on lab, I applied **t-SNE, PCA, and Isolation Forest** to the same standardized numeric features used in the previous unsupervised-learning exercises.

### t-SNE

I reduced the dataset from six features to two dimensions using:

```python
TSNE(
    n_components=2,
    perplexity=30,
    random_state=42
)
```

The resulting t-SNE representation had:

* **1,215 observations**
* **2 dimensions**
* **Perplexity: 30**

I colored the points using the **K-Means cluster labels** from the previous clustering exercise.

The visualization showed clear local structure in the dataset. One of the K-Means clusters formed a strongly separated group, while the other two clusters occupied a larger region with some overlap.

### PCA vs. t-SNE

I compared the t-SNE visualization with the **PCA projection**.

The PCA plot showed the broader structure of the dataset but contained more overlap between the clusters.

The t-SNE plot showed clearer local separation between some of the groups.

This comparison demonstrated that:

* **PCA** is better suited for preserving global variance and can also be used for dimensionality reduction before modeling.
* **t-SNE** is especially useful for visually exploring local structure and possible cluster separation.

### Isolation Forest

I then applied Isolation Forest using:

```python
IsolationForest(
    contamination=0.05,
    random_state=42
)
```

The result was:

* **1,154 normal observations**
* **61 anomalies**
* **5.02% of the dataset flagged as anomalous**

The detected percentage was very close to the expected 5% contamination level.

I also visualized the anomalies using both the **PCA and t-SNE projections**. Some anomalies appeared near the edges of the distributions, while others were not obviously unusual in two dimensions because Isolation Forest evaluates all six features together.

### Inspecting Two Anomalies

Finally, I inspected the two observations with the lowest anomaly scores.

Both observations had a **maximum heart rate close to 196**, with z-scores greater than **+3**, making this feature highly unusual compared with the rest of the dataset.

The strongest anomaly also had:

* unusually low cholesterol with a z-score of approximately **-2.43**
* fasting blood sugar equal to `1`
* a younger-than-average age

The second anomaly showed a similar pattern, especially the unusually high maximum heart rate.

This demonstrated that Isolation Forest can detect unusual **combinations of features**, rather than simply looking for one extreme value.

## Final Comparison

| Technique        | Main Purpose                               | What It Revealed                                   |
| ---------------- | ------------------------------------------ | -------------------------------------------------- |
| PCA              | Dimensionality reduction and visualization | Global variance and broader structure              |
| t-SNE            | Visualization                              | Local neighborhoods and clearer cluster separation |
| Isolation Forest | Anomaly detection                          | Unusual multivariate observations                  |

Overall, this day showed how different unsupervised-learning techniques can be used together. **PCA and t-SNE help us understand the structure of high-dimensional data, while Isolation Forest helps identify observations that behave differently from the majority.**

The detected anomalies should be interpreted as **statistically unusual observations**, not automatically as errors or medical diagnoses.


[Day 4 Hands-on Lab](hands-on-lab.ipynb)
