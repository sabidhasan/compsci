## Lecture 19 - Growth

Classic Fibonacci has a tree-growth, thereby making it qute inefficient.

Complexity consists of **space** and **time**.

Space complexity grows with number of functions that are currently active - number of frames currently active. For example, for recursive Fibonacci, until the base case is reached, all the parents are active:

> The depth of a tree-recursive algorithm is the depth of the algorithm

**Memoization**: allows improving many algorithms. It *caches* expensive calculations so they can be returned rather than recomputed. 
"Remember the results that have been computed before"
Memoization can only work for *pure functions*



The **order of growth** of a process dictates how quickly it consumes resources when given more complex inputs. To quantify this:
$$
R(n) = \Theta(f(n))
$$
where $\Theta$ is some function that abstracts complex, input-specific growth factors, and generalizes the input vs. the actual growth (*R*). **Theta notation** or big O notation is used to qualify this - what function models the average growth for a method as a function of input.



Rules:

- Constants don't affect order of growth
- Logarithm's base doesn't matter (relatively the same)
- Nested loops multiply growth
- Only the highest order term is kept ($\Theta$(n + n<sup>2</sup>) = $\Theta$(n<sup>2</sup>))

| **Category** | **Theta Notation**      | **Description**                                 |
| ------------ | ----------------------- | ----------------------------------------------- |
| Constant     | $\Theta$(1)             | Independent of input                            |
| Logarithmic  | $\Theta$(log n)         | Multiplying inputs increments growth constantly |
| Linear       | $\Theta$(n)             | Adding inputs increments growth constantly      |
| Quadratic    | $\Theta$(n<sup>2</sup>) | Adding inputs adds growth quadratically         |
| Exponential  | $\Theta$(2<sup>n</sup>) | Adding resources multiplies growth              |

