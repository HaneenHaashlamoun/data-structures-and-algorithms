from collections import deque
from typing import List


class Vertex:
    def __init__(self, value):
        self.value = value


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

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
        self.adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self.adjacency_list[v] = []
        return v

    def size(self):
        return len(self.adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(edge)
        # print(graph.adjacency_list[start_vertex.value])

    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action=(lambda vertex: None)):
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
            return neighbors

############# Code Challenge 37 ##########################


def business_trip(graph: Graph, cities_list: List):
    if len(cities_list) > 1:
        # to check if the city exist in the graph
        if (cities_list[0] in list(graph.get_nodes())) and (cities_list[1] in list(graph.get_nodes())):
            print('Valid Cities')
            neighbors = graph.get_neighbors(cities_list[1])
            if neighbors:
                for neighbor in neighbors:
                    if cities_list[0] == neighbor.vertex:
                        return (True, neighbor.weight)
                    else:
                        return(False, '$0')

        #     result = (bool, str)
        #         # for city in range(len(cities_list)):
        #         for neighbor in graph.get_neighbors(cities_list[1]):
        #             if cities_list[0] == neighbor.vertex:
        #                 result = (True, neighbor.weight)
        #             elif cities_list[1] == neighbor.vertex:
        #                 result = (True, neighbor.weight)
        #             else:
        #                 result = (False, '$0')
        #         return result
        #     else:
        #         return('NO City')
        else:
            return('NO City')


graph = Graph()
test = 'test'
# Cities (nodes / vertex)
pandora = graph.add_node('pandora')
metroville = graph.add_node('Metroville')
arendelle = graph.add_node('Arendelle')
narnia = graph.add_node('Narnia')
naboo = graph.add_node('Naboo')
monstroplolis = graph.add_node('Monstroplolis')

# Edges
graph.add_edge(pandora, metroville, 82)
graph.add_edge(pandora, arendelle, 150)
graph.add_edge(metroville, arendelle, 99)
graph.add_edge(metroville, monstroplolis, 105)
graph.add_edge(metroville, naboo, 26)
graph.add_edge(metroville, narnia, 37)
graph.add_edge(arendelle, monstroplolis, 42)
graph.add_edge(monstroplolis, naboo, 73)
graph.add_edge(naboo, narnia, 250)

# graph.add_edge(metroville, pandora, 82)
# graph.add_edge(arendelle, pandora, 150)
# graph.add_edge(arendelle, metroville, 99)
# graph.add_edge(monstroplolis, metroville, 105)
# graph.add_edge(naboo, metroville, 26)
# graph.add_edge(narnia, metroville, 37)
# graph.add_edge(monstroplolis, arendelle, 42)
# graph.add_edge(naboo, monstroplolis, 73)
# graph.add_edge(narnia, naboo, 250)

path = [metroville, pandora]
print(business_trip(graph, path))
