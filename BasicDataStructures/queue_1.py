"""
Queues: Conceptual

A conceptual overview of Queues.
Introduction

A queue is a data structure which contains an ordered set of data.

Queues provide three methods for interaction:

    Enqueue - adds data to the “back” or end of the queue
    Dequeue - provides and removes data from the “front” or beginning of the queue
    Peek - reveals data from the “front” of the queue without removing it

This data structure mimics a physical queue of objects like a line of people buying movie tickets. Each person has a name (the data). 
The first person to enqueue, or get into line, is both at the front and back of the line. As each new person enqueues, 
they become the new back of the line.

The first person in the queue is the first to be served. Queues are a First In, First Out or FIFO structure.

Implementation

Queues can be implemented using a linked list as the underlying data structure. 
The front of the queue is equivalent to the head node of a linked list and the back of the queue is equivalent to the tail node.
Since operations are only allowed to affect the front or back of the queue, any traversal or modification to other nodes within the linked list is disallowed. 
Since both ends of the queue must be accessible, a reference to both the head node and the tail node must be maintained.

One last constraint that may be placed on a queue is its length. If a queue has a limit on the amount of data that can be placed into it, it is considered a bounded queue.

Similar to stacks, attempting to enqueue data onto an already full queue will result in a queue overflow. If you attempt to dequeue data from an empty queue, 
it will result in a queue underflow.
Review

Let’s take a minute to review what we’ve covered about queues in this lesson.

Queues:

    Contain data nodes
    Support three main operations:
    Enqueue adds data to the back of the queue
    Dequeue removes and provides data from the front of the queue
    Peek provides data on the front of the queue
    Can be implemented using a linked list or array
    Bounded queues have a limited size.
    Enqueueing onto a full queue causes a queue overflow
    Queues process data First In, First Out (FIFO)

Queues Python Introduction
6 min

As previously mentioned, a queue is a data structure that contains an ordered set of data that follows a FIFO (first in, first out)
Preview: Docs A protocol describes the rules, syntax, and semantics used by two or more devices in a computer network to connect and communicate with each other.
protocol
. You can visualize it as a line at a deli:

    The customer at the front of the line (equivalent to the head in a queue) is the first customer to get served
    Any new customer must go to the back of the line (the tail of the queue) and wait until everyone in front of them has been served 
    (no line cutters allowed in this deli!)
    The deli
    Preview: Docs A server is a hardware or software device used to provide resources to clients or requesting applications. Servers 
    run on an architecture for fulfilling requests called the "Client-Server Model", which works by the client asking the server for 
    specific data in an agreed upon format and the server readying and providing the data.
    server
    only needs to know about the current order

Now, we can use Python to build out a Queue class with those three essential queue methods:

    enqueue() which will allow us to add a new node to the tail of the queue
    dequeue() which will allow us to remove a node from the head of the queue and return its value
    peek() which will allow us to view the value of head of the queue without returning it

    

Queues Python Size
16 min

Bounded queues require limits on the number of nodes that can be contained, while other queues don’t. 
To account for this, we will need to make some modifications to our Queue class so that we can keep track of and limit size where needed.

We’ll be adding two new properties to help us out here:

    A size property to keep track of the queue’s current size
    A max_size property that bounded queues can utilize to limit the total node count

In addition, we will add three new methods:

    get_size() will return the value of the size property
    has_space() will return True if the queue has space for another node
    is_empty() will return true if the size is 0

    
Queues Python Enqueue
15 min

“Enqueue” is a fancy way of saying “add to a queue,” and that is exactly what we’re doing with the enqueue()
Preview: Docs Loading link description
method
.

There are three scenarios that we are concerned with when adding a node to the queue:

    The queue is empty, so the node we’re adding is both the head and tail of the queue
    The queue has at least one other node, so the added node becomes the new tail
    The queue is full, so the node will not get added because we don’t want queue “overflow”

Let’s put this into action by building out an enqueue() method for Queue.


Queues Python Enqueue
15 min

“Enqueue” is a fancy way of saying “add to a queue,” and that is exactly what we’re doing with the enqueue()
Preview: Docs A method is a small piece of code, usually defined in a class, that can be used outside the class and in other parts of the program.
method
.

There are three scenarios that we are concerned with when adding a node to the queue:

    The queue is empty, so the node we’re adding is both the head and tail of the queue
    The queue has at least one other node, so the added node becomes the new tail
    The queue is full, so the node will not get added because we don’t want queue “overflow”

Let’s put this into action by building out an enqueue() method for Queue.


Queues Python Dequeue
14 min

We can add items to the tail of our queue, but we remove them from the head using a
Preview: Docs Loading link description
method
known as dequeue(), which is another way to say “remove from a queue”. Like enqueue(), we care about the size of the queue — 
but in the other direction, so that we prevent queue “underflow”. After all, you don’t want to remove something that isn’t there!

As with peek(), our dequeue() method should return the value of the head. Unlike, peek(), dequeue() will also remove the current 
head and replace it with the following node.

For dequeue, there are three scenarios that we will take into account:

    The queue is empty, so we cannot remove or return any nodes lest we run into queue “underflow”
    The queue has one node, so when we remove it, the queue will be empty and we need to reset the queue’s head and tail to None
    The queue has more than one node, and we just remove the head node and reset the head to the following node



Queues Python Review
2 min

Congrats! You have just implemented a queue data structure in Python by creating a Queue class that:

    follows FIFO
    Preview: Docs A protocol describes the rules, syntax, and semantics used by two or more devices in a computer network to connect and communicate with each other.
    protocol
    with enqueue(), dequeue(), and peek() methods
    gives you the option of creating bounded queues with a max_size
    prevents queue “overflow” and “underflow” by keeping track of size



"""



class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value
  

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
         
  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print(str(item_to_remove.get_value()) + " is served!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The queue is totally empty!")
  
  def peek(self):
    if self.size > 0:
      return self.head.get_value()
    else:
      print("No orders waiting!")
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0

print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #
# Uncomment the line below:
deli_line.dequeue()
# ------------------------ #