"""This BFS algorithm is an example of a practical task of restoring one of possible shortest paths between two given
chessboard fields for a chess knight
"""
from collections import deque


def prepare_knight_graph():
    """
    A function for preparing a chessboard graph displaying legal chess knight moves
    :return: a graph in a form of a graph adjacency list
    """

    def _add_edge(graph, vertex_1, vertex_2):
        """
        Helper function to store edges in both directions for two vertexes
        :param graph: a graph in a form of a graph adjacency list
        :param vertex_1: first given vertex
        :param vertex_2: second given vertex
        :return: None
        """
        graph[vertex_1].append(vertex_2)
        graph[vertex_2].append(vertex_1)

    chessboard_letters = 'abcdefgh'
    chessboard_numbers = '12345678'
    chess_graph = {letter + number: list() for number in chessboard_numbers for letter in chessboard_letters}

    for i, letter in enumerate(chessboard_letters):
        for j, number in enumerate(chessboard_numbers):
            vert_1 = letter + number
            vert_2 = ''
            for i_modified, j_modified in (i + 2, j + 1), (i - 2, j + 1), (i + 1, j + 2), (i - 1, j + 2):
                if 0 <= i_modified < 8 and 0 <= j_modified < 8:  # 8 is length of sides of chessboard
                    vert_2 = chessboard_letters[i_modified] + chessboard_numbers[j_modified]
                    _add_edge(chess_graph, vert_1, vert_2)
    return chess_graph


def find_path_bfs(graph, start_vertex, end_vertex):
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
    knight_graph = prepare_knight_graph()
    print(find_path_bfs(knight_graph, 'd4', 'f7'))
    print(find_path_bfs(knight_graph, 'a8', 'h1'))
