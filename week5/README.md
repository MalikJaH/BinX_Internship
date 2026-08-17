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
