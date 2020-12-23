## Lecture 26 - Exceptions

Python **raises an exception** when error occurs, and handled by program. Unhandled exceptions halt execution and print **stack trace**. Python exceptions have *non-local* continuations of control - meaning if `f` calls `g` which calls `h` which raises an exception, then the error can throw control back to `f` bypassing `g`.

How to raise exceptions:

- **Assert statement** raises an `AssertionError`. Running code with `-o` will run without assertions (for optimization purposes)
- **Raise statement** can be used to raise a class that is a subclass of `BaseException`

A custom exception can be made that stores instance variables:

```python
class IterImproveError(Exception):
        def __init__(self, last_guess):
            self.last_guess = last_guess
```



