## Lecture 9 - Understanding Experimental Data

**Objective functions** are used to determine how good of a fit a model is for data. For data, a **least squares method** can be used to judge how good a fit some model is:
$$
Objective\_Function = \sum_{i=0}^{len(data)}{(observed[i] - predicted[i])^2}
$$
To minimze this objective function, use **linear regression**:

- All best fit functions (in 2D this is all lines) can be represented on a 2D axis - in teh case of a line $y = mx + b$, the x-axis holds all a values, and the y axis all b values.
- Put a surface over this 2D space, where the height of the surface at point (a, b) is the solution of the objective function using (a, b). Because we used squares in objective function, there is only one surface minimum.
- The lowest point on that surface is the best (a, b) for fitting data
- To find lowest, start randomly and walk downhill until no more downhill possible.

`pylab.polyfit` can do linear regression, by giving coefficients that describe the polynomial.

To determine how good  fit a model is, you could:

- Use objective function ($\Sigma$ (observed[i] - predicted[i])$^2$ ) to compare two models relatively

- Use R$^2$ value (guaranteed to be from 0 to 1):
  $$
  R^2 = 1 - \frac{\sum(y_i - p_i)^2}{\sum_i(y_i - \mu)^2}
  $$
  



