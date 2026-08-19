# Week 5

## Day 1: K-Means Clustering

This week, I started learning about **Unsupervised Learning** and how it differs from the supervised learning methods I used in the previous weeks.

In supervised learning, the model learns from both the input features `X` and a known target `y`. In unsupervised learning, there is no target variable. The model only receives the features and tries to discover hidden structure in the data.

I learned about **clustering**, which groups similar data points together without having predefined labels.

I then studied **K-Means**, one of the most common clustering algorithms. K-Means works by assigning points to the nearest cluster centroid and repeatedly updating the centroid positions until the clusters become stable.

I also learned why scaling is especially important for K-Means. Since the algorithm uses distance, features with larger ranges can have too much influence on the result. I used `StandardScaler` to place all features on a similar scale.

For the hands-on lab, I applied K-Means to the **Iris dataset** using only its four numeric features and without using the real flower species labels.

I ran K-Means for values of `k` from 1 to 10 and used the **Elbow Method** to examine how inertia changed as the number of clusters increased.

The elbow results suggested that `k = 2` and `k = 3` were reasonable candidates.

I then compared these values using the **Silhouette Score**:

* `k = 2`: **0.581750**
* `k = 3`: **0.459948**

Since `k = 2` had the higher silhouette score, I selected it as the final number of clusters.

The final model divided the 150 flowers into:

* **Cluster 0:** 100 flowers
* **Cluster 1:** 50 flowers

By examining the cluster averages and visualization, I found that Cluster 0 contained flowers with generally larger petals, while Cluster 1 contained flowers with much smaller petal measurements.

[Day 1 Hands-on Lab](day1/hands-on-lab.ipynb)

This first day helped me understand the main idea behind unsupervised learning: instead of predicting a known target, the model tries to discover meaningful structure directly from the data.

It also introduced me to two important methods for choosing the number of clusters: the **Elbow Method** and the **Silhouette Score**.

---

## Day 2: DBSCAN & Hierarchical Clustering

On Day 2, I explored two additional clustering methods: **DBSCAN** and **Hierarchical Clustering**, and compared them with K-Means.

I first reviewed some of the limitations of K-Means. K-Means requires `k` to be selected before training, works best with relatively compact clusters, and assigns every observation to a cluster even if it is far away from the rest of the data.

I then learned about **DBSCAN**, which takes a different approach by looking for dense regions instead of cluster centroids.

The two main DBSCAN parameters I studied were:

* `eps`, which controls the neighborhood radius.
* `min_samples`, which controls how many nearby observations are needed to form a dense region.

A major advantage of DBSCAN is that it can explicitly detect **noise or outlier points** using the label `-1`.

I also learned about **Hierarchical Clustering**, which progressively combines observations into larger groups and represents this process using a **dendrogram**.

Instead of deciding the final number of clusters before building the model, I can inspect the dendrogram and choose a cut height.

For the hands-on lab, I applied all three clustering algorithms to the **Iris dataset**.

DBSCAN with `eps=0.5` and `min_samples=5` found:

* **2 clusters**
* **17 noise points**
* Cluster 0: **49 points**
* Cluster 1: **84 points**

For hierarchical clustering, I used **Ward linkage** and selected a dendrogram cut height of `10`, which resulted in:

* **3 clusters**

I also ran K-Means with `k = 3`, which produced three clusters but did not identify any noise because every point must belong to a cluster.

| Method       | Clusters |                   Noise |
| ------------ | -------: | ----------------------: |
| K-Means      |        3 |                       0 |
| DBSCAN       |        2 |                      17 |
| Hierarchical |        3 | Not explicitly detected |

I used **PCA** to reduce the four-dimensional Iris dataset to two dimensions and visualize the clustering results side by side.

This comparison helped me understand that clustering algorithms can produce different results on the same dataset because they use different definitions of what a cluster is.

* **K-Means** groups points based on their distance from centroids.
* **DBSCAN** discovers clusters based on density.
* **Hierarchical Clustering** builds relationships between observations and clusters progressively.

[Day 2 Learning](day2/day2.ipynb)

[Day 2 Hands-on Lab](day2/hands-on-lab.ipynb)

Day 2 helped me understand that selecting a clustering algorithm depends on the structure of the dataset. DBSCAN can be especially useful when noise or irregular cluster shapes are important, while hierarchical clustering provides a useful way to explore how observations are related at different clustering levels.

## Day 3: Dimensionality Reduction with PCA

On Day 3, I learned about **dimensionality reduction** and how **Principal Component Analysis (PCA)** can be used to reduce the number of features in a dataset while preserving as much useful information as possible.

