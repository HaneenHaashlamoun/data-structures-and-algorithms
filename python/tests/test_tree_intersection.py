import pytest
from code_challenges.trees.trees import BinaryTree,Node
from code_challenges.tree_intersection.tree_intersection import tree_intersection

def test_return_common_values():
    # tree_one = BinaryTree()
    assert tree_intersection(tree, tree2) == [42, 100, 250, 300, 350, 400]

def test_no_common_values():
    assert tree_intersection(tree3, tree4) == []


one2 = Node(42)
two2 = Node(100)
three2 = Node(150)
four2 = Node(200)
five2 = Node(250)
six2 = Node(300)
seven2 = Node(350)
eight2 = Node(400)
tree2 = BinaryTree()
tree2.root = one2
one2.left = two2
one2.right = three2
two2.left = four2
two2.right = five2
three2.left = six2
three2.right = seven2
seven2.right = eight2


one = Node(42)
two = Node(50)
three = Node(70)
four = Node(100)
five = Node(250)
six = Node(300)
seven = Node(350)
eight = Node(400)
tree = BinaryTree()
tree.root = one
one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
seven.right = eight




one3 = Node(1)
two3 = Node(2)
three3 = Node(3)
four3 = Node(4)
five3 = Node(5)
six3 = Node(6)
seven3 = Node(7)
eight3 = Node(8)
tree3 = BinaryTree()
tree3.root = one3
one3.left = two3
one3.right = three3
two3.left = four3
two3.right = five3
three3.left = six3
three3.right = seven3
seven3.right = eight3


one4 = Node(9)
two4 = Node(10)
three4 = Node(11)
four4 = Node(12)
five4 = Node(13)
six4 = Node(14)
seven4 = Node(15)
eight4 = Node(16)
tree4 = BinaryTree()
tree4.root = one4
one4.left = two4
one4.right = three4
two4.left = four4
two4.right = five4
three4.left = six4
three4.right = seven4
seven4.right = eight4
