# MATRIX

Matrix is a 2D array of numbers. It is used to represent transformations in 2D space.
They are really useful for a lot of usecases, like Graphics, Computer Vision, Graph Theory, etc.

## PROS

1. They are really useful for a lot of usecases, like Graphics, Computer Vision, Graph Theory, etc.
2. They are really easy to implement.

## CONS

1. They are quite heavy both in term of memory and time complexity.
2. They are not really useful for a lot of usecases.

## GOOD USE CASES

1. When you need to represent transformations in 2D space.
2. When you need to represent a graph.

## BAD USE CASES

1. When you need to represent a graph with too little edges.

## TABLE OF TIME COMPLEXITY

| Operation | Time Complexity |
|-----------|-----------------|
| Access    | O(1)            |
| Search    | O(n)            |
| Insert    | O(n)            |
| Delete    | O(n)            |
| Length    | O(1)            |

As n is the number of cells in the matrix.
If the matrix is n x m, then n => n * m.

## CODE EXAMPLES
```python
# Create a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access an element
print(matrix[0][0]) # 1

# Add an element in the end of a row
matrix[0].append(4)
```
