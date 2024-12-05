"""
Tree Traversal: Breadth-First Search vs Depth-First Search

Learn about two standard tree traversal algorithms: breadth-first search and depth-first search.

It’s your first day at a new job and you’ve been given a computer! You are tasked with manually finding a file somewhere in the filesystem, 
starting at the computer’s root directory. How will you do it?

Will you look quickly inside all first-level directories hoping the file is in one of them? Or will you pick one directory and search deep 
within its subdirectories for the file? Regardless of your choice, it is important to have a plan so you only search each directory once.

File systems often have the shape of a tree data structure, so there must be a way to search it in an organized way. In this article, 
we’ll discuss two methods of tree traversal: breadth-first search and depth-first search.
Breadth-first search vs. depth-first search

A breadth-first search is when you inspect every node on a level starting at the top of the tree and then move to the next level. 
A depth-first search is where you search deep into a branch and don’t move to the next one until you’ve reached the end. 
Each approach has unique characteristics but the process for each one is almost exactly the same. The only difference in their approach is how they 
store the nodes that need to be searched next. These nodes are known as the frontier.


Queues and stacks

The queue and the stack are the two data structures that can be used for storing nodes in a search frontier. A queue follows “First In First Out” (FIFO) behavior, 
where the order the data goes in the queue is the order it leaves the queue. This equates to any line you may have stood on 
to wait for the bus or to grab a cup of coffee.

A stack follows “Last In First Out” (LIFO) behavior which means that the most recent data added will be the first to leave. 
To get to a book at the bottom of a stack of books you must first remove the books that were more recently placed in the stack. 
The different behaviors of the queue and the stack will help define the behavior of the two search algorithms in this article.



Breadth-first search   : Queue

recall : frontier nodes are nodes that need to be searched next


Storing the frontier nodes in a queue creates the level-by-level pattern of a breadth-first search. Child nodes are searched in the order 
they are added to the frontier. The nodes on the next level are always behind the nodes on the current level. Breadth-first search is known 
as a complete algorithm since no matter how deep the goal is in the tree it will always be located.


Depth-first search

Frontier nodes stored in a stack create the deep dive of a depth-first search. Nodes added to the frontier early on can expect to remain in the 
stack while their sibling’s children (and their children, and so on) are searched. Depth-first search is not considered a complete algorithm 
since searching an infinite branch in a tree can go on forever. In this situation, an entire section of the tree would be left un-inspected.



Path to the goal

It is important to note that it is not enough to find the node with the correct value. Once the goal node is found using either method of tree traversal, 
you must be able to provide the path of nodes from the root node to the goal node. This can be done in many ways from saving paths as you search down the 
tree to working with trees that can supply the path when needed.

The location of the goal node has a significant impact on determining which search algorithm will be able to find the goal first. That is why these approaches 
are generally used as building blocks for more complex traversal algorithms. With more information on the location of the goal value in the tree, 
you can optimize the breadth-first search and depth-first search algorithms. Then they become powerful tools that can help you find that file you were looking for.
Wrap up

Nice job reaching the end of this article. Let’s recap what we learned:

    Breadth-first search is a tree traversal algorithm that explores nodes level by level. Using a queue to store frontier nodes supports the behavior of this search.

    Depth-first search is another tree traversal algorithm that goes deep into a tree exploring for nodes branch by branch. Using a stack 
    to store frontier nodes supports the behavior of this search.

"""


"""
breadth first search conceptual

Breadth-First Search: Conceptual

Learn how the breadth-first search tree traversal algorithm works using an iterative approach and frontier queue.

The breadth-first search is a tree traversal algorithm that follows a level-by-level search pattern, starting with the root node on top and moving to each level in search of a goal node. As nodes of a tree are searched, their children are added to a queue known as the frontier. This queue follows the first-in-first-out rule known as FIFO where the first nodes added to the queue will be the first to leave and be searched.

In this article, we will explore the breadth-first search algorithm using an iterative approach.
Level-By-Level Search

The level-by-level pattern followed by the breadth-first search can feel very approachable since it is just like searching for a specific word in a book or even this article. Every word is checked line by line with no word or line skipped. Similarly, the breadth-first search iteratively checks child nodes in the order they are placed in a queue.
Breadth-First Search Algorithm

The following flow chart represents an iterative breadth-first search algorithm that either locates a goal node based on a given goal value or returns a failure state.

Breadth-first search iterative algorithm

Let’s go over the steps for implementing this algorithm:

    The search starts with two values, a root node for the tree and the goal value we are searching for.
    Our first search step is to add the root node to the end of our node queue. The queue represents the search’s frontier.
    While the node queue contains at least one value, we retrieve the next node from the frontier and check its value against the goal value.
    If the two values match, the current node is returned. If they don’t match, the search continues by adding the current node’s children to the frontier.

The search goes level by level in search of the value because the children on the next tree level added to the queue will be in line behind nodes on the current level.
Multiple choice
Questions

Given the following tree and what you know about the search pattern of the breadth-first search, what are the remaining contents of the frontier queue after the node with the value 4 is popped?
Code

       1
      / \
     2   3
    / \ / \
   4  5 6  7

Answer Choices
Tracking the Path to the Goal Node

Now that we covered how to locate the goal node in a tree we must now look at how to find the path to the goal node from the root node. To do this with the iterative algorithm, a few extra steps need to be added. These steps will keep track of every frontier node’s path from the root node.

Frontier queue is path queue and holds list types

The flow chart above shows the extra steps needed to initialize the frontier:

    Define an initial path with the root node inside a list data type.
    Push the initial path onto the frontier queue.

Addition of current path variable

The above flowchart shows how to retrieve the current node:

    Pop the current path off the frontier.
    Retrieve the current node from the end of the current path.

New path for each child node

To add children to the frontier the above flowchart shows that for each child:

    Define a new path from a copy of the current path.
    Add the child node to the end of the new path.
    Push the new path onto the frontier queue.

Given a root node with two children, the end of the first search iteration will have two lists in the frontier queue:

    a list with the root node and one child as elements
    a list with the root node and the other child as elements

The frontier queue holds a path list for each frontier node with the root node as the first element. When the goal node is found, the current path is returned.
Multiple choice
Questions

During a breadth-first search of the following tree, the node with the value 2 is searched and the paths to its children need to be added to the frontier queue.

Given what you know about the search pattern of the breadth-first search, what two path lists will be added to the frontier queue?
Code

    1
   / \
  2   3
 / \ / \
4  5 6  7

Answer Choices
Conclusion

Given a basic tree structure with each node only containing a value and a list of children, it is possible to traverse the tree using a breadth-first search while returning a path to the goal node. The iterative approach is made easy when using the natural behaviors of a queue that pops values out in the same order they were pushed in. While there are other ways to implement this search using different tree structures and recursion, the iterative approach follows a clear pattern that is a great way to understand tree traversal.

Great work with the contents of this article. To recap:

    Breadth-first search is a tree traversal algorithm that explores nodes level-by-level.
    The search can be implemented using an iterative approach.
    In a breadth-first search, a queue is used to store frontier nodes.
    It is necessary to return a path of nodes from the root node to the goal node.
"""