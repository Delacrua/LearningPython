"""
The Depth-First Search is a recursive algorithm that uses the concept of backtracking. It involves thorough
searches of all the nodes by going ahead if potential, else by backtracking. Here, the word backtrack means once you
are moving forward and there are not any more nodes along the present path, you progress backward on an equivalent
path to seek out nodes to traverse. All the nodes are progressing to be visited on the current path until all the
unvisited nodes are traversed after which subsequent paths are going to be selected.
Usage:
Depth-first searches are used in:
- mapping routes and counting vertexes in graphs,
- finding spanning trees,
- cycle detection in graphs,
- analyzing networks, for example, testing if a graph is bipartite,
- topological sorting,
- scheduling problems,
- solving puzzles with only one solution, such as a maze or a sudoku puzzle.
Depth-first search is often used as a subroutine in network flow algorithms such as the Ford-Fulkerson algorithm or
in matching algorithms in graph theory such as the Hopcroft–Karp algorithm.
"""
# first set up a graph adjacency list
graph_adj = {
    '0': ['1', '14', '18'],
    '1': ['2', '15', '14', '0'],
    '2': ['1', '3', '17'],
    '3': ['4', '7', '2'],
    '4': ['5', '6', '3'],
    '5': ['4'],
    '6': ['4'],
    '7': ['3', '8', '9'],
    '8': ['7'],
    '9': ['7', '10'],
    '10': ['9', '11', '12'],
    '11': ['10'],
    '12': ['10', '13', '14'],
    '13': ['12'],
    '14': ['16', '15', '1', '0', '12'],
    '15': ['14', '1', '2'],
    '16': ['14'],
    '17': ['2'],
    '18': ['0'],
}


def dfs(vertex, graph, visited_vertexes=None):
    """
    The implementation of Depth-First Search recurrent algorithm
    :param vertex: current vertex
    :param graph: searched graph in a form of a graph adjacency list
    :param visited_vertexes: set of visited vertexes
    :return: None
    """
    visited_vertexes = visited_vertexes or set()
    if vertex not in visited_vertexes:
        visited_vertexes.add(vertex)
        for neighbour in graph[vertex]:
            dfs(neighbour, graph, visited_vertexes)
        print(f'All neighbours visited for this vertex: {vertex}')  # after recursive calls have been completed


if __name__ == '__main__':
    print("Following is the Depth-First Search")
    dfs('0', graph_adj)
