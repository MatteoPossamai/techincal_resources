# HEAP

An heap is a tree-based data structure that satisfies the heap property. The heap property is that the value of each node is greater than or equal to the value of its parent, with the minimum-value element at the root. This implementation uses a min-heap. They can have any number of children (they are not binary).
The insertion is made from left to right. Find the maximum or the minimum value, depending on the heap type (whether it is a min-heap or a max-heap) is a constant operation O(1). Search in general takes O(n), even if there are some cases that takes O(n) like to find a element that is bigger than the root, that is for sure not in the structure. 

To insert a new element, we first put it in the first open spot at the bottom of the heap, and then we heapify the structure. Heapiffy is a recursive operation that takes O(log n) time.
The Heapify process consists in comparing the element with his parent, and if the element is smaller than the parent, we swap them. We do this until the element is in the right position.

Usually, heaps are rappresented as arrays. It is an array sorted in descenting order, and the root is the first element of the array. It is made via array because it is more convenient in terms of memory.

## TABLE OF TIME COMPLEXITY

| Operation | Time Complexity |
|-----------|-----------------|
| Search    | O(n)            |
| Insert    | O(log n)        |
| Delete    | O(log n)        |

## CODE EXAMPLES

### Python

```python

class MinHeap:
      
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 
  
    def parent(self, i):
        return (i-1)/2
      
    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)           
  
    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])
              
    # Method to remove minium element from min heap
    def extractMin(self):
        return heappop(self.heap)
  
    # This functon deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()
  
    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]

## OR with simpler approach

heap = [1,2,3,4,5,6,6,7,8]

```