"""
A simplified implementation of Kosaraju's algorithm (based in vertex indexes and prints strongly connected components).
Kosaraju's Algorithm is based on the depth-first search algorithm implemented twice and is used to find strongly
connected components in directed graphs.
A directed graph is strongly connected if there is a path between all pairs of vertices. A strongly connected component
(SCC) of a directed graph is a maximal strongly connected subgraph.
"""
from collections import defaultdict


class Graph:
    """
    A class that describes graph structure using a graph adjacency list
    """
    def __init__(self, vertex_number):
        """
        initialisation of a Graph instance, using defaultdict as a base for further graph description
        :param vertex_number: number of vertexes in graph
        """
        self.vertex_number = vertex_number
        self.graph = defaultdict(list)

    def add_edge(self, start_vertex, end_vertex):
        """
        method adds an edge to graph instance by filling the graph adjacency list
        :param start_vertex: start vertex of directed edge
        :param end_vertex: end vertex of directed edge
        :return: None
        """
        self.graph[start_vertex].append(end_vertex)

    def dfs(self, vertex_index, visited_vertexes):
        """
        A recurrent DFS algorithm with addition of print function for printing strongly connected components
        :param vertex_index: current vertex index
        :param visited_vertexes: list of indexes of visited vertexes
        :return:
        """
        visited_vertexes[vertex_index] = True
        print(vertex_index, end='')
        for neighbour in self.graph[vertex_index]:
            if not visited_vertexes[neighbour]:
                self.dfs(neighbour, visited_vertexes)

    def fill_order(self, vertex_index, visited_vertexes, stack):
        """
        Method makes first DFS-run  in the graph to prepare stack for second backwards DFS-run
        :param vertex_index: current vertex index
        :param visited_vertexes: list of indexes of visited vertexes
        :param stack: a stack of vertex indexes in order of visit
        :return:
        """
        visited_vertexes[vertex_index] = True
        for neighbour_index in self.graph[vertex_index]:
            if not visited_vertexes[neighbour_index]:
                self.fill_order(neighbour_index, visited_vertexes, stack)
        stack.append(vertex_index)

    def transpose(self):
        """
        method makes a transposed representation of initial graph to use it in second DFS-run
        :return: a transposed representation of initial graph
        """
        transposed_graph = Graph(self.vertex_number)

        for start_vertex in self.graph:
            for end_vertex in self.graph[start_vertex]:
                transposed_graph.add_edge(end_vertex, start_vertex)
        return transposed_graph

    def print_scc(self):
        """
        Implementation of the main function of Kosaraju's algorithm
        :return: None
        """
        stack = []  # prepare a stack
        visited_vertexes = [False] * self.vertex_number  # prepare list of indexes of visited vertexes

        for vertex_index in range(self.vertex_number):  # first DFS to fill the stack
            if not visited_vertexes[vertex_index]:
                self.fill_order(vertex_index, visited_vertexes, stack)

        transposed_graph = self.transpose()  # transpose the graph to make a second reversed DFS run
        visited_vertexes = [False] * self.vertex_number  # clean the list of indexes of visited vertexes

        while stack:  # second DFS run (in order of stack) and printing of strongly connected components
            current_vertex = stack.pop()
            if not visited_vertexes[current_vertex]:
                transposed_graph.dfs(current_vertex, visited_vertexes)
                print()


if __name__ == '__main__':
    test_graph_1 = Graph(8)
    test_edges_1 = [(0, 1), (1, 2), (2, 3), (2, 4), (3, 0), (4, 5), (5, 6), (6, 4), (6, 7)]

    for start, end in test_edges_1:
        test_graph_1.add_edge(start, end)

    print("Strongly Connected Components:")
    test_graph_1.print_scc()
