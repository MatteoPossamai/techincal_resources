# COMPLEXITY

It is the basics of coding interview. It helps to find the best solution to each problem with multiple different approaches. It is a very important topic to learn. This concepts can be split in two different parts:
1. Time Complexity
2. Space Complexity

They together are the complete complexity of a problem.

## Time Complexity

It is a measure of how fast an algorithm is. 

## Space Complexity

It measures the amount of memory an algorithm uses.

## WHICH is better?

If two different solution have the same time complexity, then the one with less space complexity is better.
But if one has better time complecity, but worse space complexity, the best solution depends on the problem and the usecases that this problem has.

## NOTE

- For each data structure, each operation has a time complexity, and a space complexity.
- To solve a proble, you need to know what data structure to use, according to how efficient they are in doing what you need to do.

## Memory

When you create a data, like a variable, you need to save it into a memory location. The total memoty of machine if finite and bounded, so there is a finite number of memory that can be allocated. This is the reason why we need to know the space complexity of an algorithm.

### DICTONARY

- BIT: one digit that is either 0 or 1
- BYTE: 8 bits
- Fixed Width integer: a number that is represented by a fixed number of bits
- Pointer: variable that stores the address of another variable

# BIG O NOTATION

It is not possible to measure the time of an algorithm in seconds because it depends on the machine that is running it, so you need a different approach. It measures how fast the algorithm is given the size of the input. 

A way to describe the coplexity of an algorithm is the Big O notation, that is a way to describe how many times the dominant operation is executed. 

The Standard and most used Big O Notations are:
- O(1): Constant (ie. accessing an element in an array)
- O(log n): Logarithmic (ie. binary search)
- O(n): Linear (ie. searching an element in an array)
- O(n log n): Log Linear (ie. merge sort)
- O(n^2): Quadratic (ie. bubble sort)
- O(2^n): Exponential (ie. recursive fibonacci)
- O(n!): Factorial (ie. recursive permutation)
You need to put there only number, avoiding the constant, because they don't matter. For example, O(2n) is O(n), because the constant 2 is not that relevant. In case there are multiple values, you need to take the highest one. For example, O(n^2 + n) is O(n^2), because n^2 is the highest value, and the analysis is asyntoptic.

The n operation is the dominant operation, so the complexity is the number of times that operation is executed.

## CASES

The Big O notation is used to describe the worst case scenario, because it is the most important one.
The cases are some different sitios that can happen in an algorithm, and they are:
- Best Case: the best scenario that can happen
- Worst Case: the worst scenario that can happen
- Average Case: the average scenario that can happen

Example: quick sort
- Best Case: O(n log n)
- Worst Case: O(n^2)
- Average Case: O(n log n)

## Multiple inputs

If you have multiple inputs, you need to combine them, and maintain both of them, without dropping none of them, because they are both important. There are cases into the Big O notation of an algorithm is O(n + m), where n and m are the number of inputs.

# In depth: Logaritm

The logaritm is the inverse of the exponentiation. For example, log2(8) = 3, because 2^3 = 8. The logaritm is the number of times that you need to apply the exponentiation to get the result. The logaritm is the number of times that you need to divide a number by 2 to get 1. For example, log2(8) = 3, because 8/2 = 4, 4/2 = 2, 2/2 = 1. The logaritm is the number of times that you need to divide a number by 2 to get 1. For example, log2(8) = 3, because 8/2 = 4, 4/2 = 2, 2/2 = 1.

logb (n) = x means that b^x = n

In computer science, the logarithm is used as only the power of 2, so it is log2(n), but we will always call it log(n).

log(n) = x means that 2^x = n

In the complexity, the logarithm rise by one if the couter part double itself. This mean that it actually does not rise that quicklu, so it is a really good complexity. For example, if you have an array of 8 elements, you need to do 3 operations to find the element, because 2^3 = 8. If you have an array of 16 elements, you need to do 4 operations to find the element, because 2^4 = 16. If you have an array of 32 elements, you need to do 5 operations to find the element, because 2^5 = 32, and so on. 

The logarithm is the complexity of an algorithm if it, every time, cut off half of the input elements, like in binary search or similar. 