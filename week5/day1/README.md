## Day 1: K-Means Clustering

On Day 1 of Week 5, I started learning about **Unsupervised Learning** and how it is different from the supervised learning techniques I worked with in the previous weeks.

In supervised learning, the model learns from features `X` together with a known target `y`. In unsupervised learning, there is no target label. The model only receives `X` and tries to discover hidden patterns or structure in the data.

I learned that one of the main unsupervised learning tasks is **clustering**, where similar data points are grouped together without predefined classes.

I also learned how **K-Means clustering** works:

* Choose the number of clusters `k`.
* Initialize cluster centers called **centroids**.
* Assign each data point to the nearest centroid.
* Move each centroid to the mean position of the points assigned to it.
* Repeat the process until the clusters become stable.

Another important thing I learned is that K-Means is based on distance, so the features should be scaled before clustering. I used `StandardScaler` to make sure that features with larger ranges do not dominate the clustering process.

[Day 1 Learning](./day1.ipynb)

For the hands-on lab, I used the **Iris dataset** with its four numeric features and applied K-Means without using the real flower species labels.

I:

* Loaded and explored the dataset.
* Confirmed that it contained **150 rows**, **4 numeric features**, and no missing values.
* Scaled the features using `StandardScaler`.
* Ran K-Means for values of `k` from **1 to 10**.
* Used the **Elbow Method** to compare the inertia values.
* Identified `k = 2` and `k = 3` as the main candidates.
* Compared them using the **Silhouette Score**.
* Selected `k = 2` because it had the higher silhouette score.
* Fitted the final K-Means model.
* Visualized the discovered clusters using petal length and petal width.
* Examined the cluster averages to understand what each group represented.

The silhouette scores were:

* `k = 2`: **0.581750**
* `k = 3`: **0.459948**

Because a higher silhouette score represents better-separated clusters, I selected **2 clusters**.

The final model divided the dataset into:

* **Cluster 0:** 100 flowers
* **Cluster 1:** 50 flowers

Cluster 0 contained flowers with generally larger petals, while Cluster 1 contained flowers with much smaller petal measurements.

This lab helped me understand that clustering is different from classification because the model is not trying to predict a known answer. Instead, it discovers groups based only on similarities between the data points.

[Hands-on Lab](./hands-on-lab.ipynb)

I also learned that choosing the number of clusters should not depend on only one method. The **Elbow Method** gives a visual indication, while the **Silhouette Score** provides a numerical way to compare possible cluster values.

**Day completed.**
