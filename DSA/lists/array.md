# ARRAYS

Arrays are data structures where the object may or may not be of the same type.
Sometimes they have a fixed length while sometimes they are dynamic.
Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value. They have indexes that are numeric and starts from 0, to length minus 1.

## PROS
1. Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.
2. They have indexed that let us to access it easily and quickly (O(1)).

## CONS
1. It is quite difficult to add and delete an element in the middle of an array, and is quite expensive      (O(n))

## GOOD USE CASES
1. Algorithms where you need to access a given element in a constant time. IE: Binary Search.
2. When you need to store a list of elements.

## BAD USE CASES
1. When you need to add or delete elements in an arary frequently. IE: Linked List.

## TABLE OF TIME COMPLEXITY
| Operation | Time Complexity |
|-----------|-----------------|
| Access    | O(1)            |
| Search    | O(n)            |
| Insert    | O(n)            |
| Delete    | O(n)            |
| Length    | O(1)            |

## CODE EXAMPLES
### Python
```python
# Create an array
arr = [1, 2, 3, 4, 5]

# Access an element
print(arr[0]) # 1

# Add an element in the end of an array
arr.append(6)

# Delete an element
del arr[0]
```

## RESOURCES
- [Wikipedia](https://en.wikipedia.org/wiki/Array_data_structure)
- [GeeksforGeeks](https://www.geeksforgeeks.org/array-data-structure/)