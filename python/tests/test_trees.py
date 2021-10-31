"""
Tests for Binary Tree
"""

from code_challenges.trees.trees import BinaryTree , Node, Binary_Search_Tree


def test_bfs():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node('A')
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["A", "B", "C", "D"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs passed")


def test_bfs_2():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["1", "2", "3", "4"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs_2 passed")


def test_pre_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["1", "2", "4", "3"]
    # set actual to return value of pre_order call
    actual = tree.pre_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_pre_order_ passed")


def test_post_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["4", "2", "3", "1"]
    # set actual to return value of post_order call
    actual = tree.post_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_post_order_ passed")


def test_in_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["4", "2", "1", "3"]
    # set actual to return value of in_order call
    actual = tree.in_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_in_order_ passed")



############ Code Callenge 16 ######################

def test_contains():
    tree = Binary_Search_Tree()    
    items = [10,54,8,4,2]
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

test_bfs()
test_bfs_2()
test_pre_order()
test_in_order()
test_post_order()