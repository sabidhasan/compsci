## Lecture 16 - Object Oriented Programming

Computation using distributed state - state is kept in objects akin to the closures.



- Method calls as *messages* between objects

- **Classes** vs **Instances**

- Python distinguishes between **bound methods** and **functions** - methods are pre-filled in with the `self` argument
  Dot notation produces a bound method from an object (`self` parameter is pre-bound)



The **method resolution order** determines the order in which method resolution is determined for an object.

**Attributes** - parts of objects (name-value pairs)



## Lecture 17 - Inheritance

Inheritance links classes together - allow DRY code

`super()` allows calling a method in the parent class, pre-bound with `self`.

Base class attributes aren't copied into subclasses! (**MRO** is what finds those values when looking up)

**Composition** - when an object as another object as an attribute (as opposed to Inheritance). 
OOP represents **is-a** relationships, so child classes *should be* a type of their parent classes.



## Lecture 18 - Polymorphism and Abstraction

Objects should know how to represent themselves - e.g. strings represent text

- `repr` function - returns a string that `eval`s to the original object
- `str` function - human readable version of the object



A **polymorphic** function is one that applies to many forms of data, and accepts many forms of data as input. For example, `str` and `repr` are polymorphic, because they can take any type of object as their argument.

An **interface** is a shared set of properties and values, that an object can implement, and which allows the object to behave a certain way for outsiders. For example:

- Implementing `str` and `repr` allows a class to implement the string representation interface
- Implementing `__add__` allows support for `+`



**Type Dispatching** means to check the type of an object before deciding to do something, whereas **type coercion** refers to converting from one type to another.

