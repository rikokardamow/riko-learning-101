## Code Comment ##
# This is a comment ~ way to explain your thinking process!
# These lines of code will not change any values
# Anything following the first # is not run as code

""""This is a special string"""

#Code Conventions
#style familiar to your writing style

#Use Four Spaces for indentation.

if True:
    x = 5 # Four indentions

#use Lowercase with Underscores for Variable and Function Names.
#Variables and function names should be in lowercase, with word separated by underscores as necessary to improve readability.

my_variable = 1
def my_function():
    pass

#camel cases uses for mainly Class

class MyNewClass():
    pass

x = 1
x = x + 1 # Increment X

import os
import sys

# from third_party import local_module #This is not exist, just for sample code

#Correct
age = 4 + 18

#Incorrect
age=4+18


def square(number):
    """"Return the square of the number"""
    return number * number

square(5)

#Objects,types and Variables
#int(integer, a whole number with no decimal place)
#float / String / bool(True/False) / NoneType

num_1 = 10
num_2 = 2
num_3 = 6

num_1 + num_2

num_1 - num_3

num_2 * num_2

num_1 / num_3

num_3 ** num_2

num_1 += 2
num_1

num_1-=2
num_1

num_3 *=5
num_3

num_4 = num_1 + num_2 + num_3
num_4

num_3 != num_4

num_3 > num_2

simple_string_1 = "in example"
simple_string_1 = simple_string_1 + " we re working"
simple_string_1

num_3 -=5
num_3

num_3 > num_1

num_3 ** num_1 == num_2

simple_string_1 *=3
simple_string_1

# Data Structures (colletions)

# str( string: immutable, indexed by integers; items are stored in the order they were added. You cannot change the values within immutable thing.
# list (list; mutable; indexed by integers; items are stored in the order they were added.
list_1 = [3, 5, 6, 3, 'dog', 'cat', False]

#tuple( tiple;immutable; indexed by integers; items are stored in the order they were added)
tuple_1 = (3, 5, 6, 'dog', ' cat', False)

#dict (dictionary; mutable; key-value pairs are indexed by immutable keys; as of Python 3.7, items are stored in teh order they were added)
dict_1 = {'name': 'Jane', 'age': 23, 'fav_foods': ['pizza', 'fruit', 'fish']}
dict_2 = {'name': 'Javier', 'age': 45, 'fav_foods': ['chicken', 'veg', 'candy']}


list_1
set_1
dict_1
dict_2

#Accessing Data in collections
#strings, lists and tuples are indexed by integers and starting from 0 for the first item
    #these sequence types also support accessing a range of items, known as slicing
    #use negative indexing to start at the back of the sequence
#dict are indexed by their keys

list_1[3:5]

list_1[-2:]
tuple_1[-0:]

dict_1["fav_foods"]
dict_2['age']

#Built-in functions and callables
# A function is a Python object that you can "call" to perform an action or compute and return another object.
# You call a function by placing parenthesis to the right of the function name. Some functions allow you to pass arguments inside the parentheses (separating multiple arguments with a comma). Internal to the function, these arguments are treated like variables.
    # type(obj) to determine the type of an object
    # isinstance(val, obj) to determine if val is an obj
    # len(container) to determine how many items are in a container
    # callable(obj) to determine if an object is callable
    # sorted(container) to return a new list from a container, with the items sort
    # sum(container) to cumpute thye sum of a container of numbers
    # min(container) to determine the smallest item in a container
    # max(container) to determine the largest item in a container
    # abs(container) to determine the absolute value of a number
    # repr(obj) to return a string respresentation of an object

type("1.1")

isinstance("1.1", float)

len([1, 2, 3])

len(simple_string_1)
len(dict_1)

sorted([10, 99 ,2.3, 1111, 123123123, 235235])
sorted("jason")

sum([10,1232131, 123777, 0.5555])

# Object attributes (methods and properties)
# Different types of objects in Python have different attributes that can be referred tyo by name (similar to variable). To access an attribute of an object, use a dot (.) after the object, then specify the attribute(i.e. obj.attribute)
# When an attribute of an object is callable, that attribute is a called a method. It is the same as function, only this fuction is bound to particular object.
# When an attribute of an object is not callable, that attribute is called a property. It is just, that is itself another object.
# The built-in dir() function can be used to return a list of an object's attributes.

# Methods on strings

# .capitalize() to return a capitalized version of the string(only first character uppercase)
# .upper() to return an uppercase version of the string (all chars uppercase)
# .lower() to return an lowercase version of the string (all chars lowercase)
# .count(substring) to return the number of occurences of the substring in the string
# .replace(old, new) to return a copy of string with occurences of the old replaced by new

a_string = "tHis is a sTrInG"
a_string.capitalize()

a_string.lower()
a_string.upper()
a_string.count("t", 3)
a_string.count('is')
a_string.endswith('Ng')

a_string.replace('is', 'XYX')

a_string.replace('i' , '!', 2)

a_string.endswith('nG')

# Methods on lists
#  .append(item) -> to add a single item to the list
#  .extend([item1, item2, item3, ....]) -> to add multiple items to the list
#  .remove(item) -> to remove a single item from the list
#  .pop() -> to remove and return the item at the end of the list
#  .pop(index) -> to remove and return an item at an index

list_1

list_1.append("basketball")
list_1

list_1.extend(["baseball", 1]) # equivalent. list + list
list_1

list_1.remove("cat")
list_1

list_1.pop()
list_1

list_1.pop(0)
list_1


# Methods on sets
# .add(item)
# .update([item1, item2, ....])
# .update(set1, set2, set3, ....)
# .remove(item)
# .difference(set2)
# .intersection(item)
# .union(set2)
# .symmetric_difference(set2)
# .issuperset(set2)
# .issubset(set2)

set(['Jason', 'jason', 'jason'])

set_1.add("fuzz")
set_1

set_1.union()



dict_1

dict_1.pop('age', 50)
dict_1