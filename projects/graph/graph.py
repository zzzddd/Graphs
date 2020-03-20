

# class Graph:
# ​
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
# ​
#     def add_vertex(self, vertex_id):
#         """
#         Add a vertex to the graph.
#         """
#         self.vertices[vertex_id] = set()
# ​
#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise ValueError("vertex does not exist")
# ​
#     def add_undirected_edge(self, v1, v2):
#         """
#         Add an undirected edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#             self.vertices[v2].add(v1)
#         else:
#             raise ValueError("vertex does not exist")
# ​
#     def get_neighbors(self, vertex_id):
#         """
#         Get all neighbors (edges) of a vertex.
#         """
#         if vertex_id in self.vertices:
#             return self.vertices[vertex_id]
#         else:
#             raise ValueError("vertex does not exist")
# ​
#     def bft(self, starting_vertex):
#         """
#         Print each vertex in breadth-first order
#         beginning from starting_vertex.
#         """
#         # Create a queue
#         q = Queue()
#         # Enqueue the starting vertex
#         q.enqueue(starting_vertex)
#         # Create a set to store visited vertices
#         visited = set()
#         # While the queue is not empty...
#         while q.size() > 0:
#             # Dequeue the first vertex
#             v = q.dequeue()
#             # Check if it's been visited
#             # If it hasn't been visited...
#             if v not in visited:
#                 # Mark it as visited
#                 print(v)
#                 visited.add(v)
#                 # Enqueue all it's neighbors
#                 for neighbor in self.get_neighbors(v):
#                     q.enqueue(neighbor)
# ​
# ​
#     def dft(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """
#         # Create a stack
#         s = Stack()
#         # Push the starting vertex
#         s.push(starting_vertex)
#         # Create a set to store visited vertices
#         visited = set()
#         # While the stack is not empty...
#         while s.size() > 0:
#             # Pop the first vertex
#             v = s.pop()
#             # Check if it's been visited
#             # If it hasn't been visited...
#             if v not in visited:
#                 # Mark it as visited
#                 print(v)
#                 visited.add(v)
#                 # Push all it's neighbors onto the stack
#                 for neighbor in self.get_neighbors(v):
                        #  s.push(neighbor)





"""
Simple graph implementation
"""
from util import Stack, Queue  

# These may come in handy

class Graph:
    # kkkkk

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO
        if vertex_id in self.vertices:
            print('WARNING: That vertex already exists!')
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size() > 0:
            current_node = queue.dequeue()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                for neighbor in self.get_neighbors(current_node):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO

        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            current_node = stack.pop()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                for neighbor in self.get_neighbors(current_node):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        visited = visited or set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

#         ​
#     def dft_recursive(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
# ​
#         This should be done using recursion.
#         """
#         # Check if the node has been visited
#         # If not...
#             # Mark it as visited
#             # Call dft_recursive on each neighbor
# ​
#     def bfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """
#         # Create a queue
#         # Enqueue A PATH TO the starting vertex
#         # Create a set to store visited vertices
#         # While the queue is not empty...
#             # Dequeue the first PATH
#             # GRAB THE VERTEX FROM THE END OF THE PATH
#             # Check if it's been visited
#             # If it hasn't been visited...
#                 # Mark it as visited
#                 # CHECK IF IT'S THE TARGET
#                     # IF SO, RETURN THE PATH
#                 # Enqueue A PATH TO all it's neighbors
#                     # MAKE A COPY OF THE PATH

#         pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO

        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:
            path_to_current_node = queue.dequeue()
            current_node = path_to_current_node[-1]
            if current_node == destination_vertex:
                return path_to_current_node
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.get_neighbors(current_node):
                    path_to_neighbor = [*path_to_current_node, neighbor]
                    queue.enqueue(path_to_neighbor)
        print('Vertex not found')

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO

        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            path_to_current_node = stack.pop()
            current_node = path_to_current_node[-1]
            if current_node == destination_vertex:
                return path_to_current_node
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.get_neighbors(current_node):
                    path_to_neighbor = [*path_to_current_node, neighbor]
                    stack.push(path_to_neighbor)
        print('Vertex not found')

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # pass  # TODO

        path_to_current_node = path or [starting_vertex]
        visited = visited or set()
        current_node = path_to_current_node[-1]
        if current_node == destination_vertex:
            return path_to_current_node
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in self.get_neighbors(current_node):
                path_to_neighbor = [*path_to_current_node, neighbor]
                updated_path = self.dfs_recursive(
                    neighbor, destination_vertex, path_to_neighbor, visited)
                if updated_path:
                    return updated_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
