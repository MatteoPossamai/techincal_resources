# GRAPHS

A graph is a data structure that is used to describe relationships between objects. It is a collection of nodes and edges. The nodes are the objects and the edges are the relationships between them. The edges can be directed or undirected. A directed edge is an edge that goes from one node to another, while an undirected edge is an edge that goes from one node to another and vice versa. The edges can also have weights, which are values that represent the cost of the edge. The nodes can also have weights, which are values that represent the cost of the node.

In a graph there may be cycles, which are cases into you can reach a node from itself. There may also be isolated nodes, which are nodes that are not connected to any other node. There are types of graphs that does not have any cycle, like DAG (Directed Acyclic Graph). There are also types of graphs that does not have any isolated nodes, like trees.

## TABLE OF COMPLEXITY
| Operation | Time Complexity |
|-----------|-----------------|
| Storing   | O(V+E)          |
| Traversing| O(V+E)          |

### CONNECIVITY

Graphs may be:
1. Connected: if there is a path between every pair of nodes.
2. Disconnected: if there is no path between some pair of nodes.
The connectivity of a graph is the number of connections that needs to be destroyed to make the graph disconnected. The connectivity of a graph is the number of connected components that the graph has.

Here there is a more precise explaination of all the types of graphs:

1. Disconnected graphs are very similar whether the graph's directed or undirected—there is some vertex or group of vertices that have no connection with the rest of the graph.

2. Weakly Connected: A directed graph is weakly connected when only replacing all of the directed edges with undirected edges can cause it to be connected. Imagine that your graph has several vertices with one outbound edge, meaning an edge that points from it to some other vertex in the graph. There's no way to reach all of those vertices from any other vertex in the graph, but if those edges were changed to be undirected all vertices would be easily accessible.

3. Connected: Here we only use "connected graph" to refer to undirected graphs. In a connected graph, there is some path between one vertex and every other vertex.

4. Strongly connected: directed graphs must have a path from every node and every other node. So, there must be a path from A to B AND B to A.

### RAPPRESENTATION

In an OOP envirnoment, there may be an implementation for Edges and Nodes, and all the rappresentation would a sort of abstraction of all the data. But this not really efficient. 

Another common way to reppresent grapsh are edges lists. It is a sort of matrix where there are contained the two elements that are linked toghether by an edge, in a tuple. 

Another way to rappresent graphs is with adjacency lists. It is a rectangular matix where each element can be a 0 or a one. It is a one if between the node rappresented in the given list and the node rappresented in the given column there is an edge.

### TRAVERSALS

There are two main ways of traversing a graph, depth-first search and breadth-first search, as in trees. 

#### DEPTH-FIRST SEARCH DFS

You start from where you prefer, and you need to keep track of element you visiter previously, via a Stack usually. Then you move to another edge and put it in the stack. Repeat. If you reach a node that you already visited, you need to backtrack, so you need to pop the stack, and try another edge. Then, if there are not other viable edges, you need to backtrack again. Repeat until you reach the end. This algorithm may also be made recursively, but with the same approach. Efficiencty is O(V+E), where V is the number of vertices and E is the number of edges.

#### BREADTH-FIRST SEARCH BFS

In this case, we also start from whatever node you prefer. Then we visit all the adjacent nodes, and we add them into a queue structure. Then we visit the first node in the queue (dequeueing it), and we add all the adjacent nodes to the queue. We repeat this process until the queue is empty. Efficiencty is O(V+E), where V is the number of vertices and E is the number of edges.

### PATHS

Paths are basically a sequence of nodes that are connected by edges. There are two types of paths:
1. Simple paths: a path that does not contain any repeated nodes.
2. Cycles: a path that starts and ends in the same node.

#### EULERIAN PATH

An Eulerian path starts in a node, travers all the tree, and then it stops in another node. If it ends in the same node, it is called Eulerian Cycle and do not pass again on the same nodes. Euler said that a graph has an Eulerian path if and only if all the nodes have even degree. If they are Path, this restriction does not exist. 

#### HAMILTONIAN PATH

A Hamiltonian path is a path that visits every node in the graph exactly once. It is a special case of Eulerian path. A graph has a Hamiltonian path if and only if all the nodes have even degree.

### CODE EXAMPLE FOR GRAPH STRUCTURE

```python
class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)
```

### CODE EXAMPLES FOR SEARCHES

#### BFS

    def bfs(graph, start):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)
        return visited

#### DFS

    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for next in graph[start] - visited:
            dfs(graph, next, visited)
        return visited
 