"""
Dijkstra's algorithm is for finding the shortest paths between nodes in undirected, connected, weighted graphs.
Originally - it was used to calculate the shortest path between two nodes. Due to the way it works, it was adapted to
calculate the shortest path between a starting node and every other node in the graph. This way it can be used to
produce a shortest-path tree that consists of the shortest path between two nodes, as well as all other nodes, which is
a drawback of Dijkstra's algorithm that makes it unfit for large graphs.
Time complexity is O(n ** 2)
"""
from collections import deque


def read_graph(vertexes_data):
    """
    A function for preparing a weighted graph from a collection of tuples
    :param vertexes_data: collection of tuples (vertex_1, vertex_2, edge_weight) that describe graph structure
    :return: a graph in a form of a graph adjacency list with weights
    """
    def _add_edge(graph, vertex_1, vertex_2, weight):
        """
        Helper function to store an edge with weight for vertexes
        :param graph: a graph in a form of a graph adjacency list with weights
        :param vertex_1: first given vertex
        :param vertex_2: second given vertex
        :param weight: weight of edge between given vertexes
        :return: None
        """
        if vertex_1 not in graph:
            graph[vertex_1] = {vertex_2: weight}
        else:
            graph[vertex_1][vertex_2] = weight

    traversed_graph = {}
    for ver_1, ver_2, wgh in vertexes_data:
        _add_edge(traversed_graph, ver_1, ver_2, wgh)
        _add_edge(traversed_graph, ver_2, ver_1, wgh)
    return traversed_graph


def run_dijkstra(graph, start_vertex):
    """
    Dijkstra algorithm for finding minimal distances between a vertex and all other vertexes of a weighted graph
    :param graph: a graph in a form of a graph adjacency list with weights
    :param start_vertex: start vertex
    :return: a dictionary of minimal distances between start vertex and other vertexes
    """
    queue = deque()
    shortest_distances = {}
    shortest_distances[start_vertex] = 0
    queue.append(start_vertex)

    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            edge_weight = graph[vertex][neighbour]
            parent_weight = shortest_distances[vertex]
            existing_weight = shortest_distances.get(neighbour, float('inf'))

            if existing_weight == float('inf') or parent_weight + edge_weight < existing_weight:
                shortest_distances[neighbour] = parent_weight + edge_weight
                queue.append(neighbour)

    return shortest_distances


def restore_path(graph, start_vertex, end_vertex, distances):
    """
    A function for restoring one of possible shortest paths from start vertex to end vertex using results of Dijkstra's
    algorithm
    :param graph: a graph in a form of a graph adjacency list with weights
    :param start_vertex: start vertex
    :param end_vertex: end vertex
    :param distances: a dictionary of minimal distances between start vertex and other vertexes
    :return: a list of vertexes forming one of possible shortest paths from start vertex to end vertex
    """
    path = [end_vertex]
    while end_vertex != start_vertex:
        for neighbour, weight in graph[end_vertex].items():
            if distances[neighbour] == distances[end_vertex] - weight:
                path.append(neighbour)
                end_vertex = neighbour
    return path[::-1]


def dijkstra_main(vertexes_data, start_vertex, end_vertex):
    """
    Main function for running algorithm
    :param vertexes_data: collection of tuples (vertex_1, vertex_2, edge_weight) that describe graph structure
    :param start_vertex: start vertex
    :param end_vertex: end vertex
    :return: None
    """
    graph = read_graph(vertexes_data)
    shortest_distances = run_dijkstra(graph, start_vertex)
    shortest_path = restore_path(graph, start_vertex, end_vertex, shortest_distances)
    print(f'shortest distances from {start_vertex}: {shortest_distances}')
    print(f'shortest path from {start_vertex} to {end_vertex}: {shortest_path}')


if __name__ == '__main__':
    test_vertexes = [('A', 'B', 2), ('A', 'H', 15), ('B', 'C', 1), ('B', 'D', 5), ('C', 'D', 3), ('C', 'F', 2),
                     ('C', 'G', 1), ('D', 'F', 4), ('D', 'E', 6), ('E', 'F', 7), ('E', 'I', 2), ('F', 'G', 1),
                     ('F', 'H', 3), ('H', 'I', 12),
                     ]
    dijkstra_main(test_vertexes, 'A', 'I')
