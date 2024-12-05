"""
Two pointer linked list techniques 

this we shall learn how to approach linked list problems with multiple iterator pointers 
Many common  singly linked list problems can be solved by iterating with two pointers. this is 
sometimes known as runner technique 

Two pointers moving in parallel

Two Pointers Moving in Parallel

Consider the following problem:

Create a method that returns the nth last element of a singly linked list.

For example: given a linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5, return the 2nd to last element. 
The answer would be element 4.

In order to do this, you’ll need some way of knowing how far you are from the end of the list itself. However, in a singly linked list, 
there’s no easy way to iterate back through the list when you find the end.

Approaches

One thing that might first come to mind is to use a list to store a representation of the linked list, and then to obtain the nth to 
last element from this list. While this approach results in an easy-to-read implementation, it could also use up lots of memory 
maintaining a dual representation of the same data. If the linked list has one million nodes, we’ll need one million pointers in a 
list to keep track of it! An approach like this results in an extra O(n) space being allocated.

The code for this approach would look like the following:


"""
# this one has 0(n) space and 0(n)time 
def list_nth_last(linked_list, n):
  linked_list_as_list = []
  current_node = linked_list.head_node
  while current_node:
    linked_list_as_list.append(current_node)
    current_node = current_node.get_next_node()
  return linked_list_as_list[len(linked_list_as_list) - n]


"""
Instead of creating an entire parallel list, we can solve this problem by using two pointers at different positions in the list but moving at the same rate. 
As in the previous example, we will use one pointer to iterate through the entire list, but we’ll also move a second pointer delayed n steps behind the first one.
A count variable can keep track of the position of the current element in the linked list that the tail pointer is pointing to, which is initially set to 
1 which is the first element’s position."""


#0(n) time and constant space 0(1)
def nth_last_node(linked_list, n):
  current = None
  tail_seeker = linked_list.head_node
  count = 1
  while tail_seeker:
    tail_seeker = tail_seeker.get_next_node()
    count += 1
    if count >= n + 1:
      if current is None:
        current = linked_list.head_node
      else:
        current = current.get_next_node()
  return current


"""
Pointers at Different Speeds

Using two pointers moving in parallel was a good solution to the previous problem. However, there are other problems where having two 
pointers moving in parallel wouldn’t be as useful. Let’s take a look at one of those problems and consider a new strategy that uses two 
pointers moving at different speeds.

Consider the following problem:

Create a method that returns the middle node of a linked list.

For example, given the linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7, the middle node would be the element with value 4.

Approaches

As before, it’s possible to find a solution by iterating through the entire list, creating a list representation, and then returning the middle index. 
But, also as before, this can potentially take up lots of extra space:

create list
while the linked list has not been fully iterated through
  push the current element onto list
  move forward one node
return list[length / 2]

Instead, we can use two pointers to move through the linked list. The first pointer takes two steps through the linked list for every one step that the second 
takes, so it iterates twice as fast:

fast pointer = linked list head
slow pointer = linked list head
while fast pointer is not None
  move fast pointer forward
  if the end of the linked list has not been reached
    move fast pointer forward
    move slow pointer forward
return slow pointer

When the first pointer reaches the end of the list, the “slower” second pointer will be pointing to the middle element. Let’s visualize the steps of the algorithm:

Starting State

F
S
1  2  3  4  5  6  7

First Tick

      F
   S
1  2  3  4  5  6  7

Second Tick

            F
      S
1  2  3  4  5  6  7

Third Tick

                  F
         S
1  2  3  4  5  6  7

Final Tick

                     F
         S
1  2  3  4  5  6  7  None

As long as we always move the fast pointer first and check to see that it is not None before moving it and the slow pointer again, we’ll exit iteration at 
the proper time and have a reference to the middle node with the slow pointer.

implementation 
Complete the find_middle() function and return the middle node of linked_list. You can assume that the linked list has no cycles.

Return the right-weighted middle for even-length linked lists. For example, in a linked list of 4 elements it should return the element at the third position.

Use generate_test_linked_list(length) to generate linked lists with values from 1 -> 2 -> .. -> length to test out your function. For instance, 
    generate_test_linked_list(4) results in 1 -> 2 -> 3 -> 4.

"""
# has o(n) time and constant space 
def find_middle(linked_list):
  fast = linked_list.head_node
  slow = linked_list.head_node
  while fast:
    fast = fast.get_next_node()
    if fast:
      fast = fast.get_next_node()
      slow = slow.get_next_node()
  return slow


"""
Half-Speed

Another equally valid solution is to move the fast pointer once with each loop 
iteration but only move the slow pointer every-other iteration:"""

def find_middle_alt(linked_list):
  count = 0
  fast = linked_list.head_node
  slow = linked_list.head_node
  while fast:
    fast = fast.get_next_node()
    if count % 2 != 0:
      slow = slow.get_next_node()
    count += 1
  return slow