# Lecture 3

Multiple *environments* can exist in the same environment diagram. This occurs when there is a nested function. Each environment will inherit variables from its parent frame (ultimetely the **Global** frame).

Names have no meaning without an environment defined. A name evaluates to the value bound to that name in the earliest frame of the current environment in which it is found.



**Statements**

Unlike expressions that are <u>evaluated</u> to a value, a statement is <u>executed</u> by the interpreter to perform an action. **Statements govern the relationship among different expressions in a program**. These are examples of statements:

- Assignment statement like `x = <val>`
- Function definition statement like `def`
- Return statement from a function
- Control (or **Conditional**) statements like `if`

**Compound statements** have multiple lines (e.g. function definition, if statements). Compound statements may have multiple **clauses**, consisting of headers and suites. A **header** (which are like `if x == 4:`), contains a **suite** (which is what should be done in that header).

False values in Python (everything else is `True`):

- `False`
- `0`
- `""`
- `None`



