# Lecture 3 - Control

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

# Lecture 4 - Higher Order Functions

**Fibonacci Sequence**:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...

Can be computed iteratively:

```python
def fib(n):
  pred, curr = 0, 1
  k = 0			# what fib number we are on for `curr`
  while k < n:
    pred, curr = curr, pred + curr
    k += 1
  return curr
```

Functions are the best way for organizing programs. Some definitions:

- A function's **domain** is all arguments it may take
- A function's **range** is all possible output values
- A **pure function**'s behavior is the relationship between input and output
- **Function composition** - combining functions to produce more complex programs

Follow the **DRY principle** to prevent unnecessary repetition.



**Higher Order Functions**

These are a way to *generalize functions*, and share implementation, thereby removing repetition. In Python, functions are **first class**. A higher order function is:

> A function that takes another function as an argument, or returns a function as a return value.

The common structure among a function may be a **computational process**, or a **constant**. Writing HOFs means the generalized function is more extensible.

Higher order functions also have the possibility to be **closures**. In Python, local functions have access to the name bindings in the scope in which they are defined - their **parent**! This is called **lexical scoping**. Variables from the frame where a function was CREATED are available when a function is run.

When a function is executed, they have their parents, grandparents, etc. until the global scope is reached.

Decorators is syntactic sugar for Python HOFs:

```python
@dec		# test is rebound to the function that dec returns
def test():
  return None
```



**Currying**

Currying converts a function that takes multiple arguments into a chain of functions that each take a one argument.



**Lambda Expressions**

These are a way to bind a function to a name using the assignment syntax. The major difference from regular functions is that $\lambda$ functions do not have an intrinsic name.

```python
func = lambda x: x * x
```

This makes func into an operand, that can be called using a **call expression**.

- Both `def` and `lambda` create the same function (if body is the same)
- Both have the same scope
- Both bound to the same name
- However, $\lambda$ function has no **intrinsic name** (this is what is shown when typing the name of the function in the REPL). 
- However, $ \lambda $ functions cannot contain statements

Something has **First Class Status** in a language if:

1. Can be assigned to a variable
2. Passed into a function'
3. Returned from a function
4. Included in more complex data structures



# Lecture 5 - Environments

When defining a function:

- Bind name to the function body in the current frame
- Make Parent of that function be the current frame (this is how closures work)

When running a user defined function, this happens:

- A new frame is created (remember who the parent is - it is where the function was defined - this doesn't change by calling a function!)
- Bind formal parameters to local fram
- Execute the body of the function as normal, looking through parent chain for variables

For resolving names, first search the local frame, then the parent frame, then the global frame. What is a **parent frame**:

>  The **parent** of a function is the frame in which it is defined.



**Function Composition**

**Function composition** refers to making a higher order function that takes two functions, and calls them successively on one input.

