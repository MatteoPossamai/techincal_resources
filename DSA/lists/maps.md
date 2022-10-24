# HASHMAP

A HashMap is a map that uses a hash table to store its elements. It is
implemented as a HashMap<K, V> struct, which is generic over the types of its
keys and values. It retrieves and stores values based on the hash of its keys in constant time.

It uses a hash function to compute an index into an array of buckets or slots

## PROS

1. It is quite easy to add and delete elements in a HashMap.
2. It is quite easy to access an element in a HashMap.

## CONS

1. It is quite difficult and expensive to access an element in a HashMap (O(n)).
2. You have less a priori knowledge about the HashMap, and you need to compute them (O(n)).
3. It is quite difficult to iterate over a HashMap.

## GOOD USE CASES

1. When you need to add or delete elements in a HashMap frequently.
2. When you need to access a given element in a HashMap in constant time.

## BAD USE CASES

1. When you need to access a given element in a HashMap in constant time. IE: Binary Search.

## TABLE OF TIME COMPLEXITY

| Operation | Time Complexity |
|-----------|-----------------|
| Access    | O(1)            |
| Search    | O(n)            |
| Insert    | O(1)            |
| Delete    | O(1)            |
| Length    | O(n)            |


## CODE EXAMPLES

### Python

```python
# Create a HashMap
a = {}

# Add a key-value pair
a['key'] = 'value'

# Delete a key-value pair
del a['key']

# Access a value
a['key']

# Iterate over a HashMap
for key, value in a.items():
    print(key, value)
```

