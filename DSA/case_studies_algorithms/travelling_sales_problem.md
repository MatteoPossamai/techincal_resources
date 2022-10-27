## TRAVELLING SALES PROBLEM (TSP)

The travelling sales problem (TSP) is a classic problem in computer science. The problem is to find the shortest path that visits all the cities in a given set of cities. The problem is NP-hard, which means that it is difficult to solve, and there is still no way to solve it in a complexity with a constant base (Like   O(1) or O(n) or O(n^2)). 

So there are two ways to solve it:
1. Exact algorithm: This algorithm will find the best solution, but it will take a lot of time to find it. The complexity is exponential.
2. Approximate algorithm: This algorithm will find a solution that is close to the best solution, but it will be faster than the exact algorithm. The complexity is polynomial.

The exact algorithm is called brute force. It will try all the possible combinations and find the best one. The complexity is O(n!), where n is the number of cities.

There is also another exact algorithm, called the Held-Karp Algorithm, that is a dynamic programming approach. It has still a high complexity (O(n^2 * 2^n)), but it is better than the brute force.

So, usually the best choice to solve this problem is to use a approximate algorithm. 

One of them is the Christofides Algorithm. It is a greedy algorithm that will find a solution that is close to the best solution. The complexity is O(n^2 * log(n)). It transforms the graph into a tree, and then travers it as a tree. It uses a minimum spanning tree and a minimum weight matching to find the solution.
