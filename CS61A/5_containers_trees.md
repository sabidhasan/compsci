# Lecture 11 - Containers

A **sequence** is an ordered collection of values. The sequence is a collection of behaviours implemented by several data types. All sequences have:

- Length (by calling `len`)
- Element Selection (by calling `[x]`)
- Membership check (by using the `in` operator)
- Slicing (by using `[:]` operator)

## Lists

Sequence of arbitrary length, created using the following syntaxes, and contains other values (including lists):

- list literal
- `list` constructor function
- list comprehension syntax

Lists are mutable objects, meaning they can be changed after creation. 

## Sequence Iteration

**For Statements** are used to iterate over sequences or *iterable values*, such as lists.
These statements do not create a new frame in the environment diagram (NO NEW FUNCTION CALL!).
When there are multiple values to unpack, you can apply *sequence unpacking* to assign them directly to variables.

**Ranges** represent a range of integers

Common operations for iterating over sequences are:

- `map` (apply a function to all elements of sequence)
- `filter` (remove elements from sequence if they fail a function)
- `reduce` (apply function to all elements, and return accumulated value)

## Other Data Structures

A data structure is a **closure** if it can be composed of itself. For example, lists can have nested lists, thus they are a closure. These data strcutures allow other complex structures to be used.

For environment diagrams, nested data structures use pointers.

**Strings** are an abstraction of textual data, and implemented as a sequence of characters.

**Dictionaries** are:

- associative arrays of key/value pairs
- unordered
- keys cannot be mutable types
- keys must be unique

**Linked Lists** consist of a pair containing the first element of the sequence, and the rest of the sequence as the second part of the pair, as another linked list. Iterating through linked lists can be done recursively or iteratively, as well as implementing a `length` and `append` method.



#  Lecture 12 - Trees

**Trees** are a data structure for representing heirarchical relationships.

They have a **root** (or root node) and **branches** (which are also trees). A tree with no branches is called a **leaf** - the end of the tree. A tree contained within a tree is called a **subtree**. A **parent node** is one that has branches, while a child node has parents.

The Fibonacci sequence can be interpreted as a tree.

Can represent each level as an array, where element 0 is the label for a node, and the elements 1...n are the nodes (which are trees themselves).

Generally, tree traversal functions are **recursive**, and processing a leaf is the base case (as you cannot traverse anymore).