"""
Doubly Linked Lists

A conceptual overview of Doubly Linked Lists.

Like a singly linked list, a doubly linked list is comprised of a series of nodes. Each node contains data and two links (or pointers) to the next and previous nodes 
in the list. The head node is the node at the beginning of the list, and the tail node is the node at the end of the list. The head node’s previous pointer is set 
to null and the tail node’s next pointer is set to null.

Think of your daily commute on the subway as a real-world example of a doubly linked list. Your home is the head of the list, your place of work is the tail, 
and every stop in between is another node in the list.

Doubly linked list example
Adding to the list

In a doubly linked list, adding to the list is a little complicated as we have to keep track of and set the node’s previous pointer as well as update the tail of 
the list if necessary.

Adding to the head

When adding to the head of the doubly linked list, we first need to check if there is a current head to the list. If there isn’t, then the list is empty, and we can 
simply make our new node both the head and tail of the list and set both pointers to null. If the list is not empty, then we will:

    Set the current head’s previous pointer to our new head.
    Set the new head’s next pointer to the current head.
    Set the new head’s previous pointer to null.

Adding to the tail

Similarly, there are two cases when adding a node to the tail of a doubly linked list. If the list is empty, then we make the new node the head and tail of the 
list and set the pointers to null. If the list is not empty, then we:

    Set the current tail’s next pointer to the new tail
    Set the new tail’s previous pointer to the current tail
    Set the new tail’s next pointer to null

Adding to the head and tail of the list

Removing from the list

Due to the extra pointer and tail property, removing the head from a doubly linked list is slightly more complicated than removing the head from a singly linked list. 
However, the previous pointer and tail property make it much simpler to remove the tail of the list, as we don’t have to traverse the entire list to be able to do it.

Removing the head

Removing the head involves updating the pointer at the beginning of the list. We will set the previous pointer of the new head 
(the element directly after the current head) to null, and update the head property of the list. If the head was also the tail, 
the tail removal process will occur as well.
Removing the tail

Similarly, removing the tail involves updating the pointer at the end of the list. We will set the next pointer of the new tail (the element directly 
before the tail) to null, and update the tail property of the list. If the tail was also the head, the head removal process will occur as well.


Removing from the middle of the list

It is also possible to remove a node from the middle of the list. Since that node is neither the head nor the tail of the list, 
there are two pointers that must be updated:

    We must set the removed node’s preceding node’s next pointer to its following node.
    We must set the removed node’s following node’s previous pointer to its preceding node.

There is no need to change the pointers of the removed node, as updating the pointers of its neighboring nodes will remove it from the list. 
If no nodes in the list are pointing to it, the node is orphaned.


summary
Let’s take a minute to review what we’ve covered about doubly linked lists in this lesson:

    They are comprised of nodes that contain links to the next and previous nodes.
    They are bidirectional, meaning it can be traversed in both directions.
    They have a pointer to a single head node, which serves as the first node in the list.
    They have a pointer to a single tail node, which serves as the last node in the list.
    They require the pointers at the head of the list to be updated after addition to or removal of the head.
    They require the pointers at the tail of the list to be updated after addition to or removed of the tail.
    They require the pointers of the surrounding nodes to be updated after removal from the middle of the list.

"""



"""
Node Class and Constructor
7 min

Now that we’ve learned about doubly linked lists, let’s implement one in Python.

As a reminder, a doubly linked list is a sequential chain of nodes, just like a singly linked list. The nodes we used for our singly linked lists contained two elements:

    A value
    A link to the next node

The difference between a doubly linked list and a singly linked list is that in a doubly linked list, the nodes have pointers to the previous node as 
well as the next node. This means that the doubly linked list data structure has a tail property in addition to a head property, which allows for 
traversal in both directions.

So the nodes we will use for our doubly linked list contain three elements:

    A value
    A pointer to the previous node
    A pointer to the next node

Depending on the end-use of the doubly linked list, there are a variety of methods that we can define.

For our use, we want to be able to:

    Add a new node to the head (beginning) of the list
    Add a new node to the tail (end) of the list
    Remove a node from the head of the list
    Remove a node from the tail of the list
    Find and remove a specific node by its value
    Print out the nodes in the list in order from head to tail

To start, we are going to look at the updated Node class and create the constructor.

Ready? Let’s go!

Note: We will reuse the .stringify_list()
Preview: Docs A method is a small piece of code, usually defined in a class, that can be used outside the class and in other parts of the program.
method
from our LinkedList class, but we’re going to create the rest of the methods ourselves.
"""
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value


class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail

  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()

  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()

  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break

      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None

    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)

    return node_to_remove

  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

# Create your subway line here:

subway = DoublyLinkedList()
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")
print(subway.stringify_list())

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")
print(subway.stringify_list())

subway.remove_head()
subway.remove_tail()
subway.remove_by_value("Times Square")
print(subway.stringify_list())