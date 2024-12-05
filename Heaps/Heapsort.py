"""
Heapsort

Learn about how a heapsort algorithm works.

Heapsort is an algorithm that sorts arrays by inserting the data into a heap data structure and then repeatedly extracting the root of the heap. Heapsort is a particularly time-efficient algorithm due to its O(n log n) time complexity in every case.

In this article, we’ll go over the necessary steps to implement a heapsort algorithm.
How the algorithm works

Here’s how we’ll accomplish the implementation of heapsort:

    Build a max-heap to store the data from an unsorted list.
    Extract the largest value from the heap and place it into a sorted list.
    Replace the root of the heap with the last element in the list. Then, rebalance the heap.
    Once the max-heap is empty, return the sorted list.

Let’s break these steps down a little more.
Build a max-heap

For this algorithm, we’ll want to build out a max-heap. As a reminder, in a max-heap, the root value is the largest value. Each parent node must have a larger value than its associated children.

Imagine we had the following list of unsorted values:

[14, 11, 2, 20, 3, 10, 3]

By placing our values into a max-heap data structure, our list would look like this:

[20, 11, 14, 2, 10, 5, 3]

We can visualize the above max-heap like so:

max-heap
Extract the root of the heap

In order to sort our data, we’ll repeatedly extract and remove the largest value from the heap until it’s empty. By following the rule of heaps, we can expect to find the largest value located at the root of the heap.

After removing the largest value, we can’t just leave our heap without a root because that would cause us to have two orphaned nodes. Instead, we can swap our root node with the last element in the heap. Since the last element has no children, we can easily remove the value from the heap.

This step does cause one major problem. By swapping the two elements, our root node isn’t the largest value in the heap! We’ll need to restructure the heap in order to ensure that it’s balanced.
Restore the heap: heapify down

With the root value no longer holding the largest value, we’ve violated an important rule about heaps: the parent must contain a value that is larger than its children’s values.

We can fix this though! In the previous lesson, we learned how to heapify up: adding a value to the end of a heap and working our way up the data structure to find its correct placement. Now we need to heapify down. To heapify down, we’ll first compare our new root value to its children. Then, we’ll select the child with the larger value and swap it with the root value. We’ll continue working our way down the heap until it is balanced again:

heapify down

In the example above, we swap the original root value 20 with the right-most child 3. With 3 as the new root, we compare the value to its child value, 14. Since 14 is greater than 3, we will swap the two values and make 14 the new root. Next, we’ll compare 3 to its new child value, 5. Once again, the child value is greater than its parent, so we will swap 3 and 5. With no more children to compare 3 to, our heap has been rebalanced.
Repeat

We’ll repeat the process of swapping the root and the last element, extracting the largest value, and rebalancing the heap while the data structure has a size greater than 1. Once we hit this condition, we will have an ordered list of values.
Review

Great job completing this article! We learned that a heapsort is a sorting algorithm that uses heaps to organize data. To implement heapsort, we did the following:

    We placed an unordered list into a max-heap.
    While the max-heap had at least 1 element, we extracted the root of the heap and swapped it with the left-most child node. The extracted value was then placed at the beginning of a list that contains the sorted values.
    After the left-most child was placed at the root of the heap, we rebalanced the heap by comparing the new root value with the next largest child; if the child was greater than the parent, we swapped the two values. We continued this process until the heap was restored.
    Once the heap was empty, we returned the sorted list.

    

Introduction to Heapsort
2 min

Heapsort is a sorting
Preview: Docs Loading link description
algorithm
that utilizes the heap data structure to sort a list in ascending order.

In this lesson, we’ll go over how to complete the following tasks in order to build a heapsort
Preview: Docs Loading link description
method
in Python:

    First, add the values of an unsorted list into a max-heap.
    Next, while the heap has at least one item, swap the placement of the heap’s largest value with the last value in the heap.
    After the values are swapped, remove the last element in the heap and place it in a list that will be returned at the end. 
    For every time we swap and extract the root, we then must rebalance the heap.
    Finally, return the sorted list.

Let’s get started!




Narrative and Instructions
Learn
Heapsort: Python
Build a Max-Heap
6 min

Our first step with implementing the heapsort
Preview: Docs Loading link description
algorithm
is to organize our unsorted data by placing it into a heap. For this lesson, we’ll be using a max-heap, which we learned about previously.

As a quick refresher, a max-heap is a
Preview: Docs Loading link description
binary
tree type data structure that stores the largest value at its root. The root can always be found at the first element of heap structure. 
Max-heaps have one major rule: the parent must contain a larger value than its children.

Take a look at the following list:

[22, 21, 61, 13, 10, 23, 99]

After adding the above values into a max-heap, the new list should look like this:

[None, 99, 22, 61, 10, 21, 13, 23]

Let’s go over some details about this heap:

    We can picture this heap like so:

         99
       /    \
     22      61
    /  \    /  \
   10  21  13  23

    The root value of this heap is 99. Its left child is 22 and its right child is 61.
    The children of 22 are 10 and 21.
    The children of 61 are 13 and 23.
    The None value at
    Preview: Docs Loading link description
    index
    0 is a sentinel value that will terminate a loop when read as input. This sentinel element saves us the trouble of checking whether the list is empty or not

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

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  # END OF HEAP HELPER METHODS
  
  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()
    
  def heapify_up(self):
    print("Heapifying up")
    idx = self.count
    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent < child:
        print("swapping {0} with {1}".format(parent, child))
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      idx = self.parent_idx(idx)
    print("Heap Restored {0}".format(self.heap_list))

  def retrieve_max(self):
    if self.count == 0:
      print("No items in heap")
      return None
    max_value = self.heap_list[1]
    print("Removing: {0} from {1}".format(max_value, self.heap_list))
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    print("Last element moved to first: {0}".format(self.heap_list))    
    self.heapify_down()
    return max_value

  def heapify_down(self):
    idx = 1
    while self.child_present(idx):
      print("Heapifying down!")
      larger_child_idx = self.get_larger_child_idx(idx)
      child = self.heap_list[larger_child_idx]
      parent = self.heap_list[idx]
      if parent < child:
        self.heap_list[idx] = child
        self.heap_list[larger_child_idx] = parent
      idx = larger_child_idx
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("") 

  def get_larger_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child > right_child:
        print("Left child "+ str(left_child) + " is larger than right child " + str(right_child))
        return self.left_child_idx(idx)
      else:
        print("Right child " + str(right_child) + " is larger than left child " + str(left_child))
        return self.right_child_idx(idx)