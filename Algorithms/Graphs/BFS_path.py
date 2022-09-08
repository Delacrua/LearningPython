"""This BFS algorithm restores the shortest path between two given vertexes
"""
from collections import deque


def bfs_path(graph, start_vertex, end_vertex):
    """
    The implementation of Breadth-First Search algorithm using queue that restores the shortest path between two given
    vertexes
    :param graph: searched graph in a form of a graph adjacency list
    :param start_vertex: start vertex of path
    :param end_vertex: end vertex of path
    :return: a list of vertexes in the shortest path from start to end
    """
    visited = {key: False for key in graph}
    visited[start_vertex] = True
    queue = deque([start_vertex])
    parents = {key: None for key in graph}

    while queue:
        current_vertex = queue.popleft()
        for neighbour in graph[current_vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                parents[neighbour] = current_vertex
                queue.append(neighbour)

    path = [end_vertex]
    parent = parents[end_vertex]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]

    return path[::-1]


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

    print(bfs_path(graph_adj, '0', '13'))
