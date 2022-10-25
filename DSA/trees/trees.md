# TREE

A tree is a data structure that starts from the root and branches out into leaves. It is a non-linear data structure. It is considerable like an extension of a Linked List and like a subset of a Graph. A tree must be completely connected and there are never cycles inside a tree. It is oriented vertically, top down.

A tree can be divided in levels, that depends on the heigth of the actual node. The nodes are called partend and child when descripting their relationship. The highest is the partent, the lowest is the child.
The height of a node are the element between the element itself and the leaves. The Depth of a node is the number of edges between the node and the root. The height of a tree is the height of the root.

## PROS

1. His structure can be used in a lot of cases depending of some more carateristics
2. It gives an hierarchical structure

## CONS

1. Can be quite complicated to handle expecially for beginners

## GOOD USE CASES

1. Machine Learning 
2. XML parsing

## BAD USE CASES

1. When another data structure easier to handle is better (most of the cases)

## TABLE OF TIME COMPLEXITY

| Operation | Time Complexity |
|-----------|-----------------|
| Search    | O(n)            |
| Insert    | O(n)            |
| Delete    | O(n)            |

Other more specific trees types has different complexities and use cases. 

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
```