# HASHtable

A hash table is a data structure that maps keys to values in a sort of couple of elements, and it links them so that reading the value given the key, searching for the key, insertion and deletion have a time complexity of O(1).
The keys are unique, so cannot be repeated, but they can also be data that are not integers, such as strings, or even other data structures.
Under the hood, you use a hash function to transform the key into an integer, which is used to index the table, and then the value is stored in the corresponding position. This is why it is so performant in that set of operations.

## Hash function
An hash function is a function that convert a string or a generic value into a integer. For example, a possible hash function given a string can be that, for each charactedr, you sum all the ASCII values of the characters, and then you take the modulo of the sum with the size of the table.
The hash function must always be the same, so that the same key always gives the same index, and the index must be in the range of the table.
If a hash function points two times in the same index, it is called a collision, and to solve it the array become an array of linked lists, and the value is inserted in the linked list of the index. To know which data in the linked list is the correct one, you need that each data has a pointer to the key itself, so you can compare the key of the data with the key you are searching for.

So, under the hood, hash tables have constant time to archieve his operation on average, but there are sometimes into it comes to be O(n), if everything that is inside the table is in the same linked list. So, a really good hash function is needed to avoid this.

## PROS

1. It is almost unexpensive to add and delete elements in a Hashtable.
2. It is almost unexpensive to access an element in a Hashtable.

## CONS

1. You have less a priori knowledge about the Hashtable, and you need to compute them (O(n)).
2. It is quite difficult to iterate over a Hashtable.

## GOOD USE CASES

1. When you need to add or delete elements in a Hashtable frequently.
2. When you need to access a given element in a Hashtable in constant time.

## BAD USE CASES

1. When you need to access a given element in a Hashtable in constant time. IE: Binary Search.

## TABLE OF TIME COMPLEXITY

| Operation | Time Complexity |
|-----------|-----------------|
| Access    | O(1)            |
| Search    | O(1)            |
| Insert    | O(1)            |
| Delete    | O(1)            |
| Length    | O(n)            |


## CODE EXAMPLES

### Python

```python
# Create a Hashtable
a = {}

# Add a key-value pair
a['key'] = 'value'

# Delete a key-value pair
del a['key']

# Access a value
a['key']

# Iterate over a Hashtable
for key, value in a.items():
    print(key, value)
```

