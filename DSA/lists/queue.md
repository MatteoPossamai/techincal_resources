# QUEUE

Queues are data structures that uses a FIFO approach. It means that the Fist In the queue is also the First that goes Out of it. It has a head and a tail, that rappresent the first element and the last element stored in it. To add an element on the bottom of the queue, you need to Equeue it, while to put it away from the top of the queue, you need to dequeue it. These are the basics operations you can do with a queue. 

## PROS
1. The enqueue and dequeue takes constant time O(1)

## CONS
2. Other operations are quite time consuming

## GOOD USE CASES
1. When you need to create a queue to a resources, or you need to keep an order in a very important time
2. They are used in Multiprogramming, Netwoek, Job scheduling, Shared resources and also Operating Systems

## BAD USE CASES
1. When you need to sort or search for an element

## TABLE OF TIME COMPLEXITY
| Operation | Time Complexity |
|-----------|-----------------|
| Access    | O(n)            |
| Search    | O(n)            |
| Insert    | O(1)            |
| Delete    | O(1)            |
| Length    | O(n)            |

## CODE EXAMPLES
### Python
```python
# Simple Queue implementation in Python
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            data = self.storage[0]
            self.storage = self.storage[1:]
            return data

# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Note that all these are operations on a list, so you can also handle this directly on them without passing through a class
```

## PLUS 
There are also alternatives types of queues, like Deques, that are queue into you can enqueue and dequeue from both the side, both from head and tail.

There is also the priority queue. It means that each element are inserted with a parameter called prioority. Each time that an element is dequeued it the one with the highest priority. It there are two elements with the same priority, the first element to get dequeued is the oldest one. 

There are also circular queue, that are data structures with the same concept of circular linked lists. 

## RESOURCES
1. [Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
2. [GeeksforGeeks](https://www.geeksforgeeks.org/queue-data-structure/)
3. [TutorialsPoint](https://www.tutorialspoint.com/data_structures_algorithms/queue_data_structure.htm)