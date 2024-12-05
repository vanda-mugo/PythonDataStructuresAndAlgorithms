"""
Introduction to Max-Heaps
3 min

We’re going to implement a max-heap in Python. Max-heaps efficiently keep track of the maximum value in a dataset, even as we add and remove elements.

Max-heaps are nearly identical to a min-heap; however, min-heaps keep track of the minimum value in a data set. We’ll be focusing on max-heaps in this lesson, 
but much of what we cover in this lesson can be applied to a min-heap as well.

Heaps enable solutions for complex problems such as finding the shortest path (Dijkstra’s Algorithm) or efficiently sorting a dataset (heapsort).

They’re an essential tool for confidently navigating some of the difficult questions posed in a technical interview.

By understanding the operations of a heap, you will have made a valuable addition to your problem-solving toolkit.





Max-Heaps: Python
Defining Max-Heap
5 min

Our MaxHeap class will store two pieces of information in the form of instance attributes:

    A Python list of the elements within the heap.
    A count of the elements within the heap.

To make our lives easier, we’ll always keep one sentinel element at the beginning inside the list: None.

heap = MaxHeap()
print(heap.heap_list)
# [None]
print(heap.count)
# 0

A sentinel value will terminate a loop when read as input. This sentinel element of None will save us the trouble of checking whether the list is 
empty and simplify the methods we define in later lessons.





Adding an Element: Heapify Up I
7 min

Our MaxHeap class isn’t very useful if all it ever contains is None. Let’s build the functionality to add elements to our max-heap.

Our MaxHeap must abide by two principles:

    The element at
    Preview: Docs Improves the speed of data retrieval in the database.
    index
    1 is the maximum value in the entire list.
    Every “child” element in the list must be smaller than their “parent”.

The first element we add to the list will automatically be the maximum value since there are no other elements in our heap. We’ll 
tackle the trickier aspects of maintaining these principles in the coming exercises

For now, lets define two class instance methods called .add() and .heapify_up():

    .add() will handle adding an element to the heap via the .heap_list property.
    .heapify_up() will do the work of maintaining the heap properties as we add additional elements.

    



Max-Heaps: Python
Translating Parent and Child Elements Into Indices
8 min

Great work so far! Our MaxHeap adds elements to heap_list, keeps count of the number elements inside the heap, and has the beginnings of .heapify_up().

Before we dive into the logic for .heapify_up(), let’s review how heaps track elements. We use a list for storing internal elements, but we’re modeling it on a
Preview: Docs Loading link description
binary
tree, where every “parent” element has up to two “child” elements.

“child” and “parent” elements are determined by their relative indices within the internal list. By doing some arithmetic on an element’s
Preview: Docs Loading link description
index
, we can determine the indices for parent and child elements (if they exist).

    Parent: index // 2
    Left Child: index * 2
    Right Child: (index * 2) + 1

print(heap.heap_list)
# Outputs: [None, 99, 22, 61, 10, 21, 13, 23]
# Indices: [0, 1, 2, 3, 4, 5, 6, 7]

heap.parent_idx(4)
# (4 // 2) == 2
# Element at index 4 is 10 
# Element at index 2 is 22
# The parent element of 10 is 22

heap.left_child(3)
# (3 * 2) == 6
# Element at index 3 is 61
# Element at index 6 is 13
# The left child element of 61 is 13

These calculations are important for the efficiency of the heap, but they’re not necessary to memorize, so we’ve added three helper methods: .parent_idx(), .
left_child_idx(), and .right_child_idx().

These helpers take an index as the
Preview: Docs An argument is the actual value of a variable passed into a function.
argument
and return the corresponding parent or child index.




Max-Heaps: Python
Adding an Element: Heapify Up II
16 min

Now that we understand how to determine the relationship of elements with the internal list, we’re ready to finish .heapify_up().

We need to make sure that every child is smaller in value than their parent. Say we add an element to the following heap:

print(heap.heap_list)
# Output: [None, 99, 22, 61, 10, 21, 13, 23]
heap.add(90)

# ( new_element )
# { parent_element }
# [None, 99, 22, 61, {10}, 21, 13, 23, (90)]

Oh no! We’ve violated the heap property: since 90‘s parent is 10, the parent element is smaller than the child.

Don’t fret; we can fix this. We’ll exchange the parent and the child elements.

# [None, 99, 22, 61, {10}, 21, 13, 23, (90)]
# SWAP 90 and 10
# [None, 99, 22, 61, (90), 21, 13, 23, {10}]

90‘s parent is now 22, so the parent element is still smaller than the child. Keep on swappin’!

# [None, 99, 22, 61, (90), 21, 13, 23, 10]
# SWAP 22 and 90
# [None, 99, (90), 61, {22}, 21, 13, 23, 10]

Okay, you can let out that sigh of relief. We’ve restored the heap properties!

# [None, {99}, (90), 61, 22, 21, 13, 23, 10]
# The parent, 99, is greater than the child, 90!

Let’s recap our strategy for .heapify_up():

start at the last element of the list
while there's a parent element available:
  if the parent element is smaller:
    swap the elements
  set the target element index to be the parent's index





Max-Heaps: Python
Review
1 min

Nice work! You’ve implemented a MaxHeap class in Python. Heaps are useful because they’re efficient in maintaining their heap properties.

Let’s recap what we learned:

    A max-heap tracks the maximum element as the element at
    Preview: Docs Loading link description
    index
    1 within an internal Python list.
    Max-heaps must maintain the heap property that the parent values must be greater than their children.
    When adding elements, we use .heapify_up() to compare the new element with its parent; if it violates the heap property, then we must swap the two values.

In the next lesson, we’ll learn how to extract the root value of a heap as well as how to sort data using heapsort!



"""


class MaxHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  # END OF HEAP HELPER METHODS
  
  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()
    
  def heapify_up(self):
    print("Heapifying up")
    # add your code below
    idx = self.count
    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent < child:
        print(f"swapping {parent} with {child}")
        self.heap_list[idx],self.heap_list[self.parent_idx(idx)] = self.heap_list[self.parent_idx(idx)],self.heap_list[idx]
      idx = self.parent_idx(idx)
    print("HEAP RESTORED! {0}".format(self.heap_list))





    