"""
Stacks 

Introduction 
this is a data structure that contains an ordered set of data
they have 3 methods for interaction 

Push : Adds data to the 'top' of the stack 

pop : removes data from the 'top' of the stack

peek : returns data from the top of teh stack without removing it 

Stacks mimic a physical “stack” of objects. Consider a set of gym weights:

Each plate has a weight (the data). The first plate you add, or push, onto the floor is both the bottom and top of the stack. 
Each weight added becomes the new top of the stack.

At any point, the only weight you can remove, or pop, from the stack is the top one. You can peek and read the top weight without removing it from the stack.

The last plate that you put down becomes the first, and only, one that you can access. This is a Last In, First Out or LIFO structure. 
A less frequently used term is First In, Last Out, or FILO.


Implementation

Stacks can be implemented using a linked list as the underlying data structure because it’s more efficient than a list or array. 
Depending on the implementation, the top of the stack is equivalent to the head node of a linked list and the bottom of the 
stack is equivalent to the tail node.

A constraint that may be placed on a stack is its size. This is done to limit and quantify the resources the data structure 
will take up when it is “full.”

Attempting to push data onto an already full stack will result in a stack overflow. Similarly, if you attempt to pop data from an empty stack, 
it will result in a stack underflow.

Review

Let’s take a minute to review what we’ve covered about stacks in this lesson.

Stacks:

    Contain data nodes
    Support three main operations
        Push adds data to the top of the stack
        Pop removes and provides data from the top of the stack
        Peek reveals data on the top of the stack
    Implementations include a linked list or array
    Can have a limited size
    Pushing data onto a full stack results in a stack overflow
    Stacks process data Last In, First Out (LIFO)


Stacks Python Introduction
4 min

You have an understanding of how stacks work in theory, so now let’s see how they can be useful out in the wild — with Python!

Remember that there are three main methods that we want our stacks to have:

    Push - adds data to the “top” of the stack
    Pop - provides and removes data from the “top” of the stack
    Peek - provides data from the “top” of the stack without removing it

We also need to consider the stack’s size and tweak our methods a bit so that our stack does not “overflow”.

Let’s get started building out our Stack class.



Stacks Python Push and Pop
8 min

The stack’s push() and pop() methods are our tools to add and remove items from it. pop() additionally returns the value of the item it is removing. 
Keep in mind that we can only make modifications to the top of the stack.

Stacks Python Size I
8 min

With stacks, size matters. If we’re not careful, we can accidentally over-fill them with data. Since we don’t want any stack overflow, 
we need to go back and make a few modifications to our methods that help us track and limit the stack size so we can keep our stacks healthy.

What do we do if someone tries to peek() or pop() when our stack is empty?

How do we keep someone from push()ing to a stack that has already reached its limit?

How do we even know how large our stack has gotten?

Stacks Python Size II
8 min

It’s time to add a couple helper methods.

Helper methods simplify the code we’ve written by abstracting and labeling chunks of code into a new function. Here’s an example:

# Adding "!" without a helper
saying = "I love helper methods"
exclamation = saying + "!"

# Adding "!" with a helper
def add_exclamation_to_string(str):
  return str + "!"

exclamation2 = add_exclamation_to_string("I love helper methods")

This might seem like a silly example, but think about the benefit of the add_exclamation_to_string() helper.

    The name tells us what this function does. Without a helper, we’d need to read the code to understand its meaning.
    The function lets us repeat this behavior. Without a helper, we’d need to keep rewriting the same code!

First, we want one that checks if our stack has room for more items. We can use this in .push() to guard against pushing items to our stack when it’s full.

Second, it’s helpful to have a
Preview: Docs Loading link description
method
that checks if the stack is empty…

Stacks Python Review
1 min

Nice work — you’ve built out a Stack class that can:

    add a new item to the top via a push() method
    remove an item from the top and returns its value with a pop() method
    return the value of the top item using a peek() method
    allows a stack instance to maintain an awareness of its size to prevent stack “overflow”

So how does your code stack up against pizza delivery?


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



class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()