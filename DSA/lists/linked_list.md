# LINDED LISTS

Linked lists are data structures that looks like chains. Each element of the list is called a node, and each node has a value and a pointer to the next node. 
The last node of the list points to null. You don't know the length of a liked list a priori, but you need to compute it. This can be done in O(n) time.
It is quite better when it comes to adding and deleting elements in the middle of the list, but it is quite expensive when it comes to accessing an element (O(n)).

## PROS
1. It is quite easy to add and delete elements in every position in the linked list.

## CONS
1. It is quite difficult and expensive to access an element in the linked list (O(n)).
2. You have less a priori knowledge about the linked list, and you need to compute them (O(n)).

## GOOD USE CASES
1. When you need to add or delete elements in a linked list frequently.

## BAD USE CASES
1. When you need to access a given element in a constant time. IE: Binary Search.

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
# Create a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    return
                current = current.next

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

# Create a Node
head = Node(1)

# Create a linked list
ll = LinkedList(head)
ll.add(2)
ll.add(3)
ll.add(4)

# Delete an element
ll.delete(2)

# Print the linked list
ll.print()

## FOR MORE COMPLETE CODE, CHECK THE FILE linked_list.py IN THIS DIRECTORY
```

## PLUS 
Linked Lists can also be doubly, that means that they also have a pointer to the previous element. This is useful when you need to traverse the list backwards. 

A linked list can also be circular, if the last element points to the first element. This is useful when you need to traverse the list in a circular way.

## RESOURCES
- [Linked List](https://www.geeksforgeeks.org/linked-list-set-1-introduction/)
- [Doubly Linked List](https://www.geeksforgeeks.org/doubly-linked-list/)
- [Circular Linked List](https://www.geeksforgeeks.org/circular-linked-list/)

## SOLVED QUESTIONS
### HACKERRANK
 - [ Print in reverse] (https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem?isFullScreen=true) (Easy)
 (Recursive approach, that makes you arrive in the last position, and them prints out everything backwards)
 
    