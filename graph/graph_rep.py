'''
https://www.geeksforgeeks.org/graph-and-its-representations/

'''

class Graph:
    def __init__(self, vertices):
        self.V  = vertices
        # self.graph = [[]] * self.V
        self.graph = [list() for i in range(self.V )]

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)


    def print_graph(self):
        for index in range(self.V):
            print(f"List for vertex {index} = {self.graph[index]}" )


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()