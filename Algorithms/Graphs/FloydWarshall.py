"""
An implementation of Floyd Warshall algorithm, also known as Roy Warshall algorithm or Roy-Floyd algorithm.
The algorithm is for solving a problem is to find the shortest distances between every pair of vertices in a given
edge-weighted graph.
Compared to the Dijkstra's algorithm it works with negative edge weights (with an exception to negative weight cycles).
This algorithm follows the dynamic programming approach as its working pattern, so the algorithm does not construct the
path itself, but it can reconstruct the path with a simple modification.
Time complexity is O(n ** 3)
Space complexity is O(n2)
Applications:
- helps to find the inversion of real matrices,
- helps in testing whether the undirected graph is bipartite,
- helps to find the shortest path in a directed graph,
- It helps in finding the similarity between the graphs,
- finding the optimal routing i.e. the maximum flow between two vertices,
and others.
"""


def floyd_warshall(graph_matrix):
    """
    Function runs Floyd Warshall algorithm to return a matrix of distances between each vertex of the graph
    :param graph_matrix: a matrix representing graph structure, where INF means no direct edge between vertexes
    :return: a matrix of distances between each vertex of the graph
    """
    for k in range(vertexes_number):
        for i in range(vertexes_number):
            for j in range(vertexes_number):
                graph_matrix[i][j] = min(graph_matrix[i][j], graph_matrix[i][k] + graph_matrix[k][j])
    return graph_matrix


def print_solution(distances_matrix):
    """
    A helper function for pretty print of a matrix
    :param distances_matrix: a matrix of distances between each vertex of the graph
    :return:
    """
    for i in range(vertexes_number):
        for j in range(vertexes_number):
            if distances_matrix[i][j] == INF:
                print("INF".ljust(2), end='')
            else:
                print(str(distances_matrix[i][j]).ljust(3), end='')
        print(" ")


if __name__ == '__main__':
    INF = float('inf')

    test_graph = [[0, 3, INF, 5],
                  [2, 0, INF, 4],
                  [INF, 1, 0, INF],
                  [INF, INF, 2, 0]
                  ]

    vertexes_number = len(test_graph)
    print_solution(floyd_warshall(test_graph))
