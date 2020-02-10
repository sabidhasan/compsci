## Intro

These notes are from this course: **educative.io/courses/learn-ruby-from-scratch**

- `irb` launches the Ruby console.



## Variables

Four types of **variables**:

1. Global (start with $ sign)
2. Local (start with _ or lower case letter)
3. Instance variable (start with @)
4. Class variable (start with @@)

A class variable is shared by all descendants of a class

## Numbers, Strings and Symbols
### Numbers
For **numbers**, integers always produce integers - e.g. `3 / 2 = 1`, not `1.5`.
For determining odd/even-ness, use the `.odd?` method in the Number class.
The `to_i` and `to_f` methods convert to integers/floats, respectively.
Numbers' `.even` method to see if it is even

### Strings
For **strings**, define by:
1. Single quotes
2. Double quotes (interpolation and special characters \n only work in double quoted strings)
3. Using % syntax `%(some text here)`

Concatenation is done with a `+`, or `*`, like in Python.
Other useful string methods:

- `reverse`
- `upcase`
- `length`
- `capitalize` (capitalizes the first letter)
- `.include?` method for substring
- `.start_with?` for checking if a string starts with
- `.prepend` for prepending a string with another
- `.delete` method deletes characters from string

String interpolation requires `""` and uses this syntax `"Hello, #{name}!"`

### Symbols
**Symbols** are like strings, except in code, but unlike strings, Ruby symbols are immutable: `:some_sym`
This means that their `.object_id` returns the same value.

## Arrays
An array is an object that stores other objects - order for objects is maintained.
Can define using square bracket syntax or using `%w(array items)` syntax.

**Accessing**
- Use square bracket notation
- The special methods `.first` and `.last` can get the first or last element of an array.
- Ruby has no IndexErrors, meaning that like JS, it returns `Nil` when accessing a non-existing element.

**Mathematical Operation**
- To add to an array, you can use the **shovel operator**:
```ruby
	arr << "new val"
```
- **Concatenation** is done with the `+` operator.
- Arrays support **set difference** calculation with the `-` operator
- Multiplication duplicates the array by the number multiplied
- **Set Intersection** uses the `&` operator

**Useful Methods**
- `.length` for member count
- `.sort` for alphabetical sorting
- `.include?` to see if something is in the array
- `.compact` for removing nil values
- `.index` for determing the index of a given value - returns `nil` if not found
- `.select` picks elements, and `.reject` rejects an element based on a code blocl
- `.delete` method deletes a specific element
- `.each` method iterates through each element with the given code block
- `.detect` method iterates through each element with the given code block, and finds the first truthy (like find in JS)
- `.uniq` removes duplicates


For picking a specific element, use the .select method:
```ruby
arr.select { |val| val.even? }
```

## Hashes
There are two way to create a hash:
1. Keys as whatever (strings, symbols, etc), enclosed in curly braces, separated with a hash rocket `=>`
2. Keys as words, separated by colons (*this makes all keys be symbols*)

Square bracket notation can get the key from a hash, and set a key
Looking up a value that doesn't exist will return `nil`

**Useful Methods**
- `.merge` merges two hashes
- `.fetch` gets a value from the hash, but raises a KeyError if the value is not found
- `.keys` returns an array with the keys
- `.length` determines the length of a hash
- `.has_key?` returns whether there is a key in hash
- `.invert` flips a hash's keys and values

## Classes
Almost everything is a class in Ruby. On all objects, there are certain methods defined:
- To get the class for something, use `.class` method or `.is_a?` method
- To get a llist of methods, use `.methods` method, which returns an array
- `.inspect` is equivalent to `__repr__`

Built in classes (there are others but these are the basics):
- Array
- Exception
- FalseClass and TrueClass
- File
- Float, FixNum, Integer, Numeric
- Hash
- Method
- NilClass
- Proc
- Range
- String
- Symbol
- Time

In Ruby, **sending a message** to a class refers to calling a method on it

Certain methods are **predicate methods**, meaning they end with a `?`. This indicates that they return `true` or `false`

Certain methods are **bang methods**, meaning they end with a `!`. This indicates they modify the original object

