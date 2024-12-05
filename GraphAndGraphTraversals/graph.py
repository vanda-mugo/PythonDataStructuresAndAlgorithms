"""
Introduction to Graphs
3 min

In this lesson, we’ll build a robust implementation of the graph data structure. With just two classes, Vertex and Graph, we can implement a variety of
Preview: Docs Loading link description
graphs
that satisfy the requirements of many algorithms.

Let’s detail the functionality we require from these classes:

    Vertex stores some data.
    Vertex stores the edges to connected vertices and their weight.
    Vertex can add a new edge to its collection.
    Graph stores all the vertices.
    Graph knows if it is directed or undirected.
    Graph can add a new vertex to its collection.
    Graph can add a new edge between stored vertices.
    Graph can tell whether a path exists between stored vertices.

Since we’re dealing with multiple classes, we’ll use multiple files for this implementation. To keep the concepts grounded in a real-world 
application, we’ll build up a transportation network of railroads and train stations as we go.


Building the Vertex
6 min

Let’s start with our Vertex class. This class is responsible for storing information about individual vertices in our graph. 
In our railway network, instances of Vertex will represent train stations.

An instance of Vertex will store data and a Python
Preview: Docs Loading link description
dictionary
which tracks other Vertex instances connected to self.



Building the Vertex II
7 min

We’ll continue building out the Vertex class. Remember, it’s responsible for knowing which other vertices are connected. 
These connections are the edges of our graph implementation.

A key in the Vertex instance’s edges
Preview: Docs A dictionary is an unordered set of (key, value) pairs. It provides a way to map pieces of data to each other, 
and allows for quick access to values associated to keys. The syntax of a dictionary is as follows: pseudo dictionary = { key1: value1, key2: value2, key3: value3
dictionary
represents a connection to that other vertex. For now, we can just set the value to be True.

grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')

print(grand_central.get_edges())
# []

grand_central.add_edge(forty_second_street)
print(grand_central.edges)
# { "42nd Street Station": True }
print(grand_central.get_edges())
# ["42nd Street Station"]

Let’s add this functionality to our Vertex class!



Building the Graph I
9 min

We’ve built a class to store information and connections between individual vertices, but we need another class that keeps track of the big picture.

Our Graph class will track all the vertices and handle higher level concerns like whether the graph is directed, requiring edges to have a set 
direction, or undirected, allowing bi-directional movement across edges.

We’ll start by giving Graph the functionality to add vertices. We’ll use an internal .graph_dict property to store every vertex by its value 
pointing to the vertex instance itself.

We want to do the following:

grand_central = Vertex("Grand Central Station")
railway = Graph()

print(railway.graph_dict)
# {}
railway.add_vertex(grand_central)
print(railway.graph_dict)
# {"Grand Central Station": grand_central}


Building the Graph II
11 min

We’d like our Graph class to be able to set edges between the stored vertices. An instance of Graph is either directed or undirected, 
which affects how edges work between two vertices. As a reminder, the Graph class defaults to being undirected with edges being set in both directions.

The good news is our Vertex class already has an .add_edge()
Preview: Docs Loading link description
method
, so we can delegate most of the work.

The Graph version of .add_edge() will take a “from” and a “to” vertex, and set the appropriate edges by calling the Vertex instance’s own .add_edge().

undirected_railway = Graph()
directed_railway = Graph(True)

callan_station = Vertex('callan')
peel_station = Vertex('peel')

undirected_railway.add_vertex(callan_station)
undirected_railway.add_vertex(peel_station)

directed_railway.add_vertex(callan_station)
directed_railway.add_vertex(peel)

directed_railway.add_edge(callan_station, peel_station)
# directed graph will set the edge one-way
print(callan_station.get_edges())
# ['peel']
print(peel_station.get_edges())
# []

undirected_railway.add_edge(callan_station, peel_station)
# directed graph will set the edge both ways
print(callan_station.get_edges())
# ['peel']
print(peel_station.get_edges())
# ['callan']




Adding Weight
6 min

So far our Vertex class has stored edges inside of a
Preview: Docs Loading link description
dictionary
with keys of the connected vertex’s name and the value simply set to True.

We can make our implementation support edge weights with a few small changes. To keep this class as flexible as possible, we’ll introduce a default weight
Preview: Docs Loading link description
argument
to .add_edge() in the Graph and Vertex classes. With no explicit weight argument, it will default to 0. We’ll then set the appropriate value in the dictionary to that weight.

Weighted edges allow us to make
Preview: Docs Loading link description
graphs
that represent rail systems with a travel-time between stations.

railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
harwick = Vertex('harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)

# Travel-time between callan and peel: 12
railway.add_edge(callan, peel, 12)
# Travel-time between harwick and callan: 7
railway.add_edge(harwick, callan, 7)

print(callan.edges)
# { 'peel': 12 }
print(harwick.edges)
# { 'callan': 7 }


Finding a Path I
8 min

Our railway has grown to four stations with two connecting tracks. How can we tell a passenger which stations are reachable from Harwick?

undirected_railway = Graph()

callan_station = Vertex('callan')
peel_station = Vertex('peel')
ulfstead_station = Vertex('ulfstead')
harwick_station = Vertex('harwick')

undirected_railway.add_vertex(callan_station)
undirected_railway.add_vertex(peel_station)
undirected_railway.add_vertex(harwick_station)
undirected_railway.add_vertex(ulfstead_station)

undirected_railway.add_edge(peel_station, harwick_station)
undirected_railway.add_edge(peel_station, callan_station)

Our Graph class needs to determine whether a path exists between two vertices. A path means two vertices which are 
connected by a sequence of one or more intermediary edges and
Preview: Docs Loading link description
graphs
.



Finding a Path II
10 min

Our pathfinding
Preview: Docs Loading link description
method
is almost complete. Let’s take a step back and think how a passenger in Harwick station could find their way to Callan.

First, they’d look for all the stations connected to Harwick. If one of those stations was Callan, they’re in luck!

Otherwise, they would look for the connections from each of those stations excluding Harwick because they’ve already crossed it off their list.

We’ll take the same strategy with our pathfinding method.

while len(start) > 0:
  current_vertex = start.pop(0)
  # current_vertex is end_vertex
    # a path exists!
  # current_vertex is not end_vertex
    # add vertices connected to 
    # current_vertex onto the list
    # to keep searching for a path

    

Refactoring Path-Finding
8 min

Our pathfinding
Preview: Docs A method is a small piece of code, usually defined in a class, that can be used outside the class and in other parts of the program.
method
works when a path exists, but there is a serious bug! We’re not accounting for cycles in our graph.

Consider the following undirected Graph:

railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
ulfstead = Vertex('ulfstead')
harwick_station = Vertex('harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
railway.add_vertex(ulfstead)

railway.add_edge(peel, harwick)
railway.add_edge(harwick, callan)
railway.add_edge(callan, peel)

railway.find_path(peel, ulfstead)

Peel connects to Harwick and Callan. We look for a path starting at peel, adding harwick and callan to the start list. Next, we look at harwick, 
adding peel and callan. We’ll keep adding the same vertices, and our loop will never terminate.

When a path exists, return True will exit the loop. When a path does not exist, it’s a major problem!

We’ll use a
Preview: Docs Loading link description
dictionary
to track which stations we’ve visited. This will stop our passengers from riding around in circles.



Graph Review
1 min

Fantastic work! We’ve implemented a robust graph data structure in Python. Our two classes, Vertex and Graph are capable of representing the typical variations in
Preview: Docs Loading link description
graphs
that occur in many different algorithms.

Vertex:

    Uses a
    Preview: Docs A dictionary is an unordered set of (key, value) pairs. It provides a way to map pieces of data to each other, and allows 
    for quick access to values associated to keys. The syntax of a dictionary is as follows: pseudo dictionary = { key1: value1, key2: value2, key3: value3
    dictionary
    as an adjacency list to store connected vertices.
    Connected vertex names are keys and the edge weights are values.
    Has methods to add edges and return a list of connected vertices.

Graph:

    Can be initialized as a directed graph, where edges are set in one direction.
    Stores every vertex inside a dictionary
        Vertex data is the key and the vertex instance is the value.
    Has methods to add vertices, edges between vertices, and determine if a path exists between two vertices.


"""
class Graph:
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    seen = {}
    # Checkpoint 1, replace these comments:
    # Use a dictionary to track which
    # vertices we've already visited
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertex = self.graph_dict[current_vertex]
        next_vertices = vertex.get_edges()
        
        # Filter next_vertices so it only
        # includes vertices NOT IN seen
        
        # Checkpoint 3, uncomment and replace the question marks:
        #next_vertices = [vertex for vertex in next_vertices ???????]
        next_vertices = [ vertex for vertex in next_vertices if vertex not in seen]
        start.extend(next_vertices)
        
    return False
