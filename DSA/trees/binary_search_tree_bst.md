## BINARY SEARCH TREE (BST)

The trees are not that ordered and structured per se, so there are alternatives that are more organized so they can perform certain operations faster and in a simpler way. 

Every parent node has at most two children. The left child has a value lesser than the parent node and the right child has a value greater than the parent node. Due to this property, the BST is also called as ordered or sorted binary tree. It is faster when it comes to searching, insertion and deletion.

Searching only needs to find his way checking if the number is grater or smaller. To insert you need to find a path into insert the element so that the BST is still a BST. The deletion has the same problems as the normal trees. 

## TABLE OF TIME COMPLEXITY

| Operation | Time Complexity |
|-----------|-----------------|
| Search    | O(log n)        |
| Insert    | O(log n)        |
| Delete    | O(log n)        |

##  COMPLICATIONS

A BST can be really unbalance, and that can cause a lot of problems. The worst case scenario is when the tree is a linked list, and that can cause a lot of problems. In this case, the searching becomes O(n).

## CODE EXAMPLES

### Python

```python

class Node:
     def __init__(self,data):
          self.data = data
          self.parent = None
          self.left = None
          self.right = None

     def __repr__(self):
          return repr(self.data)

     def add_left(self,node):
         self.left = node
         if node is not None:
             node.parent = self

     def add_right(self,node):
         self.right = node
         if node is not None:
             node.parent = self

class BST:
        def __init__(self):
            self.root = None
    
        def insert(self,data):
            if self.root is None:
                self.root = Node(data)
            else:
                self._insert(data,self.root)
    
        def _insert(self,data,node):
            if data < node.data:
                if node.left is None:
                    node.add_left(Node(data))
                else:
                    self._insert(data,node.left)
            else:
                if node.right is None:
                    node.add_right(Node(data))
                else:
                    self._insert(data,node.right)
    
        def find(self,data):
            if self.root is not None:
                return self._find(data,self.root)
            else:
                return None
    
        def _find(self,data,node):
            if data == node.data:
                return node
            elif data < node.data and node.left is not None:
                self._find(data,node.left)
            elif data > node.data and node.right is not None:
                self._find(data,node.right)
    
        def delete(self,data):
            if self.root is not None:
                self._delete(data,self.root)
    
        def _delete(self,data,node):
            if data == node.data:
                if node.left is None and node.right is None:
                    if node.parent is not None:
                        if node.parent.left is node:
                            node.parent.left = None
                        else:
                            node.parent.right = None
                    else:
                        self.root = None
                elif node.left is not None and node.right is not None:
                    tmp = self._find_min(node.right)
                    self.delete(tmp.data)
                    node.data = tmp.data
                else:
                    if node.left is not None:
                        if node.parent is not None:
                            if node.parent.left is node:
                                node.parent.left = node.left
                            else:
                                node.parent.right = node.left
                        else:
                            self.root = node.left
                    else:
                        if node.parent is not None:
                            if node.parent.left is node:
                                node.parent.left = node.right
                            else:
                                node.parent.right = node.right
                        else:
                            self.root = node.right
            elif data < node.data and node.left is not None:
                self._delete(data,node.left)
            elif data > node.data and node.right is not None:
                self._delete(data,node.right)
    
        def _find_min(self,node):
            if node.left is not None:
                return self._find_min
# Udacity Code
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_aux(new_val, self.root)
        
    def insert_aux(self, new_val, node):
        if node.value < new_val:
            if node.left is None:
                node.left = Node(new_val)
            else:
                self.insert_aux(new_val, node.left)
        else:
            if node.right is None:
                node.right = Node(new_val)
            else:
                self.insert_aux(new_val, node.right)

    def search(self, find_val):
        return self.search_aux(find_val, self.root)
        
    def search_aux(self, find_val, node):
        if node is None:
            return False
        elif node.value == find_val:
            return True
        elif node.value < find_val:
            return self.search_aux(find_val, node.left)
        else:
            return self.search_aux(find_val, node.right)
```

