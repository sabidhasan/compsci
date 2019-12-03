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

**Mutual Recursion** - occurs when two recursive functions call each other. An implementation of the *Luhn Sum* for credit card checksum uses this phenomenon.



## Closures

A **closure** is created when a function is returned from a function. These functions can be called at a later time. This is a **Higher Order Function**.

**Lambdas** are expressions that evaluate to a function value. They have a single expression in their body.
Lambdas have no intrinsic frame, and their parent in the environment diagram is whoever called it.



The **PARENT** of any function is the frame in which it is defined.