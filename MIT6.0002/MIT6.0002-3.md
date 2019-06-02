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

- Use objective function ( $\Sigma$ (observed[i] - predicted[i])$^2$ ) to compare two models relatively

- Use R$^2$ value (guaranteed to be from 0 to 1):
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



