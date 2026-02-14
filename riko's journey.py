# ============================================================================
# MY PYTHON LEARNING JOURNEY
# ============================================================================
# This document tracks my progress learning Python fundamentals
# Each section builds on the previous one
# ============================================================================

# ============================================================================
# SECTION 1: COMMENTS AND DOCUMENTATION
# ============================================================================

# Single-line comments start with #
# They explain what the code does without affecting how it runs

"""
Multi-line strings (docstrings) are created with triple quotes.
They're often used to document functions and classes.
"""

# ============================================================================
# SECTION 2: PYTHON CODING CONVENTIONS (PEP 8)
# ============================================================================
# Following these standards makes code readable and professional

# Use 4 spaces for indentation (not tabs)
if True:
    x = 5  # This is properly indented

# Variable and function names: lowercase_with_underscores
my_variable = 1

def my_function():
    """Functions should have docstrings explaining what they do"""
    pass

# Class names: CamelCase
class MyNewClass():
    """Classes represent blueprints for objects"""
    pass

# Spacing around operators improves readability
age = 4 + 18  # Good: spaces around +
# age=4+18    # Bad: no spaces (harder to read)

# ============================================================================
# SECTION 3: BASIC DATA TYPES
# ============================================================================

# Python has several built-in data types:
# - int: whole numbers (10, -5, 0)
# - float: decimal numbers (3.14, -0.5)
# - str: text ("hello")
# - bool: True or False
# - NoneType: represents "no value" (None)

# ============================================================================
# SECTION 4: BASIC MATH OPERATIONS
# ============================================================================

num_1 = 10
num_2 = 2
num_3 = 6

# Basic arithmetic
num_1 + num_2  # Addition: 12
num_1 - num_3  # Subtraction: 4
num_2 * num_2  # Multiplication: 4
num_1 / num_3  # Division: 1.666...
num_3 ** num_2  # Exponentiation (power): 36

# Compound assignment operators (shorthand)
num_1 += 2  # Same as: num_1 = num_1 + 2
num_1 -= 2  # Same as: num_1 = num_1 - 2
num_3 *= 5  # Same as: num_3 = num_3 * 5

# Comparison operators return True or False
num_3 != num_4  # Not equal to
num_3 > num_2   # Greater than
num_3 == num_1  # Equal to (note: double ==, not single =)

# ============================================================================
# SECTION 5: WORKING WITH STRINGS
# ============================================================================

simple_string_1 = "in example"
simple_string_1 = simple_string_1 + " we're working"  # Concatenation
# Result: "in example we're working"

simple_string_1 *= 3  # String repetition
# Result: "in example we're workingin example we're workingin example we're working"

# ============================================================================
# SECTION 6: DATA STRUCTURES (COLLECTIONS)
# ============================================================================

# Lists: Ordered, mutable (can be changed), indexed by integers
list_1 = [3, 5, 6, 3, 'dog', 'cat', False]
# Can hold different data types, allows duplicates

# Tuples: Ordered, immutable (cannot be changed), indexed by integers
tuple_1 = (3, 5, 6, 'dog', 'cat', False)
# Use when you want data that shouldn't change

# Dictionaries: Key-value pairs, mutable, indexed by keys
dict_1 = {
    'name': 'Jane',
    'age': 23,
    'fav_foods': ['pizza', 'fruit', 'fish']
}

dict_2 = {
    'name': 'Javier',
    'age': 45,
    'fav_foods': ['chicken', 'veg', 'candy']
}

# Sets: Unordered, mutable, no duplicates allowed
set_1 = {'Jason', 'chicken'}  # Duplicates automatically removed

# ============================================================================
# SECTION 7: ACCESSING DATA IN COLLECTIONS
# ============================================================================

# Lists, tuples, and strings use index numbers (starting at 0)
list_1[0]      # First item: 3
list_1[3]      # Fourth item: 3
list_1[-1]     # Last item: False
list_1[-2]     # Second-to-last item: 'cat'

# Slicing: getting a range of items [start:end]
# Note: end index is NOT included
list_1[3:5]    # Items at index 3 and 4: [3, 'dog']
list_1[-2:]    # Last two items: ['cat', False]
tuple_1[0:]    # All items from start: (3, 5, 6, 'dog', 'cat', False)

# Dictionaries use keys to access values
dict_1["fav_foods"]  # Returns: ['pizza', 'fruit', 'fish']
dict_2['age']        # Returns: 45

# ============================================================================
# SECTION 8: BUILT-IN FUNCTIONS
# ============================================================================
# Functions you can call to perform common tasks

