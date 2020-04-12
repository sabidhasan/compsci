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



## Lecture 22 - Special Trees

**Binary trees** (BTree) are trees with two branches. To enforce the constraint of two branches, the BTree uses an Empty node. For something to be a leaf, it means it has two empty nodes as children.

A binary tree is used for **Binary Searching** - finding a value in a sorted sequence. A binary search tree has node who:

- have right branches with all values less than the parent node
- have left branches with all values less than the parent node

Searching is an $O(log\ n)$ process - half the work is being discarded at each step. *There are multiple valid binary search trees for any list*.

The best binary search tree is **balanced** - the left and right branch have ~ same number of nodes. This maximizes the `O(log n)` search speed.

To test for membership:

- If root matches search, return True
- If root is empty, return False
- If root < elem, recursively call search on left child
- If root > elem, recursively call search on right child



Adjoining to a BST (this is a set represented as a BST):

```python
def adjoin(bst, val):
  if bst is BTree.empty:
    return BTree(val)
  elif bst.label == val:
    return bst	# Value already exists, so just return original tree
  elif bst.label < val:
    return BTree(bst.label, bst.left, adjoin(bst.right, val)) 
  elif bst.label > val:
    return BTree(bst.label, adjoin(bst.left, val), bst.right)
```

