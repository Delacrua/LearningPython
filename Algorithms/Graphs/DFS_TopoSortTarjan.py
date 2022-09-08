"""Simple toposort implementation using Tarjan algorithm.
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed
edge u v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not
a DAG.
"""


def toposort(unsorted_graph):
    """
    An implementation of topological sorting for a graph using Tarjan algorithm
    :param unsorted_graph: graph in form of a graph adjacency list
    :return:
    """

    def _dfs(vertex, graph, visited: set, resulting_list: list):
        """
        DFS algorithm modified for Tarjan implementation
        :param vertex: current vertex
        :param graph: graph in form of a graph adjacency list
        :param visited: set of visited vertexes
        :param resulting_list: list of visited vertexes
        :return:
        """
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                _dfs(neighbour, graph, visited, resulting_list)
        resulting_list.append(vertex)  # main addition of logic required for DFS to implement toposort

    visited_vertexes = set()
    result = []
    for current_vertex in unsorted_graph:
        if current_vertex not in visited_vertexes:
            _dfs(current_vertex, unsorted_graph, visited_vertexes, result)
    result = result[::-1]
    return result


d = {0: [1, 2, 4], 1: [3, 4], 2: [3], 3: [5], 4: [5], 5: []}
print(toposort(d))
