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

| Input Type | Meaning of Input Size                                        |
| ---------- | ------------------------------------------------------------ |
| Number     | Magnitude                                                    |
| List       | Length of list                                               |
| Other      | e.g. for a **Tree**, it is Number of nodes in the tree / height of the tree |

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





## Lecture 20 - Linked Lists

A **linked list** is a sequence that is either empty, or contains a *value*, and a pointer/reference to the *rest* of the linked list. The last element in the chain of the linked list's *rest* propery points to an empty linked list.

Linked lists are designed to excel in areas where not much mutation of values is needed, or the list is created incrementally. Generally, traversal of linked lists (e.g. getting the length) is done using recursive functions.



A Binary Tree can be implemented using a Linked List.
**Pruning** a tree refers to removing some branches from a tree



**Sets** can be represented as **binary search trees**. Here, each node has at most two branches. Rules for binary search trees:

- Left branch elements are always smaller than the parent label
- Right branch is always bigger than parent label

Searching a BST is a `O(log n)` procedure, assuming the tree is **balanced**, meaning each subtree has roughly same number of nodes. The same tree can be represented in various ways:

![image-20200405223921899](/Users/abidhasan/Drive_old/Programming/compsci/CS61A/assets/image-20200405223921899.png)



## Lecture 21 - Ordered Sets

Set functions:

- **Union**: return new set with elements in either
- **Intersection**: return new set which contains elements in both
- **Adjoin**: return new set with an element added

