# Week 1

## Lecture 1

Computer science studies these things:

- What problems can be solved by a computer
- How to solve those problems
- What are effective solutions

Areas of study include:

- Artificial Intelligence
  - Decision Making, Robotics, Natural Language Processing
- Systems (like OS)
- Graphics
- Security
- Networking
- Theory
- Scientific Computing
- Programming languages

The common enemy of computational problems is **complexity**, which is countered by using **abstraction**.

**Statements** - describes an action to be **executed** by the computer, and produce some change. For example, fetching data from a URL, or assigning an *expression* to a variable.

**Expression** - describes a computation and <mark>evaluates to a value</mark> (e.g. compare with mathematical expressions). In contrast with statements that are executed,  expressions are evaluated. Any computation can be done using a call expression, including those that have operators in Python:

```python
from operator import add
add(1, 2)			# returns 3; same as 1 + 2
```

**Call Expressions** are expressions that apply a function (aka **operators**) to some expression (called **operands**), and **evaluate** to a value. Nested call expressions are evaluated by recursively performing the operation on the nested operands to get values, and then  working upwards until the entire expression is calculated. This process is described by an **expression tree**. Each node represents an expression paired with its value.

![image-20190902115353069](/Users/abidhasan/Google Drive/Programming/compsci/CS61A/assets/image-20190902115353069.png)



**Programming Languages** have three mechanisms for composing ideas:

1. **Expressions** and **Statements** as building blocks (described above)
2. **Compound Elements** - elements built by combining simpler elements (a namespace system to bind names compound elements)
3. **Means of abstraction** to manipulate the built compound elements (aka using the *assignment operator*)

**Pure vs Impure Functions** - pure functions are *idempotent* (meaning they produce the same value each time they're called with the same input), and have no side effects. The benefit are:

- Easier to compose into call expressions
- Easier to test
- Essential to writing *concurrent programs*

