r"""
    Hackerrank > Algorithms > Graph Theory > Breadth First Search

    Given an undirected graph consisting of N nodes (labelled 1 to N)
    where a specific given node S represents the start position, and an edge
    between any two nodes is of length 6 units in the graph, calculate the
    shortest distance from the start position (Node S) to all of the other
    nodes in the graph.

    Input Format:
    - The first line contains T, denoting the number of test cases.
    - The first line of each test case has two integers N, denoting the
      number of nodes in the graph, and M, denoting the number of edges in the
      graph.
    - The next M lines each consist of two space-separated integers x y, where
      x and y denote the two nodes between which the edge exists.
    - The last line of a testcase has an integer S, denoting the starting
      position.

    Constraints:
    1 <= T <= 10
    2 <= N <= 1000
    1 <= M <= N(N-1)/2
    1 <= x, y, S <= N

    Output Format:
    For each of the T test cases, print a single line consisting of N-1 space-
    separated integers, denoting the shortest distances of the N-1 nodes from
    starting position S, in the order of input 1 to N.

    For unreachable nodes, print -1.
"""


__author__ = 'ignyfera'


class Solution(object):
    def __init__(self, n, edges, unit = 1):
        """ initializes a graph with n vertices, given a list of edges and
            a unit length for each edge """
        self.size = n
        self.graph = {}
        # for each vertex, specify connected edges
        for i in xrange(n):
            self.graph[i+1] = set()
        for e in edges:
            self.graph[e[0]].add(e[1])
            self.graph[e[1]].add(e[0])
        # unit length
        self.unit = unit

    def bfs(self, start):
        visited     = set()
        tovisit     = [start]
        dist        = {}
        dist[start] = 0
        while tovisit:
            vert = tovisit.pop(0)
            if vert in visited: continue
            visited.add(vert)
            nextverts = self.graph[vert] - visited
            for w in nextverts:
                if w in dist: continue
                dist[w] = dist[vert]+self.unit
            tovisit.extend(nextverts)
        return dist

    def solve(self, start):
        dist = self.bfs(start)
        sol  = []
        for i in xrange(self.size):
            if i+1 == start: continue
            elif i+1 not in dist: sol.append(-1)
            else: sol.append(dist[i+1])
        return ' '.join(map(str, sol))
  

# read input and write output
t = int(raw_input().strip())
for _ in xrange(t):
    n, m = map(int, raw_input().strip().split())
    edges = []
    for _ in xrange(m):
        edges.append(tuple(map(int, raw_input().strip().split())))
    s = int(raw_input().strip())

    print Solution(n, edges, 6).solve(s)
