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
    
    def get_node(self, value):
        # self.get_nodes()
        for vertex in self.get_nodes() :
            if vertex.value == value:
                return vertex

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


def business_trip(graph: Graph, cities_list: list):
    if len(cities_list) > 1:
        # to check if the city exist in the graph
        if not (cities_list[0] in [vertex.value for vertex in graph.get_nodes()]) or not (cities_list[1] in [vertex.value for vertex in graph.get_nodes()]):
            return('NO City')
        node_vertex = graph.get_node(cities_list[0])
        neighbors = graph.get_neighbors(node_vertex)
        if neighbors:# check if the neighbors are in each others lis 
            for neighbor in neighbors:
                if cities_list[1] == neighbor.vertex.value:
                    return (True, f'${neighbor.weight}')                
        return(False, '$0')
        
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


graph.add_edge(metroville, pandora, 82)
graph.add_edge(arendelle, pandora, 150)
graph.add_edge(arendelle, metroville, 99)
graph.add_edge(monstroplolis, metroville, 105)
graph.add_edge(naboo, metroville, 26)
graph.add_edge(narnia, metroville, 37)
graph.add_edge(monstroplolis, arendelle, 42)
graph.add_edge(naboo, monstroplolis, 73)
graph.add_edge(narnia, naboo, 250)



path = [metroville, pandora]
print(business_trip(graph, path))

# def business_trip1(graph, trip):
#     cost = 0
#     m = {}
#     for i in range(len(trip)):
#         for city in graph.get_neighbors(trip[0]):
#             m[city.vertex.value] = f'{city.weight}'
#     cost=m.get(trip[1].value)
#     if cost is not None:
#         return f'There is a Road from {trip[0].value} to {trip[1].value} and it will cost {cost}$'
#     else :
#         return f'There is No Road'

# def business_trip2(graph,cities):
#     j = True
#     cost = 0
#     for i in range(len(cities)-1):
#         for city in graph.get_neighbors(cities[i]):
#             if cities[i+1]==city[0]:
#                 cost+=city[1]
#                 break
#             else:
#                 j=False
#     if j==False:
#             cost=0
#     return j, f'${cost}'





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