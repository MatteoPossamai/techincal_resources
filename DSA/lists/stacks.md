# STACKS

Stacks are data structures mainly used to store data and that ultimately cares the most about the most recent element added to the stack itself. It imlpements a LIFO (Last In First Out) policy. It means that the last element added to the stack will be the first one to be removed from the stack. It is quite similar to a stack of plates, where the last plate you put on the stack will be the first one to be removed from the stack. It can be implemented also with other data structures like Linked Lists and arrays. The two main operation that a stack can perform are: push and pop. Push is used to add an element to the stack, while pop is used to remove an element from the stack.

## PROS
1. It is very fast to add and remove elements from the stack, in fact it takes O(1) time.
2. Good for use cases where you need to keep track of the most recent element added to the stack.

## CONS
1. It is quite difficult to access an element in the stack (O(n)).
2. It is not possible to do in a performant way operations like sorting and searching.

## GOOD USE CASES
1. When you need to keep track of the most recent element added to the stack.

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
# Create a stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def print(self):
        print(self.stack)

# It can also be implemented only using simple arrays

# Create a stack
s = Stack()

# Add elements to the stack
s.push(1)

# Print the stack
s.print()

# Remove the last element added to the stack
s.pop()

# --------------------------------------------
# Alternative implementation with linked lists
# --------------------------------------------

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
       
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
       
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:
            data = self.head
            self.head = self.head.next
            return data
        return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        data = self.ll.delete_first()
        return data

# --------------------------------------------
# Alternative implementation with arrays
# --------------------------------------------

stack = []
# you treat append like push
stack.append(2)
# you treat pop like pop
print(stack.pop())
```

## RESOURCES
- [Wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
- [GeeksforGeeks](https://www.geeksforgeeks.org/stack-data-structure-introduction-program/)
