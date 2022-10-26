## SELF BALANCING TREES

It is a special type of tree that with algorithms tries to keep itself as much balanced as possible. The most common self-balancing trees are AVL trees and Red-Black trees.

### RED-BLACK TREES

It is a tree with a color code. All the nodes that have one child and the root are black, while the leaves are red. The number of blacks must be the same for both the sutrees.

### AVL TREES

In this particular tree, the height of the left and right subtree of every node differ by at most one. If at any time they differ by more than one, rebalancing is done to restore this property.

### RED-BLACK TREE VS AVL TREE

They are often compared because they are both self-balancing trees. The main difference is that AVL trees are more rigidly balanced than red-black trees, which makes AVL trees faster than red-black trees. However, red-black trees are more flexible and can be used in many more situations than AVL trees.

Usually, both them have around O(log n) for basic operations like insertion, deletion and search. However, AVL trees are faster than red-black trees because they are more rigidly balanced.

### ROTATIONS

Rotations are used to balance the tree. There are two types of rotations: left and right. They are used to keep the tree balanced. In this operations, usually all the childs switch their position from a side to the other of the partent node. The left rotation is used when the right subtree is too big, while the right rotation is used when the left subtree is too big. Rotation is a O(log n) operation.