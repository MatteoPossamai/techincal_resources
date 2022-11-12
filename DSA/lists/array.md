# ARRAYS

Arrays are data structures where the object may or may not be of the same type.
Sometimes they have a fixed length while sometimes they are dynamic.
Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value. They have indexes that are numeric and starts from 0, to length minus 1.

In the memory, arrays are stored in a contiguous block of memory, which means that the elements of the array are stored one after the other. This makes it easier to access the elements of the array, as we know the exact location of each element. Usually, in the majority of programming languages, all the element in the array are of the same data type, even though some languages allow arrays to store elements of different data types.

The effective size of an array in memory is obtained multiplying the the size of the data type and the number of elements stored in the array.

Array can be static or dynamic, it depends on the language. In static arrays, the size of the array is fixed, while in dynamic arrays, the size of the array is not fixed.

If the array is dynamic, the OS will store almost double the size of the array, in order to be able to expand the array if needed. The time complexity of expanding the array is O(n), where n is the number of elements in the array.

## PROS
1. Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.
2. They have indexed that let us to access it easily and quickly (O(1)).

## CONS
1. It is quite difficult to add and delete an element in the middle of an array, and is quite expensive      (O(n))

## GOOD USE CASES
1. Algorithms where you need to access a given element in a constant time. IE: Binary Search.
2. When you need to store a list of elements.

## BAD USE CASES
1. When you need to add or delete elements in an array frequently. IE: Linked List.

## TABLE OF TIME COMPLEXITY
| Operation | Time Complexity |
|-----------|-----------------|
| Access    | O(1)            |
| Set       | O(1)            |
| Init      | O(n)            |
| Traversal | O(n)            |
| Copy      | O(n)            |
| Pop       | O(1)            |
| Search    | O(n)            |
| Insert    | O(n)            |
| Delete    | O(n)            |
| Length    | O(1) or O(n)    |

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