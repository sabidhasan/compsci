## Lecture 9 - Understanding Experimental Data

**Objective functions** are used to determine how good of a fit a model is for data. If you have some model that makes predictions, we can judge how good a fit some model is with **least squares**:
$$
Objective\_Function = \sum_{i=0}^{len(data)}{(observed[i] - predicted[i])^2}
$$
To minimze this objective function, use **linear regression**:

- All best fit functions (for a 2D model, this is all possible *lines*) can be represented on a 2D axis - for a line $y = mx + b$, the x-axis holds all *a* values, and the y axis all *b* values.
- Put a surface over this 2D space, where the height of the surface at point (a, b) is the solution of the objective function - or model - which is using (a, b). Because we used squares in least squares, there is only <u>one</u> surface minimum.
- The lowest point on that surface is the best (a, b) for fitting data
- To find lowest, start randomly and walk downhill until no more downhill possible.

`pylab.polyfit` can do linear regression, by giving coefficients that describe the polynomial, for a given degree (of polynomial).

To determine how good  fit a model is, you could:

- Use least squares ( $\Sigma$ (observed[i] - predicted[i])$^2$ ) to compare two models relatively

- Use **R$^2$ value** (guaranteed to be from 0 to 1):
  $$
  R^2 = 1 - \frac{\sum(y_i - p_i)^2}{\sum_i(y_i - \mu)^2}
  $$
  

## Lecture 10 - Understanding Experimental Data

To find the best model, it doesn't always make sense to look at the best fit! Physical phenomena are typically linear or parabolic, not something like $x^{16} $! To solve this, and to avoid overfitting, it is important to do **cross validation**, and test prediction behavior.

**Overfitting** happens when the model is fitting to the noise! **Underfitting** happens when the model can't even fit to training data.

What's the harm of picking a higher order model if the coefficients are zeroed out anyway? The problem is that even a small amount of noise leads to massive prediction inaccuracy. Should pick the **simplest model** (lowest order polynomial) that cross validates.

Cross Validation can be one of the following. One common theme with all these is repeatitive training, because one model (especially with limited data) could lead to a false positive or false negative fit (you think the model is good or bad when its the opposite).

- **Leave One Out** cross validation - leave one data point out and build a model with the rest. Check how well the prediction is on the left-out point. Repeat for the entire data set, leaving out a different data point each time.
- **k-Fold** - same as LOO, except you divide data set into chunks, and leave one chunk out each time. Better for bigger data sets.
- **Repeated Random Sampling** - keep a random 20-50% of elements for testing, and keep the rest for sampling. Repeat a number of times

## Lecture 11 - Machine Learning

There are two learning methods:

- **Declarative knowledge** - or memorize facts
- **Imperative knowledge** - to deduce things

Basic ML paradigm:

- Training data is used to observe a phenomenon
- Build a model by training
- Predict something for test data

There are three types of ML paradigms:

- **Supervised Learning** - examples are labelled, you predict either classification or clustering (**k-NN**)
- **Unsupervised Learning** - examples are unlabelled; how to group them into clusters (**k-means**)
- **Reinforcement Learning** -system has freedom to make choices and given reward for choices

Need to choose which **features** to use to describe an example - adding too many features could lead to overfitting. Also, we will have to calculate the difference between two **feature vectors**. This is done with **Minkowski Matrix**:
$$
dist(X1,X2,p) = (\sum_{k=1}^{len}{|X1_k-X2_k|^p})^{(1/p)}
$$
When `p = 1`, this is the **Manhattan Distance** (sum of differences), and when `p = 2`, this is the **Euclidean Distance** (sum of differences, squared). Manhattan distance is called that because it only goes vertical/horizontally on a graph - no angles.

To test a model a **Confusion Matrix** is built. The positive and negative refer to what the model predicted, not what it actually is:

|                |                |
| -------------- | -------------- |
| TRUE POSITIVE  | FALSE POSITIVE |
| FALSE NEGATIVE | TRUE NEGATIVE  |

Can measure **model accuracy** using this, basically what percentage is correct/*true*.


$$
accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$


Also, there is **Sensitivity** (aka recall, or true positive rate) and **Specificity** (selectivity or true negative rate). Generally, these are a trade-off and a **ROC curve** is used to optimize one at another's cost:
$$
sensitivity = \frac{TP}{TP + FN}
$$

$$
specificity = \frac{TN}{TN + FP}
$$





