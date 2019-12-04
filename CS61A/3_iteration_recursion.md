# Lecture 6 - Iteration

A `return` statement comlpetes the evaluation of a call expression, and provides its value back in the original environment.

Only one return statement is executed in a function body.



**Self Reference**

A function can refer to its own name in its body, thus making a higher order function self referential.



**Currying**

Transform multiple-argument functions into a chain of single-argument, higher order functions. Useful when dealing with functions that take only single-argument functions.



# Lecture 7 - Recursive Functions

**Definition**: A function that calls itself, either directly or indirectly. When recursive functions are defined, they are not executed.

Recursive functions need:

- a **base case**, to prevent infinite looping, and which have no recursiveness
- some **recursive cases**.

Different frames keep track of the arguments in each call in the **call stack**.

**Iteration vs Recursion** - <u>Iteration is a special case of recursion</u>. In the case of factorial function, the problem can be solved in either way. Iteration is easier to follow, but recursion usually has fewer variables.

It can be tricky to convert from recursive to iterative, sometimes.
Converting from iterative to recursive is trivial.

**Mutual Recursion** - occurs when two recursive functions call each other. These functions can also be written as one recursive function, with the other's logic incorporated into the main function. For example:

- A number *n* is odd if *n* - 1 is even
- A number  *n* is even if *n* - 1 is odd
- 0 is even

An implementation of the *Luhn Sum* for credit card checksum uses this phenomenon.

**Tree Recursion** refers to a function that recurses has more than one recursive call in its return statement. The Fibonacci computation, for example.

## Closures

A **closure** is created when a function is returned from a function. These functions can be called at a later time. This is a **Higher Order Function**.

**Lambdas** are expressions that evaluate to a function value. They have a single expression in their body.
Lambdas have no intrinsic frame, and their parent in the environment diagram is whoever called it.



The **PARENT** of any function is the frame in which it is defined.



# Lecture 8 - Functional Abstractions

**Functional abstraction** means giving name to a process, and not worrying about its implementation details. Here is what is required for a caller:

- Need to know **function signature**
- What the function *does*

Other things like implementation, or even intrinsic names are not required.

Naming guidelines for functions:

1. Names should convey **meaning**
2. Parameters should be described in **docstring**, not the name
3. Convey effect, behavior or value returned in the name

Naming guidelines for values within function body:

1. Repeated compound expressions should be assigned to an intermediate name
2. Complex expressions should be named for legibility for the reader
3. Avoid cryptic names

**Single Letter Naming Conventions**

- n, k, i				integers
- x, y, z				real numbers
- f, g, h				functions



**Testing**

**Test driven development** involves writing test before writing function body.



**Currying**

Function currying is a way of manipulating functions:

> Transform a multi-argument function into single-argument, higher order function.

A currying two argument function:

```python
def curry2(func):
  def g(x):
    def h(y):
      return func(x, y)
    return h
  return g
```



**Decorators**

Use higher order functions for syntactic sugar on creating HOFs.