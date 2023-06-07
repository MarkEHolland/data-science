# Quantile Regression

- Used for *regression* problems
- provides a more correct uncertainty estimation than just mean squared error (e.g point at (x=5, y=10), error can be ymax=11, ymin=9, at (x=6, y=12), error ymax=15, ymin=10
- this makes it more useful to business (E.g predicting when an order is likely to arrive as well as the upper bound of the latest it should get to a customer)

## Objective function

- in most ML problems, we minimize a loss (ie objective) function to get our algorithm to predict as accurately possible. Some common loss functions are RMSE/MAE (regression), cross entropy/log loss (classification)— that this is calculated over all the data points using y_true - y_predicted
- For ordinary least squares linear regression we minimize squared loss L

$$ L = (y - (\theta_{0} + \theta_{1}X_{1} + \theta_{2}X_{2} + ...))^{2} $$

where y is y_true and $(\theta_{0} + \theta_{1}X_{1} + \theta_{2}X_{2} + ...)$ is the y_predicted

- for quantile regression, we minimise the absolute error, scaled by the quantile $\tau$ (e.g. 0.75 for the 75th quantile, tau is always between 0 and 1

$$
\begin{align}L &=\begin{cases}\tau(y - X\theta), \; if \; y - X\theta \geq 0 \\(\tau - 1)(y - X\theta), \; if \; y - X\theta < 0\end{cases}\end{align}
$$

The first line in the above conditions is for positive error, ie y_true > y_predicted, the second line is for negative error, ie y_true < y_predicted. since **Loss should always be positive,** we have the $(\tau -1 )$ factor in the 2nd condition (the -ve of tau -1 cancels out the -ve error to give positive loss)

************************************Scaling factor tau************************************

Plotting the loss vs prediction and vs the error: (assuming a true value of y=0)

- note that the plot is flipped left and right on the x=0 when we swap the xaxis from error to y_pred (for y_pred > 0, the error is -ve since error is defined as y_true - y_pred

loss vs y predicted

![Screenshot from 2023-04-01 22-43-01.png](data-science/images/ypred_vs_quantile.png)

loss vs error

![](2023.04.04.quantile_regression/yerror_vs_quantile.png)


The scaling factor of tau is to compensate for where we want the prediction to be. For example if we are predicting the 90th percentile, we expect the true value to lie below this, so if we predicted a higher value for the y, then it will approach closer to the 90th percentile, so we want a lower loss. 

e.g. if the true relation is y = x, and we have a bunch of training data points. at x = 0, the data points we have are 1,2,10, 1000, then the 90th percentile is 703. If we predict 700 as the 90th percentile, this is more accurate than if we predict 1 as the 90th percentile, and thus 700 (higher y_predicted and ****************************negative error**************************** will have lower loss . However, if we predict 0.5, this is very far from the 90th percentile, so it should have greater loss, even though it is closer to the true value of 0

## Mean vs Median

## Gradient boosting basics

- Most commonly we use gradient boosting with **decision trees** although any other ‘weak’ learner will do
- the weak learners are learned **sequentially**
    - 1st tree fit the target variable, you then calculate the residual
    - 2nd tree learn the residual (how much you should add/subtract from the 1st tree’s result to reduce loss)
    - etc etc
- 

**drawbacks of basic algo**

- the split in the decision tree for each step is done by brute force, so time consuming
- lightgbm speeds this up by using gradient-based one-side sampling — ie for data points that have low loss derivative (so they are not providing much info for the model to optimise), the model does a sample of these rather than use all of it to save time

## LightGBM implementation

- lightGBM has native support for quantile regression a lot longer than xgb
- tree based gradient boosting is greedy— it minimizes the loss at each step and does not consider whether it contributes to an overall smaller loss (ie local minimimum rather than global minimum)
- say you have 10 data points in a node— the node will take on one value that minimizes the loss function (e.g. squared error loss for regression etc) — e.g. if 4 points y1 to y4 i [1,2,3,4], and you pick y_node as 3, the squared loss is `np.power((np.array([1,2,3,4]) -3 ), 2).sum()`
- for each split in the tree, it will find the data points to put in each side which minimises the quantile loss
- 
- we then calculate the residuals
- gradient boosting approximates the loss function(objective) with a 2nd order [Taylor expansion](https://en.wikipedia.org/wiki/Taylor_series)— this is because we have to sum up the loss over all the trees and for a more complex loss function such as the logistic loss, this saves a lot of compute time
- since the estimation is dependent on up to the 2nd derivative, if the second derivative is 0 (as in quantile loss’s case, you have to make some tweaks to find the correct value of y that minimises the loss)
- Loss function of quantile regression has **************************************************************************zero in the 2nd derivative everywhere************************************************************************** (compared to RMSE which has a constant for the 2nd derivative)— **this means a naive implementation of the quantile loss in GBDT is likely to lead to poor results**
- Lightgbm improvement for quantile regression: **grow the trees as normal,** but then when the tree is grown, actually go back and re-compute the loss values in each leaf so that the value of y for that node minimize the true loss function instead of the second order approximation.

## Real life applications

- instacart [https://tech.instacart.com/how-instacart-delivers-on-time-using-quantile-regression-2383e2e03edb](https://tech.instacart.com/how-instacart-delivers-on-time-using-quantile-regression-2383e2e03edb)
    - a customer’s orders have a set 1hr window to arrive
    - instacart can predict when a order is likely to arrive based on a variety of features, however, they also need to know the error (ie ETA_max ≤ promised order latest delivery time, eg. order for delivery 1-2pm window has to arrive before 2pm)
    - they can use a fixed buffer based on past performance (e.g. if model predicts ETA is 1.30pm, add in buffer of 10mins based on historic data, therefore this delivery can be accepted, since it’s before 2pm, but an estimated ETA of 1.51 cannot be accepted)
    - however, the buffer is likely to change with different conditions (eg an order that is for a off peak window, say 10am in the morning when the traffic and shops are quiet), the buffer can be smaller since you are more certain of arrival times
    - quantile regression allows you to calculate this dyanmic bounds— you predict the ETA + 90th percentile

### Resources

[https://ethen8181.github.io/machine-learning/ab_tests/quantile_regression/quantile_regression.html#Objective-Function](https://ethen8181.github.io/machine-learning/ab_tests/quantile_regression/quantile_regression.html#Objective-Function)


### Gradient boosting links

- [https://www.numpyninja.com/post/gradient-boost-for-regression-explained](https://www.numpyninja.com/post/gradient-boost-for-regression-explained) — nice walkthrough of regression using GBM
- [https://xgboost.readthedocs.io/en/stable/tutorials/model.html](https://xgboost.readthedocs.io/en/stable/tutorials/model.html)
- [https://stats.stackexchange.com/questions/202858/xgboost-loss-function-approximation-with-taylor-expansion](https://stats.stackexchange.com/questions/202858/xgboost-loss-function-approximation-with-taylor-expansion)
- [https://jmarkhou.com/lgbqr/](https://jmarkhou.com/lgbqr/)


