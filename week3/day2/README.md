# Day 2 - Week 3: Linear Regression

In this day of training, I learned the fundamentals of **Linear Regression** and how a regression model finds a line that best describes the relationship between input and output values.

I first worked through a small example using weeks and car sales to understand the mathematics behind the regression line before using Scikit-learn.

## Understanding the Regression Line

A simple linear regression model can be represented as:

`y = mx + c`

Where:

* `y` is the predicted value.
* `x` is the input feature.
* `m` is the slope of the line.
* `c` is the intercept.

I learned how to calculate the mean of both `x` and `y` and use the differences from those means to calculate the slope.

The slope can be calculated using:

`m = Σ((x - x̄)(y - ȳ)) / Σ((x - x̄)²)`

After calculating the slope, the intercept can be calculated using:

`c = ȳ - mx̄`

This helped me understand how Linear Regression mathematically finds the best-fit line.

## Residuals

I also learned about **residuals**.

A residual is the difference between the actual value and the value predicted by the regression line.

In simple words:

`Residual = Actual Value - Predicted Value`

A good regression line tries to make these errors as small as possible across the dataset.

## Hands-On Lab

For the practical tasks, I used the **California Housing dataset** and trained a `LinearRegression` model to predict median house values.

I completed the following steps:

1. Loaded the California Housing dataset.
2. Separated the features from the target variable.
3. Split the dataset into training and testing sets.
4. Trained a Linear Regression model.
5. Examined the model coefficients.
6. Generated predictions on unseen test data.
7. Evaluated the model using:

   * MAE
   * RMSE
   * R²
8. Created a simple baseline model that predicts the training-set mean for every test sample.
9. Compared the Linear Regression RMSE against the baseline RMSE.
10. Interpreted the final results.

## Regression Evaluation Metrics

### MAE

**Mean Absolute Error** measures the average size of the prediction errors.

It is easy to interpret because it uses the same units as the target variable.

### RMSE

**Root Mean Squared Error** also measures prediction error, but it gives more weight to larger mistakes.

Because of this, RMSE is often larger than MAE.

### R²

**R²** measures how much of the variation in the target variable can be explained by the model.

An R² closer to `1.0` indicates that the model explains more of the variation in the data.

## Results

The Linear Regression model achieved approximately:

* **MAE:** 0.533
* **RMSE:** 0.746
* **R²:** 0.576

This means that the model explained approximately **57.6% of the variation** in median house values.

The baseline model achieved an RMSE of approximately **1.145**, while the Linear Regression model achieved a lower RMSE of approximately **0.746**.

Therefore, the Linear Regression model performed better than simply predicting the mean house value for every observation.

## What I Learned

This day helped me understand both the mathematics behind Linear Regression and how to apply it using Scikit-learn.

I practiced:

* Linear Regression
* The equation `y = mx + c`
* Mean-centered values
* Calculating slope and intercept
* Residuals
* Model coefficients
* Train/test splitting
* MAE
* RMSE
* R²
* Baseline comparison
* Evaluating whether a regression model adds value

**Day 2 - Week 3 Completed**
