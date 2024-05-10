# 0x04-python-more_data_structures    

In this project I have learned and solved tasks about:    
- sets    
- dictionaries    
- lambda functions    
- map functions    
- filter functions    
- reduce functions    

There are some QAs that I've answered about these topics    

## What are sets and how to use them?    

Sets are unordered collections with no duplicates, and their basic uses include:     
- membership testing    
- eliminating duplicate series    

Python sets support mathematical operations like Union, Intersection, Difference, and Symmetric Difference.    
Sets have methods like any sequential python datatype.    

### How to make sets?    

Use `{}` or `set()` function to create sets, however, if you want to init an empty set you should use the function only, becaues the empty curly brackets are used to init empty dicts.   
	**i.e.** `basket = {'apple', 'orange', 'apple', 'pear', 'oragne'}`    
	This will output -> `{'apple', 'orange', 'pear'}`     

### Sets Operations    

- `a - b` -> gives what in a but not in b   
- `a | b` -> gives what is in a or b or both    
- `a & b` -> gives what is common between a and b only    
- `a ^ b` -> gives what is in a or b but not both    

## When to use Sets V.S. Lists?    

The primary difference between list and set is that a list allows duplicate elements and maintains their order, while a set ensures element uniqueness without any guaranteed order.    
So, if you're wondering which to use, it depends on the use case. 
If you don’t want the values in the data to change, you can use a set. 
But if you want the items to change, you can use a list. 
You can also take into account whether the order of the items matters to you or not.    

## What are dictionaries and how to use them?    

Dictionaries are similar to arrays some how, but you can access their elements using keys (not index). 
Dicts are set of `key : value` pairs, and keys must have unique values. 
You can store a value with some key and extract it again using its given key. 
To construct a dict you can use the `dict()` function or just put `{}`.    

