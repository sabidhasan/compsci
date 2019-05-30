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

Monte Carlo simulations use **inferential statistics** of a **representative sample** from some **population** to estimate some value. Key concept is that the sample picked (randomly) is a representative subset of the population.

Confidence in results depends on two factors:

- **Sample size** (how many samples)
- **Variance** (how tight are the numbers)

Higher variance requires a larger sample size for a similar confidence level:

- Flipping 100 heads in a row is not the same as flipping 2 heads in a ro

- Variance is defined as sum of differences from mean divided by size of population:
  $$
  variance(X) = \frac{\sum_{x\epsilon X}^{} (x - \mu)^2}{|X|}
  $$
  **Standard deviation** is square of the mean

$$
\sigma = \sqrt{variance}
$$

- The **Emipirical Rule** (confidence interval) adds a better measure of the certainty than std dev alone. The 95% confidence interval is whatever lies within **1.96 standard deviations** of the mean. Assumes gaussian distribution

The **Law of Large Numbers** (or Bernoulli's Law) - as the number of trials increases, the measured probability goes to actual probability. For example: *Even if 10 coin flips have 2 heads, then 1,000,000 should have 500,000.*

Also the **Regression to the Mean** - if an extreme event happens randomly, the next random event should be less extreme. For example: *If 10 coin flips have 0 heads, the next 10 will have 5 heads (which is MORE THAN the 0 heads we just got).*

**Gamblers fallacy** - if an extreme event occurs, then the future is likely to *even out* the results so they become equal to the average. For example: *If 10 flips have 0 heads, the next 10 will have 0 tails.*



