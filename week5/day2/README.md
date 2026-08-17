# Day 2 — DBSCAN & Hierarchical Clustering

Today, I continued learning about **unsupervised learning** by exploring two clustering methods that work differently from K-Means: **DBSCAN** and **Hierarchical Clustering**.

## What I Learned

I started by reviewing **K-Means** and its main limitations.

K-Means requires the number of clusters `k` to be chosen before training, works best when clusters are relatively compact and similarly shaped, and assigns every data point to a cluster even when a point may actually be an outlier.

This introduced me to **DBSCAN**, a density-based clustering algorithm.

Unlike K-Means, DBSCAN does not require the number of clusters to be specified in advance. Instead, it looks for dense regions in the dataset.

I learned about its two main parameters:

* `eps`: controls how close points must be to be considered neighbors.
* `min_samples`: controls how many nearby points are required for an area to be considered dense.

One important feature of DBSCAN is its ability to detect **noise points**. These points receive the label `-1` instead of being forced into a cluster.

I also learned about **Hierarchical Clustering**.

Instead of choosing a fixed number of clusters at the beginning, hierarchical clustering starts with individual observations and progressively combines them into larger groups.

The result can be visualized using a **dendrogram**, which shows the order and distance at which clusters are merged.

By selecting a cut height on the dendrogram, we can decide how many final clusters we want.

I used **Ward linkage**, which tries to merge clusters while minimizing the increase in within-cluster variance.

## Hands-On Lab

For the hands-on lab, I applied **K-Means, DBSCAN, and Hierarchical Clustering** to the same **Iris dataset** so I could compare how each method grouped the same observations.

### DBSCAN

I used:

```python
DBSCAN(
    eps=0.5,
    min_samples=5
)
```

The result was:

* **2 clusters**
* **17 noise points**
* Cluster 0: **49 points**
* Cluster 1: **84 points**

The remaining 17 observations were classified as noise instead of being forced into one of the clusters.

### Hierarchical Clustering

I created a dendrogram using **Ward linkage** and selected a cut height of:

```text
10
```

This produced:

* **3 clusters**

The dendrogram helped me understand how the observations were progressively merged and how changing the cut height changes the final number of clusters.

### K-Means Comparison

For comparison, I also ran K-Means with:

```python
n_clusters=3
```

K-Means produced:

* **3 clusters**
* **0 noise points**

Unlike DBSCAN, every observation had to belong to one of the three clusters.

## Final Comparison

| Method                  | Clusters |            Noise Points |
| ----------------------- | -------: | ----------------------: |
| K-Means                 |        3 |                       0 |
| DBSCAN                  |        2 |                      17 |
| Hierarchical Clustering |        3 | Not explicitly detected |

I also used **PCA** to reduce the four Iris features to two dimensions so I could visualize the cluster assignments from all three methods side by side.

The comparison showed that different clustering algorithms can give different interpretations of the same dataset because each algorithm defines a cluster differently.

K-Means focuses mainly on distance from centroids, DBSCAN focuses on density, and Hierarchical Clustering focuses on relationships between observations and groups.

For this dataset, **DBSCAN can be a strong choice when the detected sparse observations are meaningful outliers**, because it can identify them as noise instead of forcing them into a cluster.

However, the comparison also showed that there is not always one universally correct clustering method. The best method depends on the structure of the data and what we want to discover.

[Day 2 Learning](day2.ipynb)

[Day 2 Hands-on Lab](hands-on-lab.ipynb)
