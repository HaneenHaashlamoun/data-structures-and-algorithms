import pytest
from code_challenges.trees.trees import BinaryTree, Node, Binary_Search_Tree


def test_bfs():
    tree = BinaryTree()
    a_node = Node('A')
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["A", "B", "C", "D"]
    actual = tree.bfs()
    assert actual == expected
    print("test_bfs passed")


def test_bfs_2():
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["1", "2", "3", "4"]
    actual = tree.bfs()
    assert actual == expected
    print("test_bfs_2 passed")


def test_pre_order():
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["1", "2", "4", "3"]
    actual = tree.pre_order()
    assert actual == expected
    print("test_pre_order_ passed")


def test_post_order():
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["4", "2", "3", "1"]
    actual = tree.post_order()
    assert actual == expected
    print("test_post_order_ passed")


def test_in_order():
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["4", "2", "1", "3"]
    actual = tree.in_order()
    assert actual == expected
    print("test_in_order_ passed")


############ Code Callenge 16 ######################

def test_contains():
    tree = Binary_Search_Tree()
    items = [10, 54, 8, 4, 2]
    for item in items:
        tree.add(item)
    assert tree.contains(10) == True
    assert tree.contains(54) == True
    assert tree.contains(8) == True
    assert tree.contains(4) == True
    assert tree.contains(2) == True
    assert tree.contains(1) == False


def test_Add_to_root():
    tree = Binary_Search_Tree()
    tree.add('5')
    assert tree.root.data == '5'

############ code_challenge 16 ############


def test_get_max():
    expected = 4
    tree = Binary_Search_Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    actual = tree.get_max()
    assert actual == expected


def test_max_empty_tree():
    with pytest.raises(Exception):
        tree = BinaryTree()
        actual = tree.get_max()


def test_max_one_Node():
    expected = 8
    tree = Binary_Search_Tree()
    tree.add(8)
    actual = tree.get_max()
    assert actual == expected

############ code_challenge 17 ############


def test_breadth_first():
    tree = BinaryTree()
    node1 = Node('a')
    node2 = Node('b')
    node3 = Node('c')
    node4 = Node('d')
    node5 = Node('e')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    tree.root = node1
    expected = ['a', 'b', 'c', 'd', 'e']
    actual = tree.breadth_first()
    assert actual == expected

############### code_challenge 18 ################


def test_tree_fizz_buzz():
    tree = BinaryTree()
    node1 = Node(5)
    node2 = Node(15)
    node3 = Node(3)
    node4 = Node(1)
    node5 = Node(20)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    tree.root = node1
    actual = tree.tree_fizz_buzz()
    excepted = ['1', 'Buzz', 'FizzBuzz', 'Fizz', 'Buzz']
    assert actual == excepted