I first studied the **curse of dimensionality**. As the number of features increases, the data becomes more sparse, distance measurements can become less meaningful, models may become more prone to overfitting, and visualization becomes difficult because data with more than three dimensions cannot be directly plotted.

Dimensionality reduction helps address these problems by representing the data using fewer dimensions.

I then learned how **PCA** works. Instead of selecting a subset of the original features, PCA creates new features called **principal components**.

Each principal component is a linear combination of the original features, and the components are ordered according to the amount of variance they explain:

* `PC1` captures the largest amount of variance.
* `PC2` captures the next largest amount of variance.
* Additional components capture progressively smaller amounts of variance.

Before applying PCA, I used `StandardScaler` because PCA is based on variance. Without scaling, features with larger numerical ranges could dominate the principal components even if they are not more important.

For the hands-on lab, I applied PCA to a synthetic cardiac-style dataset containing **1,215 observations** and the following six numerical features:

* `age`
* `resting_bp`
* `cholesterol`
* `bmi`
* `fasting_blood_sugar`
* `max_heart_rate`

After scaling the data, I fitted PCA using all six possible components and examined the **explained variance ratio**.

The variance explained by each component was:

| Component | Explained Variance |
| --------- | -----------------: |
| PC1       |             33.37% |
| PC2       |             17.83% |
| PC3       |             15.71% |
| PC4       |             14.22% |
| PC5       |             12.96% |
| PC6       |              5.90% |

I then calculated the **cumulative explained variance**:

| Number of Components | Cumulative Variance |
| -------------------: | ------------------: |
|                    1 |              33.37% |
|                    2 |              51.20% |
|                    3 |              66.92% |
|                    4 |              81.13% |
|                    5 |              94.10% |
|                    6 |             100.00% |

I plotted the cumulative explained variance against the number of components and used a **95% variance threshold** to determine how many components should be retained.

Five components preserved **94.10%** of the total variance, which was slightly below the required 95% threshold. Therefore, all six components were required to preserve at least 95% of the variance.

This meant that, for this dataset, PCA did not provide meaningful dimensionality reduction when using a strict 95% threshold:

* Original features: **6**
* Components required for at least 95% variance: **6**
* Total variance retained: **100%**

This result showed me that PCA does not always significantly reduce the number of dimensions. In this case, the six original features contained enough distinct information that removing one complete principal component would cause the retained variance to fall below 95%.

I also reduced the dataset to **two principal components** for visualization.

The first two components retained:

* `PC1`: **33.37%**
* `PC2`: **17.83%**
* Total retained variance: **51.20%**

I plotted `PC1` against `PC2` in a 2D scatter plot and colored the points using the known `cardiac_risk` group.

The `cardiac_risk` variable was not included as an input to PCA. It was only used after the transformation to help visually inspect whether the known groups showed any separation in the reduced space.

Reducing the data from six dimensions to two dimensions made visualization possible, but it also meant that approximately **48.80% of the original variance was not represented in the plot**.

This helped me understand an important trade-off in PCA:

* Keeping more components preserves more information.
* Keeping fewer components provides stronger dimensionality reduction and easier visualization.
* Principal components are harder to interpret because they are combinations of the original features.

[Day 3 Hands-on Lab](day3/hands-on-lab.ipynb)

Day 3 helped me understand that PCA is not simply about reducing the number of columns. The main goal is to find a smaller representation of the data while preserving as much of its variance as possible.

I also learned how to use the **explained variance ratio** and **cumulative explained variance** to decide how many components should be retained, and how PCA can be used to project high-dimensional data into two dimensions for visualization.

## Day 4: t-SNE & Anomaly Detection

On Day 4, I explored **high-dimensional visualization and anomaly detection** using t-SNE and Isolation Forest.

I applied **t-SNE** to reduce six numeric features into two dimensions and visualized the results using the K-Means cluster labels from Day 1. I then compared the t-SNE visualization with **PCA**, where t-SNE showed clearer local cluster separation while PCA provided a better view of the overall variance structure.

For anomaly detection, I used **Isolation Forest** with a contamination value of `0.05`. The model flagged **61 out of 1,215 observations (5.02%)** as potential anomalies.

Finally, I inspected the two strongest anomalies using their feature values and z-scores. Both observations had unusually high maximum heart rates, with z-scores above `+3`, along with other uncommon feature combinations.

### Key Takeaways

* t-SNE is useful for visualizing local structure in high-dimensional data.
* PCA and t-SNE reveal different aspects of the same dataset.
* Isolation Forest can detect unusual multivariate patterns without labeled anomalies.
* Flagged anomalies should be investigated rather than automatically treated as errors.

[Day 4 Hands-on Lab](day4/hands-on-lab.ipynb)

