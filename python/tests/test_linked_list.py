import pytest
from linked_list.linked_list import Linked_list, Node


def test_import():
    assert Linked_list

def test_instantiate_empty_list():
    linked_list=Linked_list()
    assert linked_list


def test_insert():
    linked_list = Linked_list()
    linked_list.insert("first")
    actual = linked_list.head.value
    assert actual == "first"

def test_head():
    node1=Node(5)
    linked_list = Linked_list()
    linked_list.head=node1
    assert linked_list.head == node1

def test_insert_multiple_nodes():
    node1=Node(1)
    linked_list = Linked_list()
    linked_list.head=node1
    linked_list.insert(4)
    assert linked_list.head.value == 4
    linked_list.insert(6)
    assert linked_list.head.value == 6
    linked_list.insert(9)
    assert linked_list.head.value == 9

