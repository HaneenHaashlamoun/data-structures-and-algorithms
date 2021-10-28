import pytest
from linked_list.linked_list import Linked_list, Node, zip_Lists


def test_import():
    assert Linked_list


def test_instantiate_empty_list():
    linked_list = Linked_list()
    assert linked_list


def test_insert():
    linked_list = Linked_list()
    linked_list.insert("first")
    actual = linked_list.head.value
    assert actual == "first"


def test_head():
    node1 = Node(5)
    linked_list = Linked_list()
    linked_list.head = node1
    assert linked_list.head == node1


def test_insert_multiple_nodes():
    node1 = Node(1)
    linked_list = Linked_list()
    linked_list.head = node1
    linked_list.insert(4)
    assert linked_list.head.value == 4
    linked_list.insert(6)
    assert linked_list.head.value == 6
    linked_list.insert(9)
    assert linked_list.head.value == 9


def test_linked_contain():
    expected = True
    ll = Linked_list()
    testx = ll.insert(2)
    actual = ll.includes(2)
    assert expected == actual


def test_to_string():
    expected = "{ a } -> { b } -> { c } -> NULL"
    ll = Linked_list()
    node1 = ll.insert("c")
    node2 = ll.insert("b")
    node3 = ll.insert("a")
    actual = ll.__str__()
    assert actual == expected

####################### TEST:  Linked_List_Insertion #######################

def test_append_one():
    expected = "{ 2 } -> { 5 } -> NULL"
    ll = Linked_list()
    node1 = ll.insert(2)
    node2 = ll.append(5)
    actual = str(ll)
    assert actual == expected


def test_insert_before():
    expected = "{ 3 } -> { 5 } -> { 1 } -> NULL"
    ll = Linked_list()
    node1 = ll.insert(1)
    node1 = ll.insert(3)
    node2 = ll.insert_before(1, 5)
    actual = str(ll)
    assert actual == expected

# def test_inseartAfter():
#     List=Linked_list()
#     List.insert_after(1,11)
#     List.insert_after(2,22)
#     List.insert_after(3,33)
#     actual=List.__str__()
#     expected='{1}-> {11}-> {3}-> {33}-> {5}-> NULL'
#     assert actual == expected

def test_insert_after():
  def test_inseartAfter():
    List=Linked_list()
    List.insertAfter(1,11)
    List.insertAfter(2,22)
    List.insertAfter(3,33)
    actual=List.__str__()
    expected='{1}-> {11}-> {2}-> {22}-> {3}-> {33}-> {4}-> {5}-> NULL'
    assert actual == expected
  

def test_k_index_out_of_range():
    excepted='out of range'
    ll=Linked_list()
    ll.insert(3)
    ll.insert(2)
    ll.insert(2)
    ll.append(13)
    actual=ll.kth_from_end(5)
    assert excepted==actual

def test_k_and_length_the_same():     
    excepted='out of range'     
    ll=Linked_list()
    ll.insert(3)
    ll.insert(2)
    ll.insert(2)
    ll.append(13)
    actual=ll.kth_from_end(4)
    assert excepted==actual

def test_k_negative():     
    excepted='negative value not allowed'     
    ll=Linked_list()
    ll.insert(3)
    ll.insert(2)
    ll.insert(2)
    ll.append(13)
    actual=ll.kth_from_end(-4)    
    assert excepted==actual


####################### TEST:  Linked List ZIP #######################

def test_empty_lists():     
    excepted='empty list'     
    first_ll =Linked_list()
    second_ll =Linked_list()
    actual= zip_Lists(first_ll,second_ll)
    #Assert
    assert excepted==actual


def test_first_list_empty():     
    excepted="{ 5 } -> { 3 } -> { 2 } -> NULL"     
    first_ll =Linked_list()
    second_ll =Linked_list()
    second_ll.insert(5)
    second_ll.append(3)
    second_ll.append(2)
    actual= zip_Lists(first_ll,second_ll)    
    assert excepted==actual

def test_second_list_empty():
    excepted="{ 5 } -> { 3 } -> { 2 } -> NULL"     
    first_ll =Linked_list()
    second_ll =Linked_list()
    first_ll.insert(5)
    first_ll.append(3)
    first_ll.append(2)
    actual= zip_Lists(first_ll,second_ll)    
    assert excepted==actual

def test_zipped_List():    
    excepted="{ 1 } -> { 5 } -> { 7 } -> { 3 } -> { 4 } -> { 2 } -> NULL"     
    first_ll =Linked_list()
    first_ll.insert(1)
    first_ll.append(7)
    first_ll.append(4)
    #second list
    second_ll =Linked_list()
    second_ll.insert(5)
    second_ll.append(3)
    second_ll.append(2)
    print(str(second_ll))
    actual= zip_Lists(first_ll,second_ll)
    assert excepted==actual    