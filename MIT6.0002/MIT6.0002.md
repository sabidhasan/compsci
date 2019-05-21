## Lecture 1 - Optimization Problems

**Optimization problem** - optimize an *objective function* that needs to be maximized or minimized, given some *constraints*. Example - shortest path from A to B, or the knapsack problem.



**Knapsack Problem**

A knapsack that only holds a finite amount (constraint) needs to be filled with stuff to maximze items (objective function). There are two flavors:

- *Fractional knapsack* - a fraction of each item can be taken. This can be solved with a **greedy algorithm**. Take as much of the most expensive as possible, and continue until space runs out.
- *0/1 knapsack* - each item can either be taken or not, no fractions

**0/1 Knapsack** can be programatically represented:

- Knapsack has a max capacity of `w`
- Each item is represented by `<value, weight>`
- A vector `I` represents the set of all possible items
- A vector `V` represents the items that have been taken

Unfortunately, the knapsack problem is `O(2^n)` at best. To solve this problem, here are possible solutions:

- **All Possibilities:** Generate a **power set** which is all possible combinations. Remove combinations with too high weight, and get one that maximizes the weight. Unfortunately, this yields way too many possibilities.
- **Greedy Algorithm**: Picks stuff in order of most valuable to least valuable. Efficiency for this is `O(n log n)`. Greedy algorithms only use *local optimization*, meaning they don't care what future implications of their choices are.
- 





