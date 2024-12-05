"""
linked lists and doubly linked lists 

Nodes 
an individual node contains data and a link to another node. each of the data structures adds additional
constraints or behaviour to these features to create the desired structure 
such data structures include :

linked lists
stacks
queues
trees

Node implementation 

the data contained within a node can be a variety of types 
the links within a node are sometimes referred to as pointers. this is because they point to 
another node 

data structures implement nodes with one or more links, if these links are null, it denotes that you have reached the end 
of the particular node or link path you were previously following 




"""

# implementation of a node structure 
class Node:
  def __init__(self, value, link_node=None):
       self.value = value
       self.link_node = link_node

  def get_value(self):
   return self.value
  
  def get_link_node(self):
   return self.link_node
  
  def set_link_node(self, link_node):
   self.link_node = link_node

  def set_value(self, value):
   self.value = value

  def increment_value(self):
    self.value = self.value + 1




"""
linked lists : conceptual 

a link list is comprised of a number of nodes . the head node is the node at the beginning of the list , each node 
contains data and a link(pointer) to the next node in the list. the link is terminated when a nodes link is null
the last node is called a tail node 


Common operations on a linked list may include:

    adding nodes
    removing nodes
    finding a node
    traversing (or traveling through) the linked list

    
    Adding to and Removing from the Linked List

With linked lists, because nodes are linked to from only one other node, you can’t just go adding and removing nodes willy-nilly without doing a bit of maintenance.


Adding a New Node

Adding a new node to the beginning of the list requires you to link your new node to the current head node. This way, you maintain your connection with 
the following nodes in the list.


Removing a Node

If you accidentally remove the single link to a node, that node’s data and any following nodes could be lost to your application, leaving you with orphaned nodes.

To properly maintain the list when removing a node from the middle of a linked list, you need to be sure to adjust the link on the previous node so that it 
points to the following node.

Depending on the language, nodes that are not referenced are removed automatically. “Removing” a node is equivalent to removing all references to the node.

summary

Linked Lists:

    Are comprised of nodes
    The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
    Can be unidirectional or bidirectional
    Are a basic data structure, and form the basis for many other data structures
    Have a single head node, which serves as the first node in the list
    Require some maintenance in order to add or remove nodes
    The methods we used are an example and depend on the exact use case and/or programming language being used

"""

# linked lists are implemented by nodes 
"""
With the Node in hand, we can start building the actual linked list. Depending on the end-use of the linked list, a variety of methods can be defined.

For our use, we want to be able to:

    get the head node of the list (it’s like peeking at the first item in line)
    add a new node to the beginning of the list
    print out the list values in order
    remove a node that has a particular value
"""


class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node 

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node 

  def set_next_node(self,next_node):
    self.next_node = next_node


my_node = Node(44)

print(my_node.get_value())


# Create your LinkedList class below:
# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node != None:
        if current_node.get_next_node().get_value() == value_to_remove:
          next_node = current_node.get_next_node()
          current_node.set_next_node(next_node.get_next_node())
        else:
          current_node = current_node.get_next_node()  
  
  """
  The final use case we mentioned was the ability to remove an arbitrary node with a particular value. This is slightly more complex, 
  since a couple of special cases need to be handled.

Consider the following list:

a -> b -> c

If node b is removed from the list, the new list should be:

a -> c

We need to update the link within the a node to match what b was pointing to prior to removing it from the linked list.

Lucky for us, in Python, nodes which are not referenced will be removed for us automatically. If we take care of the references, 
b will be “removed” for us in a process called Garbage Collection. Remember having to do this in c++

For the purposes of this lesson, we’ll create a function that removes the first node that contains a particular value. However, 
you could also build this function to remove nodes by index or remove all nodes that contain a particular value."""
  # Define your remove_node method below:

  


"""
Swapping elements in linked lists 
Learn how to swap two nodes in a singly linked list in Python.

Since singly linked lists only have pointers from each node to its next node, swapping two nodes in the list isn’t as easy as doing so in an array 
(where you have access to the indices). You not only have to find the elements, but also reset their surrounding pointers to maintain the integrity of the list. 
This means keeping track of the two nodes to be swapped as well as the nodes preceding them.

Given a linked list and the elements to be swapped (val1 and val2), we need to keep track of four values:

    node1: the node that matches val1
    node1_prev: node1‘s previous node
    node2: the node that matches val2
    node2_prev: node2‘s previous node

Given an input of a linked list, val1, and val2, the general steps for doing so is as follows:

    Iterate through the list looking for the node that matches val1 to be swapped (node1), keeping track of the node’s previous node as you iterate (node1_prev)
    Repeat step 1 looking for the node that matches val2 (giving you node2 and node2_prev)
    If node1_prev is None, node1 was the head of the list, so set the list’s head to node2
    Otherwise, set node1_prev‘s next node to node2
    If node2_prev is None, set the list’s head to node1
    Otherwise, set node2_prev‘s next node to node1
    Set node1‘s next node to node2‘s next node
    Set node2‘s next node to node1‘s next node


"""


def swap_nodes(input_list, val1, val2):
    if val1 == val2:
        print("Elements are the same - no swap needed")
        return
    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev = None
    node2_prev = None

    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()
        #at this point we have found the nodes related with node 1 ]
        # that is node_1 and node_1_previous that match with the value we were looking for 

    while node2 != None:
        if node2.get_value() == val2:
            # we have found the value we were looking for 
            break 
        node2_prev = node2
        node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
        print("Swap not possible - one or more element is not in the list")
        return

    if node1_prev == None:
      input_list.head_node = node2
    else:
      # not equal to none
      node1_prev.set_next_node(node2)

    if node2_prev == None:
      input_list.head_node = node1
    else:
      node2_prev.set_next_node(node1)

    
    temp = node1.get_next_node()
    # note by that in this case node 1 has already been switched with node 2
    # so what follows node1 is what used to follow node2 since we only dealt with the 
    # previous nodes 
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)

    


        
