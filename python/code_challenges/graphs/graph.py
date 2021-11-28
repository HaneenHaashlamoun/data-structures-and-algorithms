from collections import deque


class Vertex:
    def __init__(self, value):
        self.value = value


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendLeft(value)

    def dequeue(self):
        self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Stack:
    def __init__(self):
        self.dq = deque()

    def push(self, value):
        self.dq.append(value)

    def pop(self):
        self.dq.pop()


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.__adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):        
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):        
        return self.__adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action=(lambda vertex: None)):
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)

            neighbors = self.get_neigbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
