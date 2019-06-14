## Lecture 4 - Stochastic Thinking

**Deterministic Programs** - the same input leads to same output for a program.

**Stochastic Process** - any process where state depends on some random element. Generally, we can simulate stochastic processes more easily than computing them. Independent events in a stochastic system are those wherein one event has no impact on another (e.g. dice roll). Here are three laws of stochastic processes:

- Probabilities always range from 0 to 1.
- If probability of something happening is `p`, the probability of it not happening is `1-p`.
- **Multiplicative Law**: Probability of all <u>independent</u> events occuring is the *product* of probability of each event. Only applies if events are independent of each other.

Python's `random` library is predictively non deterministic, as it uses a seed based on time.

## Lecture 5 - Random Walks

**Random walks** are a special type of stochastic process wherein an agent *walks* (changes its position) a certain number of steps in each cycle. Brownian motion is an example.

When simulating a random walk, always run **sanity checks**, to determine if the model is not giving unexpected results.

Scientific Python Libraries

- numpy
- scipy
- matplotlib - great for plotting!

## Lecture 6 - Monte Carlo Simulations & Statistics

Monte Carlo simulations use **inferential statistics** of a **representative sample** from some **population** to estimate some value. Key concept is that the sample picked (randomly) is a representative subset of the population. Calculate **confidence intervals** from a large number of random trials, by applying **Empirical Rule**.

Confidence in any random simulation depends on two factors:

- **Sample size** (how many samples), which is part of **Bernoulli's Law** (states that probability of something is reality if infinite trials)
- **Variance** (how tight are the numbers); high variance requires a larger sample size for a similar confidence level

-----

**Statistical Definitions**:

- **Variance** - how diversely distributed a sample is from the average

$$
variance = \frac{\sum_{x\epsilon X}{(x - \mu)^2}}{X}
$$

- **Standard deviation** is square of $\mu$; it is used as it is in same units as original data

$$
\sigma = \sqrt{variance}
$$

- **Coefficient of Variation** is the variance adjusted for the mean. It is used to compare different  when  averages are different.

------

**Trends in Stochastic Processes**:

- The **Regression to the Mean** - if an extreme event happens randomly, the next random event should be less extreme. For example: If 10 coin flips have 0 heads, the next 10 will have 5 heads (which is MORE THAN the 0 heads we just got).

- The **Law of Large Numbers** (or Bernoulli's Law) - as the number of trials increases, the measured probability goes to actual probability. For example: *Even if 10 coin flips have 2 heads, then 1,000,000 should have 500,000.*

- **Gamblers fallacy** - if an extreme event occurs, then the future is likely to *even out* the results so they become equal to the average. For example: *If 10 flips have 0 heads, the next 10 will have 0 tails.*

Monte Carlo simulations can be used for real world phenomena - for example digits of pi can be determined using a MC simulation.

## Lecture 7 - Confidence Intervals

The `random.gauss` function produces a random number from gaussian distributed data centered at a given average.

A **probability distribution** is a histrogram showing probability for a result vs. how often that result occurs. Probabilities can be discrete or continuous, in the latter case they are described by a **probability density function**. This graphs the derivative of the cumulative distribution function. The area under the curve is the probability.

The **Empirical Rule** says that 1.96 standard deviations of the mean has 95% of the probability for normal distribution.

Not all data has **normal distribution** as for example a single spin of a roulette wheel. Here are other distributions:

- **Continuous Uniform Distribution** - where probability is evenly spread in some interval (e.g. how much time left till bus arrives)
- **Discrete Uniform Distribution** - where probability is evenly spread, but can only take certain values (e.g. dice roll, an example of **binomial distribution**)
- **Exponential distribution** occurs for phenomena that change exponentially.

But over a large data set, the **Central Limit Theorem** holds even for random events that are independent (because edge cases are unlikely):

- The means of the samples in a set of samples will be normally distributed
- The mean of the means will be close to the mean of the population
- The variance of the sample mean will be close to variance of the population

The 95% **confidence interval**  says that we will get the same **RELATIVE** interval 95% of the time when running a simulation. The actual value (or *where* the average lies) is beyond statistics as that is rooted in physical phenomena.
For example, calculating π by dropping needles in a circle-in-a-square, the value determined will be more or less (but not identically) the same, as it factually approaches the answer as inifinity needles are dropped.

## Lecture 8 - Sampling and Standard Error

**Probability sampling** - each member of the population has some probability of getting picked. But, how do we know how many to pick to make representative sample?

In a large data set (*population*), picking *x* members randomly over many trials (*samples*), will produce:

- A normal distribution of the average of these samples
- The average of any sample will equal the average of populations

Th is dictated by the **Central Limit Theorem**. However, if the above's confidence inverval is too big, increase the sample size. 

Realistically, you can't pick many members at random many times to then calculate the average and get the 95% confidence interval of the mean (for example, can't conduct political poll 1000 times). For this, we use the **standard error of the mean**, which allows estimating confidence interval of mean.
$$
SEM = \frac{\sigma}{\sqrt{n}}
$$

$$

$$

where $\sigma$ is the st. dev of the *population*, and n is the number of samples. However, st dev of the sample, actually roughly tracks the st dev of the population if sample size is large enough.

How good this approximation is depends on **skew** - or how evenly distributed the population is. The **sample size** actually doesn't matter for SEM much!

- Choose sample size based on skew and pick random sample from population
- Calculate µ and $\sigma$ (per central limit theorem, µ = population µ)
- Assume $\sigma$ for sample roughly = $\sigma$ for population, and estimate the SEM
- Use SEM to get 95% confidence intervals



