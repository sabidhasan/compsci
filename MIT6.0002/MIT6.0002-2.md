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
- matplotlib



  	