"""Breadth-First Search (BFS) traverses the graph systematically, level by level, forming a BFS tree along the way.
This algorithm can be used for both graph traversal and search.
When searching for a node that satisfies a certain condition (target node), the algorithm will find the shortest
distance from the starting node to the target node. The distance is defined as the number of edges traversed.
Breadth-First Search can be used to solve problems such as:
- determining the levels of each node,
- finding connected components of graph,
- finding spanning trees,
- finding the shortest path between two nodes in an unweighted graph,
- finding the shortest cycle in oriented unweighted graph,
- finding all edges that belong to the shortest path between a given pair of nodes,
- finding all nodes that belong to the shortest path between a given pair of nodes,
and some others.
"""
from collections import deque


def bfs(graph, start_vertex):
    """
    The implementation of Breadth-First Search algorithm using queue that returns levels of vertexes
    :param graph: searched graph in a form of a graph adjacency list
    :param start_vertex: start vertex
    :return: a dict of levels for each vertex according to start vertex
    """
    levels = {key: None for key in graph}
    levels[start_vertex] = 0
    queue = deque([start_vertex])

    while queue:
        current_vertex = queue.popleft()
        for neighbour in graph[current_vertex]:
            if levels[neighbour] is None:
                levels[neighbour] = levels[current_vertex] + 1
                queue.append(neighbour)
    return levels


if __name__ == '__main__':
    graph_adj = {  # 15 vertexes and 16 edges
        '0': ['1', '10', '11', '12'],
        '1': ['0', '7'],
        '2': ['6'],
        '3': ['11'],
        '4': ['10', '6'],
        '5': ['13', '8'],
        '6': ['2', '4', '10'],
        '7': ['1', '13'],
        '8': ['5', '12'],
        '9': ['11'],
        '10': ['0', '4', '6'],
        '11': ['0', '12', '9', '3', '14'],
        '12': ['0', '11', '8'],
        '13': ['7', '5'],
        '14': ['11'],
    }

    print(bfs(graph_adj, '0'))
