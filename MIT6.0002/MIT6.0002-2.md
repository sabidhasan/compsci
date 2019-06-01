## Lecture 4 - Stochastic Thinking

**Causal Non Determinism** - behavior of the physical world cannot be predicted with complete certainty.

**Predictive Non Determinism** - though many things *are* certain, our knowledge is limited in many cases, so treat things are unknowns.

**Stochastic Process** - any process where state depends on some random element :game_die:. Generally, we can *simulate* stochastic processes more easily than computing them. Here are three laws of stochastic processes:

- Probabilities always range from 0 to 1.
- If probability of something happening is `p`, the probability of it not happening is `1-p`.
- **Multiplicative Law**: Probability of all <u>independent</u> events occuring is the *product* of probability of each event. Only applies if events are independent of each other.

Python's `random` library is predictively non deterministic, as it uses a seed based on time.

## Lecture 5 - Random Walks

**Random walks** are a special type of stochastic process wherein an agent *walks* (changes its position) a certain number of steps in each cycle.

When simulating a random walk, always run **sanity checks**, to determine if the model is not giving unexpected results.

Scientific Python Libraries

- numpy
- scipy
- matplotlib - great for plotting!

## Lecture 6 - Monte Carlo Simulations & Statistics

Monte Carlo simulations use **inferential statistics** of a **representative sample** from some **population** to estimate some value. Key concept is that the sample picked (randomly) is a representative subset of the population. Calculate **confidence intervals** from a large number of random trials, by applying **Empirical Rule**.

Confidence in results depends on two factors:

- **Sample size** (how many samples)
- **Variance** (how tight are the numbers)

Higher variance requires a larger sample size for a similar confidence level:

- Flipping 100 heads in a row is not the same as flipping 2 heads in a row

- Variance is defined as sum of differences from mean divided by size of population:
  $$
  variance(X) = \frac{\sum_{x\epsilon X}^{} (x - \mu)^2}{|X|}
  $$
  **Standard deviation** is square of the mean

$$
\sigma = \sqrt{variance}
$$

- The **Emipirical Rule** (confidence interval) adds a better measure of the certainty than std dev alone. The 95% confidence interval is whatever range of *x* lies within **1.96 standard deviations** of the mean. Assumes Gaussian distribution.

The **Law of Large Numbers** (or Bernoulli's Law) - as the number of trials increases, the measured probability goes to actual probability. For example: *Even if 10 coin flips have 2 heads, then 1,000,000 should have 500,000.*

Also the **Regression to the Mean** - if an extreme event happens randomly, the next random event should be less extreme. For example: *If 10 coin flips have 0 heads, the next 10 will have 5 heads (which is MORE THAN the 0 heads we just got).*

**Gamblers fallacy** - if an extreme event occurs, then the future is likely to *even out* the results so they become equal to the average. For example: *If 10 flips have 0 heads, the next 10 will have 0 tails.*

Monte Carlo simulations can be used for real world phenomena - for example digits of pi can be determined using a MC simulation.

## Lecture 7 - Confidence Intervals

The `random.gauss` function produces a random number from gaussian distributed data centered at a given average.

**Probability Density Function** - a function that graphs the derivative of the cumulative distribution function. The area under the curve is the probability (the absolute #s on y-axis don't matter).

Not all data has **normal distribution** as for example a single spin of a roulette wheel. But over a large data set, the **Central Limit Theorem** holds even for random events that are independent (because edge cases are unlikely):

- The means of the samples in a set of samples will be normally distributed
- The mean of the means will be close to the mean of the population
- The variance of the sample mean will be close to variance of the population

The 95% **confidence interval**  says that we will get the same **RELATIVE** interval 95% of the time when running a simulation. The actual value (or *where* the average lies) is beyond statistics as that is rooted in physical phenomena.
For example, calculating π by dropping needles in a circle-in-a-square, the value determined will be more or less (but not identically) the same, as it factually approaches the answer as inifinity needles are dropped.

## Lecture 8 - Sampling and Standard Error

**Probability sampling** - each member of the population has some probability of getting picked. But, how do we know how many to pick?

In a large data set (*population*), picking *x* members randomly over many trials (*samples*), will produce:

- A normal distribution over all samples (for example, the average)
- The average of the samples, will be = to average of populations

However, if the above's confidence inverval is too big, increase the sample size. 

Realistically, you can't pick many members at random many times to then calculate the average and get the 95% confidence interval (for example, cant conduct political poll 1000 time). For this, we use the **standard error of the mean**.
$$
SEM = \frac{\sigma}{\sqrt{n}}
$$
where $\sigma$ is the st. dev of the *population*, and n is the number of samples. However, st dev of the sample, actually roughly tracks the st dev of the population if sample size is large enough.

How good this approximation is depends on **skew** - or how evenly distributed the population is. The **sample size** actually doesn't matter for SEM much!

- Choose sample size based on skew and pick random sample from population
- Calculate µ and $\sigma$ (per central limit theorem, µ = population µ)
- Assume $\sigma$ for sample roughly = $\sigma$ for population, and estimate the SEM
- Use SEM to get 95% confidence intervals









