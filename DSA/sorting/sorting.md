# SORTING

Sorting algorithms are algorithms that rearrange a given data structure in a specific order. 

## BUBBLE SORT

It continues to change adiacent elements if they are not in the correct order. It is a simple algorithm, but it is very inefficient. It has a time complexity of O(n^2).

### HOW DOES IT WORK?

It checks the first two element, and if they are not sorted, it swap them. Then it checks the second and the third. At the end of all this, the largest element is at the end of the array. Then it starts again, but it stops at the last element, because it is already sorted. It continues until the array is sorted.

### PROS

- It is very simple to implement

### CONS

- It is very inefficient
- There are no case into it is the best choice

### PSEUDOCODE

    for i = 1 to n
        for j = 1 to n - i
            if a[j] > a[j + 1]
                swap a[j] and a[j + 1]


## SELECTION SORT

For each iteration, it searches the smallest element in the subarray, and puts it in the first position. Then, it checks only from the second and repeats the process. It has a time complexity of O(n^2), where n is the number of elements in the data structure. 

### HOW DOES IT WORK

It finds the smalles element in the array, and put it in the first position. Then it checks all the array except the first element. Now it repeats for the rest of the array, until it is sorted.

### PROS

- Easy to implement
- Performs well in small data sets
- Performs well in already sorted data sets

### CONS

- It takes a long time to be executed in medium-large data sets.

### PSEUDOCODE

    for i = 1 to n
        min = i
        for j = i + 1 to n
            if a[j] < a[min]
                min = j
        swap a[i] and a[min]

## INSERTION SORT

It is a sorting algorithm that builds the final sorted array (or list) one item at a time. It has a time complexity of O(n^2), where n is the number of elements in the data structure, checking 

### HOW DOES IT WORK
It takes from the second card, and puts in in the correct place in the subarray of the elements that have already been sorted. It does this until it is sorted.

### PROS

- It is very efficient when the data structure is almost sorted.
- Easy to implement
- Performs well in small data sets
- The ability to sort a list as it is being received.

### CONS

- Insertion sort is inefficient against more extensive data sets.
- The insertion sort exhibits the worst-case time complexity of O(n2)
- It does not perform well than other, more advanced sorting algorithms.

### PSEUDOCODE
    
        for i = 2 to n
            x = a[i]
            j = i - 1
            while j > 0 and a[j] > x
                a[j + 1] = a[j]
                j = j - 1
            a[j + 1] = x   

## SHELL SORT

It is an algorithm that sorts a list by comparing elements that are far apart from each other, then progressively reducing the gap between elements to be compared. It has a time complexity of O(n^2), where n is the number of elements in the data structure.

### HOW DOES IT WORK

It starts by comparing elements that are far apart from each other, then progressively reducing the gap between elements to be compared. It does this until the gap is 1, and it is the same as the insertion sort.

### PROS

- It is very efficient when the data structure is almost sorted.
- Easy to implement
- Performs well in small data sets

### CONS

- It is inefficient against more extensive data sets.
- The insertion sort exhibits the worst-case time complexity of O(n^(3/2))

### PSEUDOCODE

    for gap = n/2 to 1
        for i = gap to n
            x = a[i]
            j = i - gap
            while j > 0 and a[j] > x
                a[j + gap] = a[j]
                j = j - gap
            a[j + gap] = x

## QUICK SORT

It is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

### HOW DOES IT WORK

It picks an element as pivot and decide that it is in the right position. Then, it puts all the smallest in his left and all the larger or his right. Then, it does the same for the subarrays of the smaller and larger elements. It has a time complexity of O(n log n), where n is the number of elements in the data structure. It makes this algorithm very efficient.

### PROS

- It is very efficient when the data structure is almost sorted.
- Very performant

### CONS

- Bit more complex to imlpement and understand

### PSEUDOCODE

    function quickSort(arr, left, right)
        if left < right
            pivotIndex = partition(arr, left, right)
            quickSort(arr, left, pivotIndex - 1)
            quickSort(arr, pivotIndex + 1, right)
    
    function partition(arr, left, right)
        pivot = arr[right]
        i = left
        for j = left to right - 1
            if arr[j] < pivot
                swap arr[i] and arr[j]
                i = i + 1
        swap arr[i] and arr[right]
        return i

## MERGE SORT

It is a divide and conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

### HOW DOES IT WORK

It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. It has a time complexity of O(n log n), where n is the number of elements in the data structure. It makes this algorithm very efficient. It is recursive.

### PROS

- It is very efficient when the data structure is almost sorted.
- Very performant
- Fastest sorting algorithm for large data sets

### CONS

- Bit more complex to imlpement and understand

### PSEUDOCODE

    function mergeSort(arr, l, r)
        if l < r
            m = (l + r) / 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
    
    function merge(arr, l, m, r)
        n1 = m - l + 1
        n2 = r - m
        L = new array of size n1
        R = new array of size n2
        for i = 1 to n1
            L[i] = arr[l + i - 1]
        for j = 1 to n2
            R[j] = arr[m + j]
        i = 1
        j = 1
        k = l
        while i <= n1 and j <= n2
            if L[i] <= R[j]
                arr[k] = L[i]
                i = i + 1
            else
                arr[k] = R[j]
                j = j + 1
            k = k + 1
        while i <= n1
            arr[k] = L[i]
            i = i + 1
            k = k + 1
        while j <= n2
            arr[k] = R[j]
            j = j + 1
            k = k + 1