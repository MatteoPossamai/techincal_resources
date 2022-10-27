## SHORTEST PATH PROBLEM

The shortest path problem consistst in finding the shortest path in a graph from a node to another one, given that each edge has a weight that rappresents its cost, or just the number of edges if the graph has no weighted edges (in this case use BFS).

## SOLUTIONS:

### DIJKSTRA'S ALGORITHM

The algorithm is based on the fact that the shortest path from a node to another one is the sum of the shortest path from the first node to the node before the last one and the weight of the edge between the last two nodes. This is why it is a Greedy algorithm.

You have to compute the shortest path from the source node to all the other nodes, and then you can find the shortest path from the source node to the destination node. It is usually done by using a priority queue, where the priority is the distance from the source node. 

The algorithm complexity is O(|V|^2) because in the worst case you will visit each node and each edge, but it can be improved to O(|E|log|V|) by using a priority queue.

#### PSEUDOCODE

    dijkstra(G, s):
        for each vertex v in V[G]:
            dist[v] = inf
            prev[v] = null
        dist[s] = 0
        Q = V[G]
        while Q is not empty:
            u = extract_min(Q)
            for each vertex v in Adj[u]:
                alt = dist[u] + w(u, v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        return dist[], prev[]

