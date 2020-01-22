# Lecture 9 - Tree Recursion

Order of recursive calls is important to understand behavior of recursive functions.

> A function that calls another function **must wait** for that function to finish before continuing

If two implementations of a function are equally clear, the **shorter is better**.
For recursive functions, it is often better to define the base case explicitly.



**Tree Recursion**

Tree recursion is when the body of a recursive function calls itself more than once.
The computation process evolve into a **tree structure**.

Classic case - **Fibonacci**.

```python
def fib(n):
  if n <= 1:
    return n
  else:
    return fib(n-2) + fib(n-1)
```

Without saving results, the same computation is being executed numerous times, so this implementation is actually less performant than a non-recursive implementation.



**Counting Partitions**

This is a difficult problem to solve without tree recursion. What are the combinations of numbers less or equal to `max_partition` that add up to `number` in increasing order.

```python
def count_partition(number, max_partition)
```

For example, `count_partition(6, 4)` produces:

```
2 + 4 = 6
1 + 1 + 4 = 6
3 + 3 = 6
1 + 2 + 3 = 6
...
```

Break problem into two:

- Use at least one `max_partition`
- Don't use `max_partition` (instead use `max_partition - 1`)

```python
def count_partition(num, max_part):
  if num == 0:
    return 1
  elif num < 0:
    return 0
  elif max_part == 0:
    return 0
  else:
    with_m = count_partition(num - max_part, max_part)
    without_m = count_partition(num, max_part - 1)
    return with_m + without_m
```



# Lecture 10 - Data Abstraction

**Native Data Types** - every value in Python has a class that determines what type of value it is. Native data types share two properties:

- Can be expressed using **literals** 
- There are **built in functions** or operators to manipulate them

For example, for numbers, there are three types: `int`, `float`, and `complex`. (BTW Need to beware of floating point approximation errors).

However, most real values are compound values (date, geographic location, rational numbers, etc) need more complex data structures to represent them.

**Data Abstraction** is a methodology by which a barrier is enforced between *data representation* and *data use*. This allows programs to become more modular. There are functions for:

- constructors (make a complex data type from simpler/primitives)
- selectors (getters for data from the abstraction)

Programs must be structured so that they operate on abstract data. For this, we must have constructor functions.

Abstraction works **in levels**, and between the levels exist **abstraction barriers**. These separations are important because abstracted functionality can be modified without breaking the rest of the program.

A higher level of abstraction shouldn't cross a lower level (meaning if internally something is expressed as a tuple, there is no need to poke into the tuple if you can accomplish the task with a getter function).

>  You can recognize an abstract data representation by its behavior, rather than its constructor or selectors. 

