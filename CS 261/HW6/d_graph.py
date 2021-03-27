# Course: CS261 - Data Structures
# Author: Vincent Rastello
# Assignment: 6
# Description: Matrix based directed graph with weighted edges

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Adds vertex to directed graph, increments vertex count, increments matrix sizes
        """
        new_v = []
        self.v_count += 1
        for _ in range(self.v_count - 1):
            new_v.append(0)
        self.adj_matrix.append(new_v)
        for v in range(self.v_count):
            self.adj_matrix[v].append(0)

        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds edge between two vertices, if nodes invalid does nothing
        """
        if src != dst:
            if 0 <= src < self.v_count and 0 <= dst < self.v_count and weight > 0:
                self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes edge between two vertices, validates vertices are not same and are in bounds
        """
        if src != dst:
            if 0 <= src < self.v_count and 0 <= dst < self.v_count:
                self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Returns list of vertices in graph
        """
        vertices = []
        for i in range(self.v_count):
            vertices.append(i)
        return vertices

    def get_edges(self) -> []:
        """
        Returns list of tuples containing source, destination and weight of each edge
        """
        edges = []
        for i in range(self.v_count):
            for j in range(self.v_count):
                if self.adj_matrix[i][j] != 0:
                    edges.append((i, j, self.adj_matrix[i][j]))

        return edges

    def is_valid_path(self, path: [], i=0) -> bool:
        """
        Returns true or false when given path in list form
        """
        if i + 1 < len(path):

            if self.adj_matrix[path[i]][path[i + 1]] == 0:
                return False
            else:
                return self.is_valid_path(path, i + 1)

        return True

    def helper_dfs(self, v_start, v_end, visited):
        """recursive helper for dfs search"""
        if v_end:
            if v_start == v_end:
                return visited
        for v in range(self.v_count):
            next_node = self.adj_matrix[v_start][v]
            if next_node != 0 and v not in visited:
                visited.append(v)
                self.helper_dfs(v, v_end, visited)

        return visited

    def dfs(self, v_start, v_end=None) -> []:
        """
        Main function for recursive dfs search, uses helper function
        """
        visited = []
        if 0 > v_start >= self.v_count:
            return visited

        visited.append(v_start)
        return self.helper_dfs(v_start, v_end, visited)

    def helper_bfs(self, v_start, v_end, visited):
        """recursive helper for bfs search"""
        if v_end:
            if v_start == v_end:
                return visited
        queue = []
        for v in range(self.v_count):
            next_node = self.adj_matrix[v_start][v]
            if next_node != 0 and v not in visited:
                queue.append(v)
        for vi in queue:
            visited.append(vi)
        for vi in queue:
            self.helper_bfs(vi, v_end, visited)

        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        Main function for recursive bfs search, uses helper function
        """
        visited = []
        if 0 > v_start >= self.v_count:
            return visited

        visited.append(v_start)
        return self.helper_bfs(v_start, v_end, visited)

    def next_node_queue(self, v_start):
        """creates queue of successor vertices in graph in numerical order"""
        queue = []
        for v in range(self.v_count):
            if self.adj_matrix[v_start][v] != 0:
                queue.append(v)
        return queue

    def helper_has_cycle(self, v, visited, marked):
        """Recursive helper function for detect cycle"""
        visited[v] = True
        marked[v] = True
        successors = self.next_node_queue(v)
        # recursion for all successors
        # if any successor is visited and
        # in current marked recursion it's cyclic
        for node in successors:
            if not visited[node]:
                if self.helper_has_cycle(node, visited, marked):
                    return True
            elif marked[node]:
                return True

        # remove marks from recursion if not cycle found
        marked[v] = False
        return False

    def has_cycle(self):
        """
        Detects cycle in graph returns boolean, uses recursive helper function
        """
        visited = {}
        marked = {}
        for v in self.get_vertices():
            marked[v] = False
            visited[v] = False
        if self.v_count < 3:
            return False

        for node in range(self.v_count):
            if not visited[node]:
                if self.helper_has_cycle(node, visited, marked):
                    return True
        return False

    def dijkstra(self, src: int) -> []:
        """
        Implementation of Dijkstra's algorithm
        Returns list, indexes represent vertices, values are weights
        List is shortest path from given source to all vertices in graph
        """
        v_map = []
        for _ in range(self.v_count):
            v_map.append(float('inf'))
        p_queue = []
        heapq.heappush(p_queue, (0, src))
        while len(p_queue) > 0:
            vertex = heapq.heappop(p_queue)
            v = vertex[1]
            d = vertex[0]
            if v_map[v] == float('inf'):
                v_map[v] = d
                for successor in self.next_node_queue(v):
                    ds = self.adj_matrix[v][successor]
                    dt = ds + d
                    heapq.heappush(p_queue, (dt, successor))

        return v_map


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7), (-1, 23, -1), (1, 23, -1)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)
    for src, dst, weight in edges:
        g.remove_edge(src, dst)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