type("1.1")                    # Returns: <class 'str'> (it's a string, not float)
isinstance("1.1", float)       # Returns: False (checking if it's a float)
len([1, 2, 3])                 # Returns: 3 (number of items)
len(simple_string_1)           # Returns: length of string
len(dict_1)                    # Returns: 3 (number of key-value pairs)

sorted([10, 99, 2.3, 1111, 123123123, 235235])  # Returns sorted list
sorted("jason")                # Returns: ['a', 'j', 'n', 'o', 's']

sum([10, 1232131, 123777, 0.5555])  # Returns sum of all numbers
min([10, 2, 100])              # Returns: 2 (smallest)
max([10, 2, 100])              # Returns: 100 (largest)
abs(-5)                        # Returns: 5 (absolute value)

# ============================================================================
# SECTION 9: STRING METHODS
# ============================================================================
# Methods are functions that belong to a specific object type

a_string = "tHis is a sTrInG"

a_string.capitalize()          # "This is a string" (only first letter caps)
a_string.upper()               # "THIS IS A STRING" (all uppercase)
a_string.lower()               # "this is a string" (all lowercase)
a_string.count('is')           # 2 (counts occurrences of 'is')
a_string.endswith('nG')        # True (checks if string ends with 'nG')
a_string.replace('is', 'XYZ')  # "tHXYZ XYZ a sTrInG" (replaces all 'is')
a_string.replace('i', '!', 2)  # Replace only first 2 occurrences

# Note: These methods don't change the original string!
# Strings are immutable, so they return a NEW string

# ============================================================================
# SECTION 10: LIST METHODS
# ============================================================================
# Lists are mutable, so these methods CHANGE the original list

# Starting with a fresh list
my_list = [3, 5, 6, 3, 'dog', 'cat', False]

my_list.append("basketball")   # Adds one item to the end
# Result: [3, 5, 6, 3, 'dog', 'cat', False, 'basketball']

my_list.extend(["baseball", 1])  # Adds multiple items to the end
# Result: [..., 'basketball', 'baseball', 1]

my_list.remove("cat")          # Removes first occurrence of 'cat'
my_list.pop()                  # Removes and returns last item
my_list.pop(0)                 # Removes and returns item at index 0

# ============================================================================
# SECTION 11: SET METHODS
# ============================================================================
# Sets automatically remove duplicates

my_set = {'Jason', 'jason', 'chicken'}  # Only unique values stored

my_set.add("fuzz")             # Adds one item
my_set.update(['item1', 'item2'])  # Adds multiple items
my_set.remove("Jason")         # Removes specific item

# Set operations (mathematical set theory)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

set_a.difference(set_b)        # Items in set_a but not in set_b: {1, 2}
set_a.intersection(set_b)      # Items in both sets: {3, 4}
set_a.union(set_b)             # All items from both sets: {1, 2, 3, 4, 5, 6}
set_a.symmetric_difference(set_b)  # Items in either set but not both: {1, 2, 5, 6}

# ============================================================================
# SECTION 12: DICTIONARY METHODS
# ============================================================================

my_dict = {'name': 'Jane', 'age': 23, 'fav_foods': ['pizza', 'fruit']}

# Adding/updating key-value pairs
my_dict.update([("rain", True), ("cars", "a lot")])
# Result: {'name': 'Jane', 'age': 23, 'fav_foods': [...], 'rain': True, 'cars': 'a lot'}

# Accessing dict data
my_dict.keys()     # Returns all keys: dict_keys(['name', 'age', 'fav_foods', ...])
my_dict.values()   # Returns all values: dict_values(['Jane', 23, [...], ...])
my_dict.items()    # Returns key-value pairs as tuples

# Removing items
my_dict.pop("age")  # Removes 'age' key and returns its value (23)




# ============================================================================
# KEY TAKEAWAYS FROM MY LEARNING
# ============================================================================

"""
1. Python has both MUTABLE (can change) and IMMUTABLE (cannot change) types
   - Mutable: lists, dicts, sets
   - Immutable: strings, tuples, numbers

2. Methods vs Functions:
   - Functions: called directly, e.g., len(my_list)
   - Methods: called on objects with dot notation, e.g., my_list.append(5)

3. Indexing starts at 0 in Python
   - Use negative indices to count from the end: -1 is last item

4. Following PEP 8 style makes code professional and readable

5. Comments and docstrings help explain WHY code exists, not just WHAT it does
"""
dict_1

dict_1.keys()


