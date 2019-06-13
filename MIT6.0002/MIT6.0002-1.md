## Lecture 1+2 - Optimization Problems

**Optimization problem** - optimize an **objective function** that needs to be maximized or minimized, given some **constraints**. Example - shortest path from A to B, or the knapsack problem.

**Knapsack Problem**

A knapsack that only holds a finite amount (constraint) needs to be filled with stuff to maximze items (objective function). There are two flavors:

- *Fractional knapsack* - a fraction of each item can be taken. This can be solved with a **greedy algorithm**. Take as much of the most expensive as possible, and continue until space runs out.
- *0/1 knapsack* - each item can either be taken or not, no fractions

**0/1 Knapsack** can be programatically represented:

- Knapsack has a max capacity of `w`
- Each item is represented by `<value, weight>`
- A vector `I` represents the set of all possible items
- A vector `V` represents the items that have been taken (binary)

To solve this problem, here are possible solutions:

- **All Possibilities:** Generate a **power set** which is all possible combinations. Remove combinations with too high weight, and get one that maximizes the weight. Unfortunately, this yields way too many possibilities. Complexity is `O(2^n)`.

  *Pro* - actually solves the problem   |   *Con* - practically impossible

- **Greedy Algorithm**: Picks stuff in order of most valuable to least valuable. Efficiency for this is `O(n log n)`. Greedy algorithms use *local optimization* - don't care about future implications of choices.

  *Pro* - fast and easy				|				*Con* - may not give correct answer

- **Dynamic Programming** - if there are any **repetitions** in the knapsack, you can use *memoization* to speed the calculation up considerably. The general method is still the *All Possibilities* method.

**Search Trees** - when considering All Possibilities algorithm, a search tree with all possibilities is built (at each node, one branch is to take the item *n*, and the other branch is not take it). Recursively, it calls itself with a list of `itemsToConsider`, which decreases by 1 item at each call (seeing the possibility of taking or not taking the item). Complexity is `O(n x 2^n)`.

**Dynamic Programming** - DP is a way to solve complex problems that have overlapping subproblems, by **memoizing** answers, and prevent recalculations. The overlapping subproblems need to be the same operation with the same input (eg. a sort algorithm can't be DP'd)

Fibonacci and Knapsack problem are really well optimized with DP. For this, a **rooted binary tree** is built, which is a directed acyclic graph with:

- One Root
- Each node (except root) having one parent
- Each node having at most 2 children

At each node, record the items taken and the undecided items. This is the decision tree, for a knapsack with weight limit of 5:

![image-20190611215158185](/Users/abidhasan/Google Drive/Programming/compsci/MIT6.0002/assets/image-20190611215158185.png)

For the memo, we save the (length of items considered, available space) as key and the result as value.

## Lecture 3 - Graph Algorithms

Covers both **Depth First** and **Breadth First** search. Graphs are useful for representing e.g. family trees, maps, rail networks, etc., and are made of:

- **Node** or vertices (these are the points in the graph)
- **Edges** or arcs (these are the connections between nodes)

Graphs can be **directed** or *digraph* (information flows only one way) or **undirected** (information goes from source to destination and back). **Weighted graphs** have values associated with edges. Some graph problems are:

- **Shortest path** - path of edges and nodes to lead from start to end node
- **Shortest weighted path** - same as above, except weight is minimized
- **Maximum clique** - a clicque is a section of the graph wherein any two nodes are connected with an edge
- **Max Flow Min Cut** - a cut a list of edges such that if they are removed, a section of the graph becomes isolated.

To represent a graph programatically, make a `Node` class and an `Edge` class (contains a `source` and `destination` property, which  are `Node`s). Now, the graph can be represented via:

1. **Adjacency matrix** - this is a big matrix that has all nodes on X and Y axes and indicates if they are directly connected as Booleans.
2. **Adjacency List** - has a `Digraph` class, which uses *dict*. Nodes are keys, and their destinations are values (in a *list*). For a `Graph` (non-directed graph), you add the edge from source to dest and dest to source.

**Searching Graphs**

**Depth First Search** - **recursive** algorithm, but can be iterative too. Start at beginning node, and start going as deep as possible, only working back up if going down no longer possible:

```python
def DFS(graph, start, visited=[]):
  if not start in visited: visited.append(start)
  # Loop through all unvisited nodes
  for unvisited_node in (graph[start].children - visited):
    visited += DFS(graph, unvisited_node, visited)

DFS(graph, 'A')
```

DFS can be modified to include a shortest path feature:

```python
def DFS(graph, start, goal, path, shortest):
  # Path represents the path used to get to this node
  path.concat(start)
  # If the goal is reached, then pass up to parents
  if start == goal: return path
  #Loop thru children (-current_path ensures we don't loop)
  for child_node in start.children - path:
  	child_path = DFS(graph, child_node, goal, path, shortest)
    if shortest == None or len(shortest) > child_path:
      shortest = child_path
  return shortest
```

**Breadth First Search**

Unlike DFS this explores all the direct children, before going to their children. This means that once a solution has been found *it will be the shortest*, as all others are longer.

Typically coded as an **iterative** algorithm. It depends on the **queue data structure**, which is FIFO.

```python
def BFS(graph, start, goal):
  init_path = [start]
  path_queue = [init_path]		# This is what to look for next
  while len(path_queue) != 0:
    curr_path = path_queue.pop(0)
    # is this the target?
    if curr_path[-1] == goal:
      return curr_path
    # Loop thru children, avoiding circles
    for child in curr_path[-1].children - curr_path:
      path_queue.append(curr_path + [child])
   return None		   				 # Nothing was found
```

For **weighted paths**, depth first search can be modified NOT breadth first search.

