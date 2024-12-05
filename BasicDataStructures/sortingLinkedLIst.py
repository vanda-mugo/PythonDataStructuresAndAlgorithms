"""
Sort a Linked List
18 min

We also often sort
Preview: Docs Loading link description
data structures
in order to organize the values stored in them. In this exercise, you will sort a linked list 
from smallest value to largest value.

To sort a linked list, we can do the following:

    Instantiate a new linked list
    Find the maximum value of our inputted linked list
    Insert the maximum to the beginning of the new linked list
    Remove the maximum value from the inputted linked list
    Repeat steps 2-4 until the head node of the inputted linked list points to None
    Return the new linked list

"""

from linkedlist import LinkedList

def find_max(linked_list):
  current = linked_list.get_head_node()
  maximum = current.get_value()
  while current.get_next_node():
    current = current.get_next_node()
    val = current.get_value()
    if val > maximum:
      maximum = val
  return maximum

#Fill in Function
def sort_linked_list(linked_list):
  print("\n---------------------------")
  print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
  new_linked_list = LinkedList()
  #Write Code Here!
  while linked_list.get_head_node():
    max_value = find_max(linked_list)
    new_linked_list.insert_beginning(max_value)
    linked_list.remove_node(max_value)

  return new_linked_list

  

#Test Cases
ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_3).stringify_list()))

#Runtime
runtime = "N^2"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))