import pytest
from code_challenges.graphs.graph import Graph, Vertex, business_trip


def test_add_node():
    graph = Graph()
    expected = "test"
    actual = graph.add_node('test').value
    assert actual == expected


def test_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected


def test_size():
    graph = Graph()
    graph.add_node('spam')
    expected = 1
    actual = graph.size()
    assert actual == expected


def test_add_edge_interloper_start():
    graph = Graph()
    start = Vertex('start')
    end = graph.add_node('end')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():
    graph = Graph()
    end = Vertex('end')
    start = graph.add_node('start')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_get_nodes():
    graph = Graph()
    banana = graph.add_node('banana')
    apple = graph.add_node('apple')
    loner = Vertex('loner')
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected

def test_get_node():
    graph = Graph()
    banana = graph.add_node('banana')    
    expected = banana
    actual = graph.get_node('banana')
    assert actual == expected

def test_get_node_fails():
    graph = Graph()
    banana = graph.add_node('banana')    
    expected = None
    actual = graph.get_node('apple')
    assert actual == expected

def test_get_neighbors():
    graph = Graph()
    banana = graph.add_node('banana')
    apple = graph.add_node('apple')
    graph.add_edge(apple, banana, 44)
    neighbors = graph.get_neighbors(apple)
    assert len(neighbors) == 1
    neighbor_edge = neighbors[0]
    assert neighbor_edge.vertex.value == 'banana'
    assert neighbor_edge.weight == 44

def test_get_two_neighbors():
    graph = Graph()
    banana = graph.add_node('banana')
    apple = graph.add_node('apple')
    cherry = graph.add_node('cherry')
    # mango = graph.add_node('mango')
    graph.add_edge(apple, banana, 44)
    graph.add_edge(apple, cherry, 22)
    neighbors = graph.get_neighbors(apple)
    assert len(neighbors) == 2
    neighbor_edge = neighbors[0]
    assert neighbor_edge.vertex.value == 'banana'
    assert neighbor_edge.weight == 44
    neighbor_edge = neighbors[1]
    assert neighbor_edge.vertex.value == 'cherry'
    assert neighbor_edge.weight == 22

def test_business_trip_both_city_not_present():
    graph = Graph()
    path = ['metroville','test']
    excepted = 'NO City'
    actual = business_trip(graph,path)
    assert excepted == actual


def test_business_trip_one_city_not_present():
    graph = Graph()
    graph.add_node('pandora')
    path = ['pandora','test']
    excepted = 'NO City'
    actual = business_trip(graph,path)
    assert excepted == actual


def test_business_trip_cities_dont_have_egde():
    graph = Graph()
    graph.add_node('pandora')
    graph.add_node('Metroville')
    path = ['pandora','Metroville']
    excepted = False,'$0'
    actual = business_trip(graph,path)
    assert excepted == actual

def test_business_trip_cities_do_have_egde():
    graph = Graph()
    pandora = graph.add_node('pandora')
    metroville = graph.add_node('Metroville')
    graph.add_edge(pandora, metroville, 82)
    path = ['pandora','Metroville']
    excepted = True,'$82'
    actual = business_trip(graph,path)
    assert excepted == actual

def test_business_trip_one_city():
    graph = Graph()
    path = ['metroville']
    excepted = None
    actual = business_trip(graph,path)
    assert excepted == actual

def test_business_trip_two_paths():
    """
    It should pass if both paths exist with correct weights
    """
    graph = Graph()
    pandora = graph.add_node('pandora')
    metroville = graph.add_node('Metroville')
    arendelle = graph.add_node('arendelle')
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(pandora, arendelle, 150)
    path2 = ['pandora','arendelle']
    path = ['pandora','Metroville']
    excepted = True,'$82'
    excepted2 = True,'$150'
    actual = business_trip(graph,path)
    actual2 = business_trip(graph,path2)
    assert excepted == actual
    assert excepted2 == actual2

def test_business_trip_two_paths_fail():
    graph = Graph()
    pandora = graph.add_node('pandora')
    metroville = graph.add_node('Metroville')
    arendelle = graph.add_node('arendelle')
    naboo = graph.add_node('naboo')
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(pandora, arendelle, 150)
    path = ['pandora','naboo']
    excepted = False,'$0'
    actual = business_trip(graph,path)
    assert excepted == actual
    
    # Cities (nodes / vertex)
    # pandora = graph.add_node('pandora')
    # metroville = graph.add_node('Metroville')
    # arendelle = graph.add_node('Arendelle')
    # narnia = graph.add_node('Narnia')
    # naboo = graph.add_node('Naboo')
    # monstroplolis = graph.add_node('Monstroplolis')

    # Edges
    # graph.add_edge(pandora, metroville, 82)
    # graph.add_edge(pandora, arendelle, 150)
    # graph.add_edge(metroville, arendelle, 99)
    # graph.add_edge(metroville, monstroplolis, 105)
    # graph.add_edge(metroville, naboo, 26)
    # graph.add_edge(metroville, narnia, 37)
    # graph.add_edge(arendelle, monstroplolis, 42)
    # graph.add_edge(monstroplolis, naboo, 73)
    # graph.add_edge(naboo, narnia, 250)

    

    
