# SEARCHING ALGORITHMS

Searching algorithms are all the algorithms that solves the searching problem, meaning that they try to find an element in a given data structure, and eventually return its position. The output of a searching algorithm is a boolean value, which is true if the element is found, and false otherwise, or the position if the algorithm is designed in this particular way. There are two types of algorithms:

- [Sequential Search] [It is a searching algorithm that sequentially checks each element of the data structure until the desired one is found. IE: Linear Search]
- [Interval Search] [It is a searching algorithm that checks if the element is in a given interval, and changes it dinamically. IE: Binary Search]

## LINEAR SEARCH

It is the simplest algorithm. It sequentially checks each element of the data structure until the desired one is found. It is a very inefficient algorithm, because it has a time complexity of O(n), where n is the number of elements in the data structure. It is used when the data structure is not ordered, and the number of elements is small. Otherwise, it is better to use a more efficient algorithm.

### HOW DOES IT WORK
It reads each element in the data structure, and compares it with the element we are looking for. If the element is found, it returns true, otherwise it returns false.

### PROS
- It is very simple to implement.
- It is very easy to understand.
- Is very efficient when the number of elements is small.

### CONS
- It is very inefficient when the number of elements is big.
- It is very inefficient when the data structure is ordered.

## BINARY SEARCH
Binary search algorithm works on the principle of divide & conquer and it is considered the best searching algorithms because of its faster speed to search. It has a time complexity of O(log n), where n is the number of elements in the data structure. It is used when the data structure is ordered, and the number of elements is big. Otherwise, it is better to use a more efficient algorithm. In fact, the sorting problem is heavier to resolve. 

### HOW DOES IT WORK
It takes the position in the half of the data structure (array). If it is what is was searching for, it return true, otherwise checks if it is bigger or smaller than the element. If it is bigger, it now only checks the first half of the data structure, and if it is smaller, it checks the second half. It does this until it finds the element, or it returns false.

### PROS
- It is very efficient when the number of elements is big.
- It is very efficient when the data structure is ordered.

### CONS
- It is very inefficient when the number of elements is small.
- It is very inefficient when the data structure is not ordered.

## JUMP SEARCH

It uses still an ordered data structure. It is a searching algorithm that checks if the element is in a given interval, and changes it dinamically. It has a time complexity of O(sqrt(n)), where n is the number of elements in the data structure. It is used when the data structure is ordered, and the number of elements is big. Otherwise, it is better to use a more efficient algorithm. I

### HOW DOES IT WORK

It starts from the first index (0), and checks. Then, he choose a value, that is the jump value. It is the square root of the number of elements in the data structure (for obtimal performance). It checks the element in the position of the jump value. If it is smaller, it checks the elements between the previous position and the current one. If it is bigger, it checks the elements between the current position and the next one. It does this until it finds the element, or it returns false.

### PROS
- It is very efficient when the number of elements is big.
- It is very efficient when the data structure is ordered.

### CONS
- It is very inefficient when the number of elements is small.
- It is very inefficient when the data structure is not ordered.
