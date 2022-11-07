"""
Topological sorting of a graph.
It is a way of writing a graph in linear order (list) such that for every edge
(u, v), u comes before v in the list. It is like to insert all the courses into
a list such that for every prerequisite course, it comes before the course that 
depends on it.

To perform topological sorting, we need to find a linear ordering of the graph, 
and the graph must be a DAG (Directed Acyclic Graph). If the graph is not a DAG,
there are cycles, and the recursion will never stop.
"""

### VERSION 1 WITH COLLECTIONS AND DICTIONARIES AS DATA HOLDER
from collections import defaultdict

output_stack = []

def topological_sort(vertex):
    if not visited_list[vertex]:
        visited_list[vertex] = True
        for neighbor in adjancency_list[vertex]:
            topological_sort(neighbor)
        output_stack.insert(0, vertex)

adjancency_list = defaultdict()

adjancency_list['a'] = ['d']
adjancency_list['b'] = ['d']
adjancency_list['c'] = ['e']
adjancency_list['d'] = ['e']
adjancency_list['e'] = []

visited_list = defaultdict()

visited_list['a'] = False
visited_list['b'] = False
visited_list['c'] = False
visited_list['d'] = False
visited_list['e'] = False

if __name__ == '__main__':
    print(adjancency_list)
    for vertex in visited_list:
        topological_sort(vertex)
    print(output_stack)