# Course: CS 261
# Author: Vincent Rastello
# Assignment: 6
# Description: Hash table based undirected graph with unweighted edges


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph, validates vertex not already in graph.
        """
        if v not in self.adj_list:
            self.adj_list[v] = []
        
    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph, validates:
        * That given vertices are not equal
        * That given vertices exist--if not adds them
        * That given edge doesn't exist already
        """
        if u != v:
            if v not in self.adj_list or u not in self.adj_list:
                if u not in self.adj_list:
                    self.add_vertex(u)
                if v not in self.adj_list:
                    self.add_vertex(v)

            if u not in self.adj_list[v]:
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        if v in self.adj_list and u in self.adj_list:
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
                self.adj_list[v].remove(u)

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges, validates vertex exists
        """
        if v in self.adj_list:
            del self.adj_list[v]
            for vertex in self.adj_list:
                if v in self.adj_list[vertex]:
                    self.adj_list[vertex].remove(v)

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        vertices = []
        for vertex in self.adj_list:
            vertices.append(vertex)
        return vertices

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (from first to last)
        """
        edge_list = []
        vertices = self.get_vertices()
        for vertex in range(len(vertices) - 1):
            # removes first vertex
            v = vertices[0]
            del vertices[0]
            # then adds edge for each vertex found in adjacency list
            for vi in self.adj_list[v]:
                # if vertex not in vertices list then that edge has already been added
                if vi in vertices:
                    edge_list.append((v, vi))

        return edge_list

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        # checks for empty list
        if not path:
            return True
        # checks for single vertex
        if len(path) == 1:
            if path[0] not in self.adj_list:
                return False
        # validates vertex exists
        # checks for presence of next vertex in path in current vertex's adjacency list
        for i in range(len(path) - 1):
            v = path[i]
            vi = path[i + 1]
            if v not in self.adj_list:
                return False
            if vi not in self.adj_list[v]:
                return False

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        # initialize variables
        visited = []
        stack = []
        # if v_start not in graph, return empty list
        if v_start in self.adj_list:
            # push to stack
            stack.append(v_start)
            while len(stack) > 0:
                v = stack.pop()
                # append popped stack vertex to visited list if not in list
                if v not in visited:
                    visited.append(v)
                    # if end reached return list
                    if v == v_end:
                        return visited
                    # add direct successors to stack in reverse order by popping
                    # produces in order visits during search
                    successors = sorted(self.adj_list[v])
                    while len(successors) > 0:
                        stack.append(successors.pop())

        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        # initialize variables
        visited = []
        queue = []
        # if v_start not in graph, return empty list
        if v_start in self.adj_list:
            # enqueue v_start
            queue.append(v_start)
            while len(queue) > 0:
                v = queue[0]
                del queue[0]
                # append dequeued vertex to visited list
                if v not in visited:
                    visited.append(v)
                    # if end reached return list
                    if v == v_end:
                        return visited
                    # add direct successors to stack in order
                    # produces in order visits during search
                    successors = sorted(self.adj_list[v])
                    for i in range(len(successors)):
                        # check if successors are in visited list
                        if successors[i] not in visited:
                            queue.append(successors[i])

        return visited

    def count_connected_components(self):
        """
        Return number of connected components in the graph
        """

        # initialize variables
        vertices = self.get_vertices()
        count = 0
        # if no vertices return 0
        while len(vertices) > 0:
            count += 1
            start = vertices[0]
            # check for all connected using breadth first search
            connected = self.bfs(start)
            total_v = set(vertices)
            sub_v = set(connected)
            # get left-over unconnected graph using set difference
            # run again on unconnected portion of graph
            vertices = list(total_v.difference(sub_v))

        return count

    def dfs_rec(self, v, cycle_found, pred_node, marked):
        """recursive dfs function for finding cycle"""
        if cycle_found[0]:
            return
        marked[v] = True
        for vi in self.adj_list[v]:
            if marked[vi] and vi != pred_node:
                cycle_found[0] = True
                return
            if not marked[vi]:
                self.dfs_rec(vi, cycle_found, v, marked)

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        marked = {v: False for v in self.adj_list}
        cycle_found = [False]

        for v in self.adj_list:
            if not marked[v]:
                self.dfs_rec(v, cycle_found, v, marked)
            if cycle_found[0]:
                break
        return cycle_found[0]

if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
