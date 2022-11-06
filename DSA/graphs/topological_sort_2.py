# VERSION 2 WITH OOP AS DATA HOLDER
from collections import defaultdict

class GraphNode:
    data = ''
    neighbors = []

    def __init__(self, data=None, neighbors=[]):
        self.data = data
        self.neighbors = neighbors

def topological_sort(vertex):
    if not visited_dict[vertex]:
        visited_dict[vertex] = True
        for adj in vertex.neighbors:
            topological_sort(adj)
        output_stack.insert(0, vertex)


if __name__ == "__main__":
    # Initialization of nodes
    a = GraphNode(data='a')
    b = GraphNode(data='b')
    c = GraphNode(data='c')
    d = GraphNode(data='d')
    e = GraphNode(data='e')

    # Creation of relationships
    a.neighbors = [d]
    b.neighbors = [d]
    c.neighbors = [e]
    d.neighbors = [e]
    e.neighbors = []

    # Creation of visited dictionary
    visited_dict = defaultdict()
    visited_dict[a] = False
    visited_dict[b] = False
    visited_dict[c] = False
    visited_dict[d] = False
    visited_dict[e] = False

    # Creation of output variabiles and loop
    output_stack = []

    for vertex in visited_dict:
        topological_sort(vertex)

    for e in output_stack:
        print(e.data)
