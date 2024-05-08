# 0x03-python-data_structures    

In this project I learned how to use python lists and tuples. The following sections are some questions I've answered myself to test if I've fully understand.    

## What are lists and how to use them?    

Lists are sequential datatypes that can be used to store a variable number of elements. A list is heterogeneous datatype, due to its ability to store multiple elements with multiple datatypes.    
To make a list you must enclose your elemets with square brackets and separate them by commas.    
- `square = [0, 1, 4, 9, 16, 25]`    

You can access list elements by using the slicing or indexing features.    
- `square[0] -> 0`    
- `square[2:-1] -> [4, 9, 16]` (slicing returns a shallow copy of the original list BTW)    

Lists support concatenation where you can add lists to each other ending up with a longer list.    
- `squares + [99, 44, 55]`    

## What are the differences and similarities between strings and lists?    

List and Strings are actually the same, but not totally the same. Yes, there are similarities, but there are some differences like:    
1. Lists are mutable, while strings are not.    
2. Lists support variable datatypes in the same exact list.    
3. Operations are different.    
4. Both support slicing but:    
	- Strings support indexing and slicing based on characters.    
	- Lists support indexing and slicing based on elements.    

## What are the most common methods of lists and how to use them?   

- `list.append(x)`: add item `x` to the end of the list    
- `list.extend(iterable)`: extend the list by appending all elements in `iterable`    
- `list.insert(i, x)`: insert element `x` at index `i`    
- `list.remove(x)`: removes the first element that is equal to `x`, if no match a `ValueError` is raised    
- `list.pop([i])`: removes and return the last element of the list if index `i` is not specified    
- `list.clear()`: removes all elements in a list    
- `list.index(x[, start[, end]])`: get the index of `x` and you may give a `start` and `end` indices, but the returned index is relative to the original list    
- `list.count(x)`: count how many times did `x` appear in a list    
- `list.sort(*, key=None, reverse=False)`: sort list with specified key    
- `list.reverse()`: reverse the list    
- `list.copy()`: return a shallow copy of list    

## How to use lists as stacks and queues?    

### Stacks   

Lists methods made it easy to follow the stack way (i.e. LIFO). You only need to call `list.pop()` to remove and `list.append(x)` to add elements to the end of the list. However, you can implement whatever function you want to aid you with you stack implementation.    

### Queues    

Python provides us with a sub-module called `dequeue` in a package called `collections` that gives the ability to follow the queue way (i.e. FIFO).    

## What are list comprehensions and how to use them?    

List comprehensions are a concise way to create lists using a single line of code. They provide a more readable and efficient way to create lists from existing iterables such as lists, ranges, strings, or any other sequence data type.    
The basic syntax of a list comprehension is as follows:    
`[expression for item in iterable if condition]`    
- `expression`: An expression that produces the element for the list.     
- `item`: The variable that represents each element in the `iterable`.    
- `iterable`: An iterable object (e.g., a list, range, string) to loop over.     
- `condition` (optional): A boolean expression to filter the elements. If provided, only elements for which the condition is `True` are included in the list.     

## What are tuples and how to use them?

Sequential datatypes that are like lists where we can do the following:    
1. assign multiple values with differenet types    
2. index it    
3. nest it    
i.e. `t = (1, 2, 3, 4)`    

## When to use tuples versus lists?    

Choose tuples when you want an immutable, fixed-size collection of items or need to ensure data integrity. 
Choose lists when you need a mutable, dynamic collection that can be modified as needed throughout the program.    

## What is a Sequence?    

A sequence is a data structure that represents an ordered collection of elements. 
Sequences can store a variety of data types (such as integers, strings, or other objects), and the elements can be accessed using indexing and slicing. 
Sequences are a fundamental concept in Python and provide many features that make working with collections of data efficient and convenient.    

## What is tuple packing?    

When you assign multiple values to a single variable, separated by commas.    
`t = 'a', 'ab', 'abc', 'abcd'`    

## What is tuple unpacking?    

When the values from a tuple are assigned to multiple variables.    
`a, b, c, d = t`     
