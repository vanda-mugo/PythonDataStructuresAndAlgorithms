"""
Review
2 min

In this lesson, you have successfully built a
Preview: Docs Loading link description
Binary Search Tree
(BST) data structure in Python. You have implemented:

    a BinarySearchTree class containing value, depth, and left and right child nodes.
    an .insert()
    Preview: Docs A method is a small piece of code, usually defined in a class, that can be used outside the class and in other parts of the program.
    method
    to place a node of a specified value at the correct location in the Binary Search Tree. The time efficiency of this operation is O(logN) 
    for a balanced tree - if there are N nodes in the BST, the max depth of a balanced tree is log(N). So, this method makes at most log(N) 
    value comparisons. In the worst case of an imbalanced tree (all values on one side), the performance would be O(N).
    a .get_node_by_value() method to retrieve a node in the tree by its value. The time efficiency of this operation is also O(logN) for a balanced tree - 
    if there are N nodes in the BST, the max depth of the tree is log(N), so this method makes at most log(N) value comparisons. 
    In the worst case of an imbalanced tree (all values on one side), the performance would be O(N).
    a .depth_first_traversal() method to print the
    Preview: Docs First traverses the left subtree, then the root, and then the right subtree.
    inorder traversal
    of the Binary Search Tree. This visits every single node, so if there are N nodes, the time efficiency for traversal is O(N).

Great job! The Binary Search Tree is a dynamic data structure that provides efficient insertion and searching of data. 
It has the benefit of being easily expandable while maintaining a sorted order of the data. In more complex implementations, we could include:

    a .delete() method
    a self-balancing feature as data is inserted that maintains that two sides of the tree are even, guaranteeing a max depth of log(N)

Try these out for yourself if you are up for the challenge!
"""




"""
Traversing A Binary Search Tree
14 min

There are two main ways of traversing a binary tree: breadth-first and depth-first. With breadth-first traversal, we begin traversing at 
the top of the tree’s root node, displaying its value and continuing the process with the left child node and the right child node. 
Descend a level and repeat this step until we finish displaying all the child nodes at the deepest level from left to right.

With depth-first traversal, we always traverse down each left-side branch of a tree fully before proceeding down the right branch. However, 
there are three traversal options:

    Preorder is when we perform an action on the current node first, followed by its left child node and its right child node
    Inorder is when we perform an action on the left child node first, followed by the current node and the right child node
    Postorder is when we perform an action on the left child node first, followed by the right child node and then the current node

For this lesson, we will implement the
Preview: Docs Loading link description
inorder traversal
option. The advantage of this option is that the values are displayed in sorted order from the smallest to the largest value.

To illustrate, let’s say we have a binary tree that looks like this:

           15
     /------+-----\
    12            20
   /   \         /   \   
 10     13     18     22
 / \   /  \    / \   /  \
8  11 12  14  16 19 21  25

We begin by traversing the left subtree at each level, which brings us to the nodes with values 8, 10, and 11. The inorder traversal would be:

8, 10, 11

We ascend one level up to visit root node 12 before we descend back to the bottom where the right subtree of 12, 13, and 14 resides. 
Inorder traversal then continues with the values:

12, 12, 13, 14

We again ascend one level up to visit root node 15 before we traverse the right subtree starting at the bottom level again. We continue with 
the bottom leftmost subtree where 16, 18, and 19 reside. The inorder traversal continues with:

15, 16, 18, 19

We ascend one level up to visit root node 20 before we descend back to the bottom where the rightmost subtree containing nodes with values 21, 22, and 25 resides.

Traversal finishes with:

20, 21, 22, 25

The entire inorder traversal becomes:

8, 10, 11, 12, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 25

Notice that all the values displayed are sorted in ascending order.

Now let’s implement this inorder traversal for the BinarySearchTree class!
"""


import random

class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None

  def insert(self, value):
    if (value < self.value):
      if (self.left is None):
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        self.left.insert(value)
    else:
      if (self.right is None):
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)
        
  def get_node_by_value(self, value):
    if (self.value == value):
      return self
    elif ((self.left is not None) and (value < self.value)):
      return self.left.get_node_by_value(value)
    elif ((self.right is not None) and (value >= self.value)):
      return self.right.get_node_by_value(value)
    else:
      return None
    


# inorder implementation where we start with left child, current node then right
  def depth_first_traversal(self):
    if (self.left is not None):
      self.left.depth_first_traversal()
    print(f'Depth={self.depth}, Value={self.value}')
    if (self.right is not None):
      self.right.depth_first_traversal()


print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

for x in range(10):
  tree.insert(random.randint(0, 100))
  
print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()