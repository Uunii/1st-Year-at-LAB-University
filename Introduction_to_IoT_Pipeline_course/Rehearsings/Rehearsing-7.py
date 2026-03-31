# List = [1, 2, 3]
# List.append(4) # Adds an item to the end of the list.
# print(List) # Output: [1, 2, 3, 4]

# addtoList = [1, 2, 3]
# addtoList.extend([4, 5, 6]) # Extends the list by appending elements from another list.
# print(addtoList) # Output: [1, 2, 3, 4, 5]

# insertList = [1, 2, 3]
# insertList.insert(1, 'a') # Inserts an item at a specified position.
# print(insertList) # Output: [1, 'a', 2, 3]

# removeList = [1, 2, 3, 2]
# removeList.remove(3) # Removes the first occurrence of a specified value.
# print(removeList) # Output: [1, 3, 2]

# popList = [1, 2, 3]
# item = popList.pop() # Removes and returns the item at the given position or the last item.
# print(item) # Output: 3
# print(popList) # Output: [1, 2]

# clearList = [1, 2, 3]
# clearList.clear() # Removes all items from the list.
# print(clearList) # Output: []

# indexList = [1, 2, 3]
# index = indexList.index(2) # Returns the index of the first occurrence of a specified value.
# print(index) # Output: 1

# countList = [1, 2, 2, 3]
# count = countList.count(2) # Returns the number of occurrences of a specified value.
# print(count) # Output: 2

# sortList = [3, 1, 2]
# sortList.sort() # Sorts the list in ascending order.
# print(sortList) # Output: [1, 2, 3]

# reverseList = [1, 2, 3]
# reverseList.reverse() # Reverses the order of the list.
# print(reverseList) # Output: [3, 2, 1]

# copyList = [1, 2, 3]
# newList = copyList.copy() # Returns a shallow copy of the list.
# print(newList) # Output: [1, 2, 3]

#Data structures: tuples

countTuple = (1, 2, 2, 3)
count = countTuple.count(2) # Returns the number of times a specified value appears.
print(count) # Output: 2
indexTuple = (1, 2, 3)
index = indexTuple.index(2) # Returns the index of the first occurrence of the given value.
print(index) # Output: 1

# Data structures: dictionaries

keysDict = {'a': 1, 'b': 2, 'c': 3}
keys = keysDict.keys() # Returns a list view of all the keys in the dictionary.
print(keys) # Output: dict_keys(['a', 'b', 'c'])

valuesDict = {'a': 1, 'b': 2, 'c': 3}
values = valuesDict.values() # Returns a list view of all the values in the dictionary.
print(values) # Output: dict_values([1, 2, 3])

itemsDict = {'a': 1, 'b': 2, 'c': 3}
items = itemsDict.items() # Returns a list view of dictionary’s key-value tuple pairs.
print(items) # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

getDict = {'a': 1, 'b': 2, 'c': 3}
value = getDict.get('b') # Returns the value for a specified key if the key is in the dictionary.
print(value) # Output: 2

updateDict = {'a': 1, 'b': 2}
updateDict.update({'c': 3, 'd': 4}) # Updates the dictionary with the elements from another dictionary.
print(updateDict) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

popDict = {'a': 1, 'b': 2, 'c': 3}
value = popDict.pop('b') # Removes the specified key and returns the corresponding value.
print(value) # Output: 2
print(popDict) # Output: {'a': 1, 'c': 3}

clearDict = {'a': 1, 'b': 2, 'c': 3}
clearDict.clear() # Removes all items from the dictionary.
print(clearDict) # Output: {}

defaultDict = {'a': 1, 'b': 2}
value = defaultDict.setdefault('c', 3) # Returns the value of a key.
print(value) # Output: 3
print(defaultDict) # Output: {'a': 1, 'b': 2, 'c': 3}

copyDict = {'a': 1, 'b': 2, 'c': 3}
new_dict = copyDict.copy() # Returns a copy of the dictionary.
print(new_dict) # Output: {'a': 1, 'b': 2, 'c': 3}

popItemDict = {'a': 1, 'b': 2, 'c': 3}
item = popItemDict.popitem() # Removes and returns the last inserted key-value pair as a tuple.
print(item) # Output: ('c', 3)
print(popItemDict) # Output: {'a': 1, 'b': 2}

# Data structures:sets

addSet = {1, 2, 3}
addSet.add(4) # Adds an element to the set.
print(addSet) # Output: {1, 2, 3, 4}

removeSet = {1, 2, 3}
removeSet.remove(2) # Removes the element from the set. Raises an error if the element is not found.
print(removeSet) # Output: {1, 3}

discardSet = {1, 2, 3}
discardSet.discard(2) # Removes the element from the set if it is present. Does not raise an error.
print(discardSet) # Output: {1, 3}

popSet = {1, 2, 3}
element = popSet.pop() # Removes and returns an arbitrary element from the set. Error if empty.
print(element) # Output: 1 (or any other element)
print(popSet) # Output: {2, 3} (or the remaining elements)

clearSet = {1, 2, 3}
clearSet.clear() # Removes all elements from the set.
print(clearSet) # Output: set()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
unionSet = set1.union(set2) # Returns a new set with elements from the set and all others.
print(unionSet) # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersectionSet = set1.intersection(set2) # Returns a new set with common elements.
print(intersectionSet) # Output: {2, 3}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
differenceSet = set1.difference(set2) # Returns a new set with different elements.
print(differenceSet) # Output: {1}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
symDiffSet = set1.symmetric_difference(set2) # Returns a new set with elements in either or set.
print(symDiffSet) # Output: {1, 4}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2) # Updates the set, adding elements from all others.
print(set1) # Output: {1, 2, 3, 4, 5}