Classes are defined thus:
```ruby
  class Person
    def initialize(name)
      @name = name
    end

    def name=(new_name)
      @name = new_name
    end
  end
```

You MUST use CamelCase to define a class (Ruby throws an error)
Call the `.new` method on a class to instantiate a new member
The `initialize` method is special and runs when the class is instantiated

> Methods that exist on classes are called **class methods**, and methods that are available on instances are called **instance methods**. Instance methods are defined inside the class body as regular methods.
> **Instance variables** are defined on the instance by being prefixed with `@`

An **attribute reader** is a method that simply returns the value of an instance variable, and an **attribute writer** sets an instance variable.
When Ruby sees the assignment operator, it tries to use the attribute writer (ie. the `Person.name=` method) to assign the value.

Within an object the `self` keyword refers to the object itself. This is useful if you want to refer specifically to methods/attributes in the current object


## Methods
Define methods with:
```
	def method_name(args)
		# Do something
	end
```

In Ruby, a method always returns exactly one single thing.

Ruby methods don't need to be called - when a variable is referenced, it checks for a local variable, and if not found, it looks for a method with that name.

Within a method body, variables from the outer scope are not available


## Blocks
A block is like an anonymous method - it is a piece of code without any name. It still receives values, and returns a value.

To create a block, there are two methods

1. The `do`...`end` syntax for multiliners:

```ruby
		5.times do
			puts "hello!" 
		end
```

2. The curly brace syntax:
```ruby
	5.times { puts "hello!" }
```

If the block gets an argument, it is enclosed in pipes `|arg|`

Methods that use blocks and loop over a data structure are called **iterators**


## Conditionals and Operators
### Conditionals
Ruby supports trailing `if` for conditionals:

```ruby
	puts "some string" if number.even?
```

An if statement evaluates to whatever condition within it is true.
```ruby
	some_var = if number.even? "test" else "no test" end
```

> The only falsy values are `nil` and `false`


---
### Operators

Ruby operators support polymorphism:
- the `+` operator concatenates strings and arrays
- the `*` operator duplicates strings and arrays

The operators `&&`, `||`, and `!` take precedence over `and`, `or`, and `not`

For the `==` operator, two arrays are equal when the have the same elements in the same order
To check equality by object ID, use `.equal?`

All Ruby methods are on objects, including operators. When doing `1 + 5`,  Ruby actually calls the function: `1.+(5)`, but this is syntactic sugar.


## Require, Include, Extend (aka Modules)
Some functionality is in libraries, and must be imported before using. A **module** is like a class, except it cannot be instantiated. For example, utility functions can be in a module, and a class can import and use them directly. Modules are defined:

```ruby
	module Animals
		def mammals
			# Module's instance method
			['duck', 'dog', 'cat']
		end
		
		def self.birds
			# Module's class method
      ['falcon', 'dove', 'pigeon']
		end
	end
```

To use this functionality, you can either use `require`  (placed at the very top of the file) or `include` (placed in class definition) or `extend` (placed in class definition).

- The `require` keyword makes the module be defined `Animals` - this is similar to import in JS/Python.
- The `include` keyword is an OO-keyword that extends a class - kind of makes a parent class, and makes all methods be **instance-level methods**
- The `extend` keyword is the same as include, except it makes methods **class-level methods** (they are accessed using class, no need for calling `.new` first).

The module itself is an object too - so accessing `Animals.mammals` will not work because it is an instance method. But modules cannot be instantiated so `mammals` can only be extended or included in other classes.
However, `birds` is a class method, so `Animals.birds` will work. And because birds is a class method, it cannot be extended or included in other classes, and only accessed by `Animals.birds`.

```ruby
	# Expose module Digest.
	# Can call class methods in module by doing Digest.class_methods()
	require 'digest'
	
	class Test
		# Make instance methods from SomeModule as instance methods in this class
		include SomeModule
		# other methods
	end
```

## Private Methods
Properties on an instance are private by definition unless a getter is defined.
For methods to have the same benefit, they must be defined as private.

This is done by using the `private` keyword.
