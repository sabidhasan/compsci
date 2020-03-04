## Lecture 13 - Mutable Values

**Objects** group behavior and data together and have **attributes** and **methods**. They abstract things, properties and proesses to give their behavior.

A type of an obect is called a `class`.

An object is mutable by definition - it can change its value over time. All names that refer to the same object are affected by a mutation.

Mutations can happen in a function call - a function can access something in the global scope, and they are passed mutable values by reference, so changes happen outside the function

**Tuples** are immutable sequences.

An immutable sequence is protected from changing, but:

- a mutable value that it contains can change (e.g. a list within a tuple)
- the name that binds to a immutable value can be rebound to something else



The **nonlocal** unary keyword states that the variable affected will occur in a frame that is not the local or global frame, and tells the interpreter to start looking in the parent frame. This is required when a HOF needs to *change* the binding for a shadowed variable. Reading a variable follows LEGB rules, and will go to the parent frame as normal.



**Referential Transparency** refers to the idea that an expression is the sum of its subexpressions' values. When impure functions (e.g. with the `nonlocal` keyword) are used, they will remove referential transparency because the environment is changed.



**Iterators** are a way to process sequential values. Python implements this with the `iter` function, `next ` function, and  `StopIteration` exception. An **iterable** value is one that can produce an iterator. A **generator** is an iterator that is reeturned by a **generator function**. This is created with the `yield` keyword.

## Lecture 14 - Mutable Functions

**Mutable Functions** have data associated with them that changes. For example, a HOF with closure variable, will be a mutable function.

The local state of these functions is stored in their parent's scope.

There are two ways to update local state:

- Use `nonlocal` keyword (otherwise, it attempts to assign the variable in the current function's frame). The name listed in `nonlocal` have to be defined in an enclosing scope.
- Use a mutable value like a list (this doesn't need `nonlocal` because the list is mutable)

Here is what the **assignment statement** does:

1. If no `nonlocal` and variable doesn't exist, it creates new variable in current frame
2. If no `nonlocal` and variable exists, it rebinds variable in current frame
3. If `nonlocal` and variable in enclosing frame, it rebinds variable in enclosing frame
4. If `nonlocal` and variable doesn't exist in enclosing frame, it raises SyntaxError
5. If `nonlocal` and variable exists in enclosing frame and current frame, it raises SyntaxError





## Lecture 15 - Iterators & Generators

Sequential data can be represented using iterators, which allow accessing data in order one at a time.

`iter` produces an iterator for an iterable value
`next` gives the next value from an iterator

For statements iterate over an *iterator* (`iter`) or over an iterable (like a `list` or `range`).
When iterating over an iterable, the for loop creates an iterator and iterates over it. For an iterator, it will just iterate. The consequence being that once the iterator is extinguished, it cannot iterate any longer.



A **generator** is a special iterator that comes from a function (other special iterators are maps, filters, zips, etc.). A generator function demarcated by `yield` keyword.
Function execution is paused when the `yield` keyword is encountered.

A `yield from <iterable>` syntax allows yielding from an iterable one by one in turn

