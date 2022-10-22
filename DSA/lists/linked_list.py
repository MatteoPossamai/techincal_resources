"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

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
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position == 1:
            return self.head
        else:
            current = self.head
            idx = 1
            while position > idx and current.next != None:
                current = current.next
                idx += 1 
        return current
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        if position == 1:
            self.head = new_element
            self.head.next = current
        else:
            idx = 2
            while position > idx and current.next != None:
                current = current.next
                idx += 1
            next_element = current.next
            current.next = new_element
            new_element.next = next_element
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        if self.head.value == value:
            self.head = self.head.next
        else:
            while current.value != value or current.next == None:
                previous = current
                current = current.next
            previous.next = current.next

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        

def reverse(llist):
    prev, current = None, llist
    while current:
        cnext = current.next
        current.next = prev
        prev = current
        current = cnext        
    return prev

## IF IT IS DOUBLY LINKED (WITH A PREVIOUS)
def reverse(llist):
    # Write your code here
    prev, current = None, llist
    
    while current:
        node = current.next
        current.next = prev
        current.prev = node
        prev = current
        current = node
        
    return prev

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test insert
ll.insert(e4,3)

# Test delete
ll.delete(1)

# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)