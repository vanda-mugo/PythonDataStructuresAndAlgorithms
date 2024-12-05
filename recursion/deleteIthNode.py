
"""
Delete i-th node from a linked list

Now that Alex’s gallery display is organized in the correct order, we can use a linked list to represent 
the series of gemstones. The linked list class has been implemented for you behind the scene.

A friend asks Alex if she could buy a gemstone from his gallery. Alex agrees to remove any gemstone and 
sell it to her. How can he delete the i-th node from the linked list recursively?

    First, address the edge case where i is negative. If i is negative, return the current node.
    There are two base cases that we need to consider:
        If the current node is None (meaning it doesn’t exist), we can just return None.
        If i is equivalent to 0, then we need to delete the current node by “skipping” it and returning 
        the pointer to the next node instead.
    The recursive step involves assigning the next node to the recursive call with the first arguments 
    being the next node and the second argument being i-1.
    Return the current node.

Coding question
Questions

Define a function called remove_node() that takes in the following parameters:

    head - a node that acts as the head of a linked list
    i - an integer

The function should remove the ith node of the linked list (index from 0) and return the modified head.

Example:

    Input: remove_node(head = "Amber"->"Sapphire"->"Jade"->"Pearl", 1)
    Output: head = "Amber"->"Jade"->"Pearl"

The LinkedList class has been implemented for you. You do not need to modify it.

We take care of the edge case where i <= 0 because it’s impossible to remove a node of negative index. 
It’s good practice to address edge cases like this in your program to ensure it always functions as 
intended.

We then define the two base cases:

    The first base case involves checking if head is None. If this is True, we know that we have 
    reached the end of the linked list so we simply return a None object.
    The second base case involves checking if i == 0 and removing head from the linked list. 
    The simplest way to remove head is by skipping over it and returning head.next_node instead.

In order to iterate the linked list, we assign head.next_node to the recursive call. remove_node() 
is recursively called with arguments head.next_node and i - 1, which moves the input closer to the 
first and second base cases simultaneously.

The last step is to return head. After all recursive calls on the call stack resolve, head will be 
the first node of the linked list with the ith node removed.
"""





from LinkedLIst import LinkedList

# Definition for singly-linked list node.
# class ListNode:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

def remove_node(head, i):
    if i < 0:
        return head
    if head is None:
        return None
    if i == 0:
        return head.next_node

    head.next_node = remove_node(head.next_node, i - 1)
    return head


# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())
