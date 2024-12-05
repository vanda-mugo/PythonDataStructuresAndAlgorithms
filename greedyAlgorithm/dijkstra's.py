"""
Dijkstra's Python: Graph Review
2 min

Before we delve into implementing Dijkstra’s
Preview: Docs An algorithm is a formal process used to solve a problem. They can be represented in several formats but 
are usually represented in pseudocode in order to communicate the process by which the algorithms solve the problems they were created to tackle.
Algorithm
, we need a graph to explore it, but how exactly do we represent
Preview: Docs Graphs are a way of modeling systems based on a node and edge structure for representing the relationships between items.
graphs
in python? One of the ways to represent graph is through an adjacency list using a Python
Preview: Docs A dictionary is an unordered set of (key, value) pairs. It provides a way to map pieces of data to each other, 
and allows for quick access to values associated to keys. The syntax of a dictionary is as follows: pseudo dictionary = { key1: value1, key2: value2, key3: value3
dictionary
.

Take a look at the following graph represented by an adjacency list:

graph = {
  'A': [('B', 10), ('C', 3)],
  'B': [('C', 3), ('D', 2)],
  'C': [('D', 2)],
  'D': [('E', 10)],
  'E': [('B', 15)],
}

Reading this adjacency list, we can tell the graph has 5 vertices: 'A', 'B', 'C', 'D', 'E'.

There is a path from 'A' to 'B' with a cost (or edge weight) of 10 and a path from 'A' to 'C' with a cost of 3.

There is a path from 'B' to 'C' with a cost of 3 and a path from 'B' to 'D' with a cost of 2.

There is a path from 'C' to 'D' with a cost of 2.

There is a path from 'D' to 'E' with a cost of 10.

There is a path from 'E' to 'B' with a cost of 15.



Dijkstra's Algorithm: Python
Understanding Heapq
5 min

Remember that Dijkstra’s
Preview: Docs Loading link description
Algorithm
works like the following:

    Instantiate a
    Preview: Docs A dictionary is an unordered set of (key, value) pairs. It provides a way to map pieces of data to each other, 
    and allows for quick access to values associated to keys. The syntax of a dictionary is as follows: pseudo dictionary = { key1: value1, key2: value2, key3: value3
    dictionary
    that will eventually map vertices to their distance from their start vertex

    Assign the start vertex a distance of 0 in a min heap
    Assign every other vertex a distance of infinity in a min heap
    Remove the vertex with the smallest distance from the min heap and set that to the current vertex
    For the current vertex, consider all of it’s adjacent vertices and calculate the distance to them by 
    (distance to the current vertex) + (edge weight of current vertex to adjacent vertex). 
    If this new distance is less than its current distance, replace the distance.
    Repeat 4 and 5 until the heap is empty
    After the heap is empty, return the distances

In order to keep track of all the distances for Dijkstra’s Algorithm, we will be using a heap! Using a heap will allow removing the minimum 
from the heap to be efficient. In python, there is a library called heapq which we will use to do all of our dirty work for us!

The heapq
Preview: Docs Loading link description
method
has two critical methods we will use in Dijkstra’s Algorithm: heappush and heappop.

    heappush will add a value to the heap and adjust the heap accordingly
    heappop will remove and return the smallest value from the heap

Let’s say we start by initializing a heap with the following
Preview: Docs Loading link description
tuple
inside:

heap = [(0, 'A')]

We can add values to this heap like this:

heapq.heappush(heap, (1, 'B'))
heapq.heappush(heap, (-4, 'C'))

We can remove the smallest value in the heap like this:

value, letter  = heapq.heappop(heap)

value will be equal to -4, and letter will be equal to 'C'.

You can read more about the documentation of heapq here.

Initializing Dijkstra's Algorithm
6 min

Now, let’s start writing the algorithm!

The first part of the
Preview: Docs An algorithm is a formal process used to solve a problem. They can be represented in several formats but 
are usually represented in pseudocode in order to communicate the process by which the algorithms solve the problems they were created to tackle.
algorithm
is all about initialization! Here’s what we have to do:

    Define the function with a start vertex and a graph.
    Instantiate a distances
    Preview: Docs A dictionary is an unordered set of (key, value) pairs. It provides a way to map pieces of data to each other, 
    and allows for quick access to values associated to keys. The syntax of a dictionary is as follows: 
    pseudo dictionary = { key1: value1, key2: value2, key3: value3
    dictionary
    that will eventually map vertices to their distance from their start vertex.
    Assign the start vertex a distance of 0.
    Assign every other vertex a distance of infinity.
    Set up a vertices_to_explore min-heap list that keeps track of neighboring vertices left to explore.

After initializing these
Preview: Docs Stores data that can be manipulated and referenced throughout the code.
variables
, we can then traverse the graph and update the distances!


Finishing the Algorithm!
12 min

Let’s finish the algorithm!

First, we’ll traverse the vertices_to_explore heap until it is empty, popping off the vertex with the minimum distance from start. Inside our while loop, 
we’ll iterate over the neighboring vertices of current_vertex and add each neighbor (and its distance from start) to the vertices_to_explore min-heap.

In each neighbor iteration, we will do the following:

    Identify neighbor‘s distance from start.
    Make sure the new distance found for neighbor is less than the distance currently set for distances[neighbor].
    Update distances[neighbor] if the new distance is smaller than the currently recorded distance.
    Add neighbor and its distance to the vertices_to_explore min-heap.



"""


from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
  distances = {}
  
  for vertex in graph:
    distances[vertex] = inf
    
  distances[start] = 0
  vertices_to_explore = [(0, start)]
  
  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
        
  return distances
        
distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))
