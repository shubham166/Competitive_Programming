from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)


    def BFS(self, s):
        visited = [False] * len(self.graph)

        q = []
        q.append(s)
        visited[s] = True
        while len(q) > 0:
            src = q.pop()
            print(f"Node visited = {src}")
            for e in self.graph[src]:
                if not visited[e]:
                    q.append(e)
                    visited[e] = True

    def print_graph(self):
        for index in range(len(self.graph)):
            print(f"List for vertex {index} = {self.graph[index]}" )

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
# g.print_graph()
