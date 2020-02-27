## Lecture 13

**Objects** group behavior and data together and have **attributes** and **methods**. They abstract things, properties and proesses to give their behavior.

A type of an obect is called a `class`.

An object is mutable by definition - it can change its value over time. All names that refer to the same object are affected by a mutation.

Mutations can happen in a function call - a function can access something in the global scope, and they are passed mutable values by reference, so changes happen outside the function

**Tuples** are immutable sequences.

An immutable sequence is protected from changing, but:

- a mutable value that it contains can change (e.g. a list within a tuple)
- the name that binds to a immutable value can be rebound to something else



The **nonlocal** unary keyword states that the variable affected will occur in a frame that is not the local or global frame, and tells the interpreter to start looking in the parent frame. This is required when a HOF needs to *change* the binding for a shadowed variable. Reading a variable follows LEGB rules, and will go to the parent frame as normal.



**Referential Transparency** refers to the idea that a subexpression can be substituted with its value, and will behave the same. When impure functions (e.g. with the nonlocal keyword) are used, they will remove referential transparency.



**Iterators** are a way to process sequential values. Python implements this with the `iter` function, `next ` function, and  `StopIteration` exception. An **iterable** value is one that can produce an iterator. A **generator** is an iterator that is reeturned by a **generator function**. This is created with the `yield` keyword.



