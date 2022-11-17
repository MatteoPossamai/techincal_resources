# TREE

A tree is a data structure that starts from the root and branches out into leaves. It is a non-linear data structure. It is considerable like an extension of a Linked List and like a subset of a Graph. A tree must be completely connected and there are never cycles inside a tree. It is oriented vertically, top down.

A tree can be divided in levels, that depends on the heigth of the actual node. The nodes are called partend and child when descripting their relationship. The highest is the partent, the lowest is the child.
The height of a node are the element between the element itself and the leaves. The Depth of a node is the number of edges between the node and the root. The height of a tree is the height of the root.

The search takes O(n) because you need to traverse the entire tree searching for the specific node. The deletion is usually a search followed by a deletion of the node.  There may be issues with the deletion of the node, because the node may have children. So, if you want to keep data, you need to upgrade childsa and get rid of voids.

Inserting an element if there is no specific order is simple. You just need to add the element to the end of the tree. If there is a specific order, you need to find the right place for the element.

## TREES NAMES BASED ON THE NUMBER OF CHILDREN

If a tree can have at most two child, it is called a binary tree, if it can have at most three children, it is called a ternary tree, and then you can call a tree a k-ary tree if it can have at most k children.

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

## BALANCED TREES

A tree is considered balanced when the complexity of the traversal of only half of the tree, is around O(log n), meaning that each time it cut the tree in half. So, in easier words, the tree is balanced when the height of the tree is O(log n).

## COMPLETE TREES

A tree is considere complete when each spot of the tree is filled, except the last level. The last level is filled from left to right. 

## FULL TREES

A tree is considered full when each node has either 0 or k children, when we use k as the nomber of children that the given tree can have in the largest case.

## PERFECT TREES

A tree is considered perfect when all the leaves have the same depth. It is also a complete tree.

## TABLE OF TIME COMPLEXITY

| Operation | Time Complexity |
|-----------|-----------------|
| Search    | O(n)            |
| Insert    | O(n)            |
| Delete    | O(n)            |
| Storage   | O(n)            |
| Traversal | O(n)            |
| Half Trav | O(log n)        |
| Height    | O(n)            |
| Depth     | O(n)            |

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