# Data structures: arrays

# import array
# # Create an array of integers
# exampleArray = array.array('i', [1, 2, 3, 4])
# print(exampleArray) # Output: array('i', [1, 2, 3, 4])

# exampleArray.append(5) # Adds an element to the end of the array.
# print(exampleArray) # Output: array('i', [1, 2, 3, 4, 5])

# exampleArray.extend([6, 7]) # Extends the array by appending elements from another array.
# print(exampleArray) # Output: array('i', [1, 2, 3, 4, 5, 6, 7])

# exampleArray.insert(1, 10) # Inserts an element at a given index.
# print(exampleArray) # Output: array('i', [1, 10, 2, 3, 4, 5, 6, 7])

# exampleArray.remove(10) # Removes the first occurrence of a given value.
# print(exampleArray) # Output: array('i', [1, 2, 3, 4, 5, 6, 7])

# element = exampleArray.pop() # Removes and returns the element at the given index or the last
# print(element) # Output: 7
# print(exampleArray) # Output: array('i', [1, 2, 3, 4, 5, 6])

# index = exampleArray.index(4) # Returns the index of the first occurrence of a given value.
# print(index) # Output: 3

# exampleArray.reverse() # Reverses the order of the array.
# print(exampleArray) # Output: array('i', [6, 5, 4, 3, 2, 1])

# count = exampleArray.count(4) # Returns the number of occurrences of a specified value.
# print(count) # Output: 1

# Data structures: deques

from collections import deque
exampleDeque = deque([1, 2, 3, 4])
print(exampleDeque) # Output: deque([1, 2, 3, 4])

exampleDeque.append(5) # Adds an element to the right end of the deque.
print(exampleDeque) # Output: deque([1, 2, 3, 4, 5])

exampleDeque.appendleft(0) # Adds an element to the left end of the deque.
print(exampleDeque) # Output: deque([0, 1, 2, 3, 4, 5])

element = exampleDeque.pop() # Removes and returns an element from the right end.
print(element) # Output: 5
print(exampleDeque) # Output: deque([0, 1, 2, 3, 4])

element = exampleDeque.popleft() # Removes and returns an element from the left.
print(element) # Output: 0
print(exampleDeque) # Output: deque([1, 2, 3, 4])

exampleDeque.extend([5, 6]) # Extends the right end of the deque.
print(exampleDeque) # Output: deque([1, 2, 3, 4, 5, 6])

exampleDeque.extendleft([0, -1]) # Extends the left end of the deque in reverse order.
print(exampleDeque) # Output: deque([-1, 0, 1, 2, 3, 4, 5, 6])

exampleDeque.rotate(2) # Rotates the deque n steps to the right (or left if negative).
print(exampleDeque) # Output: deque([5, 6, -1, 0, 1, 2, 3, 4])

exampleDeque.rotate(-2)
print(exampleDeque) # Output: deque([-1, 0, 1, 2, 3, 4, 5, 6])

exampleDeque.clear() # Removes all elements from the deque.
print(exampleDeque) # Output: deque([])

exampleDeque = deque([1, 2, 2, 3, 4]) # Counts the number of occurrences of given value.
count = exampleDeque.count(2)
print(count) # Output: 2

# Data structures: named tuples

from collections import namedtuple
# Define a named tuple called 'Point'
Point = namedtuple('Point', ['x', 'y'])

# Create an instance of Point
p = Point(1, 2)
print(p) # Output: Point(x=1, y=2)

# You can access the fields of a named tuple by name.
print(p.x) # Output: 1
print(p.y) # Output: 2

# _replace() returns a new named tuple with specified fields replaced with new values.
p2 = p._replace(x=10)
print(p2) # Output: Point(x=10, y=2)

# _asdict() returns the named tuple as an OrderedDict.
p_dict = p._asdict()
print(p_dict) # Output: {'x': 1, 'y': 2}

# _fields returns a tuple of field names of the named tuple.
fields = p._fields
print(fields) # Output: ('x', 'y')

# _make() creates a new instance of the named tuple from an iterable.
p3 = Point._make([3, 4])
print(p3) # Output: Point(x=3, y=4)

# Data structures: counters

from collections import Counter
# Create a Counter from a list
exampleCounter = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(exampleCounter) # Output: Counter({'b': 3, 'a': 2, 'c': 1})

elements = list(exampleCounter.elements()) # Returns an iterator over elements repeating
# each as many times as its count.
print(elements) # Output: ['a', 'a', 'b', 'b', 'b', 'c']

common = exampleCounter.most_common(2) # Returns a list of the n most common elements
# and their counts from the most common to the least.
print(common) # Output: [('b', 3), ('a', 2)]

exampleCounter.subtract(['a', 'b', 'b']) # Subtracts element counts from another
# iterable or counter.
print(exampleCounter) # Output: Counter({'b': 1, 'a': 1, 'c': 1})

exampleCounter.update(['a', 'b', 'b', 'd']) # Adds counts for elements from another
# iterable or counter.
print(exampleCounter) # Output: Counter({'b': 3, 'a': 2, 'c': 1, 'd': 1})

new_counter = exampleCounter.copy() # Returns a shallow copy of the counter.
print(new_counter) # Output: Counter({'b': 3, 'a': 2, 'c': 1, 'd': 1})

exampleCounter.clear() # Removes all elements from the counter.
print(exampleCounter) # Output: Counter()