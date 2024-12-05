"""
Finding the Maximum Value in a Linked List
17 min

Now that we can analyze the
Preview: Docs Loading link description
runtime
of a function, let’s take a look at the runtime of
Preview: Docs Systems for organizing data that dictate how items relate to one another, 
are accessed, and modified.
data structures
.

We often search through data structures to find a specific value. In this exercise, you will write a 
function to find the maximum value of a linked list and you will also analyze the runtime of your 
function.

The function, find_max, takes in linked_list as an input. The function should return the maximum value 
in the linked list.
"""

from linkedlist import LinkedList

#Fill in Function
def find_max(linked_list):
  print("--------------------------")
  print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))
  #Write Code Here
  
  current_node = linked_list.get_head_node()
  max_value = current_node.get_value()
  while current_node:
    if current_node.get_value() > max_value:
      max_value = current_node.get_value()
    current_node = current_node.get_next_node()
  return max_value
  
  
  
  

#Test Cases
ll = LinkedList(6)
ll.insert_beginning(32)
ll.insert_beginning(-12)
ll.insert_beginning(48)
ll.insert_beginning(2)
ll.insert_beginning(1)
print("The maximum value in this linked list is {0}\n".format(find_max(ll)))

ll_2 = LinkedList(60)
ll_2.insert_beginning(12)
ll_2.insert_beginning(22)
ll_2.insert_beginning(-10)
print("The maximum value in this linked list is {0}\n".format(find_max(ll_2)))

ll_3 = LinkedList("A")
ll_3.insert_beginning("X")
ll_3.insert_beginning("V")
ll_3.insert_beginning("L")
ll_3.insert_beginning("D")
ll_3.insert_beginning("Q")
print("The maximum value in this linked list is {0}\n".format(find_max(ll_3)))

#Runtime
runtime = "N"
print("The runtime of find_max is O({0})".format(runtime))