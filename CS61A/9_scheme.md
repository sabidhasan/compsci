## Lecture 24 - Scheme

The most fundamental concept of programming is that of an interpreter - a program, which is just text, is only given meaning via another program, which is the interpreter. This idea is built up using **Scheme**, which is a dialect of **Lisp** (one of the oldest programming languages).

Scheme programs consist of primitives and combinations:

- **Primitives**: 2, 3.3, true, +, ...
- **Combinations**: `(quotient 10 2)` or `(not true)`

Call expressions include an operator and operands in parentheses. Functions in schema are called **procedures**. Spacing is entirely optional in Scheme/Lisp.

Some common built in functions:

- `+`, `-`, `*`, `/`
- `number?` to tell if something is numeric
- `zero?` to tell if something is zero
- `integer?`

**Special Forms** are any combination that is not a call expression. Examples:

- `(if <predicate> <consquent> <alternative>)`
- `(and <e1> <e2> ...)`
- `(or <e1> <e2>)`
- Defining variables: `(define <symbol> <expression>)` for example `(define pi 3.14)`
- Defining functions: `(define (<symbol> <parameters>) <body>)`

Note that Scheme does lazy evaluation. Example of a function in Scheme

```scheme
(define (abs x)
  (if (< x 0) (- x) x)
)
```



Scheme also heavily uses **Lambda expressions**. The following two are equivalent:

```scheme
(define (square x) (* x x))
(define square (lambda (x) (* x x)))
```



A **list or array** can be expressed in Scheme using a built in type called a **pair**. There are three concepts related to pairs:

- `cons` is a procedure that creates a pair: `(cons 1 2)`
- `car` is a procedure that returns the first element of a pair
- `cdr` is a procedure that returns the second element of a pair
- `nil` is an empty list

A **dotted list** is a broken list, and it is one that doesn't have follow the linked list recursive definition (i.e. the second item in the pair is **not** `nil` or another pair).

Scheme interpreter displays the lists in the following fashion:

- For a dotted list which is a non-linked-list, e.g. `(cons 1 10)`, it displays `(1 . 10)`
- For a linked list/array (e.g. `(cons 1 (cons 10 nil))`), it displays `(1 10)`

Helpful methods related to lists:

- `pair?` determines if something is a pair
- `null?` determines if something is `nil`
- `list` which makes a list from parameters: `(list 1 2 3 4 5)`



**Symbolic Programming**

The **single quotation mark** allows directly parsing output, similar to `eval` in Python. Quotation allows symbols to be values. Some examples for where this can be used:

1. Symbols typically stand for values but quotation allows constructing lists out of symbols
2. List output can be evaluated in to the underlying lists

```scheme
> (list 'a 'b)
(a b)

> (car '(a b c))
a

> '(1 2 . 3)
(1 2 . 3)

> '(1 2 . (3 4))
(1 2 3 4) 	; this makes sense - a dot with a pair is actually not malformed
```

You can refer even to symbols that have not been defined yet!

