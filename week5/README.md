## Week 5

### Day 1: K-Means Clustering

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
