# from hash_table.hash_table import HashTable
# from trees.trees import BinaryTree,Node

class Node_hash:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node_hash(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        index = self.__hash(key)
        if not self.__buckets[index]:
            self.__buckets[index] = LinkedList()
        my_value = [key, value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
        index = self.__hash(key)
        if self.__buckets[index]:
            linked_list = self.__buckets[index]
            current = linked_list.head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        return None

    def contains(self, key):
        index = self.__hash(key)
        return True if self.__buckets[index] else False

########################################################################


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def _init_(self):
        self.root = None

    def pre_order(self):
        list_of_items = []

        def walk(node):
            if node:
                list_of_items.append(node.data)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

######################################################


# def common_values(tree_one: BinaryTree, tree_two: BinaryTree):
#     if tree_one.root == None or tree_two.root == None:
#         return None
#     hashtable = HashTable()
#     result_values = []
#     def walk_one(node):
#         if node:
#             if hashtable.add(str(node.data),node.data):
#                 print(hashtable)
#                 walk_one(node.left)
#                 walk_one(node.right)
#     walk_one(tree_one.root)
#     def walk_two(node):
#         if node:
#             if hashtable.contains(str(node.data)):
#                 result_values.append(node.data)
#                 walk_two(node.left)
#                 walk_two(node.right)
#     walk_two(tree_two.root)
#     return result_values


def tree_intersection(tree1:BinaryTree, tree2:BinaryTree):
    if tree1.root == None or tree2.root == None:
        return None
    arr=[]
    hash = HashTable()
    def walk(node:Node):
        if node:
            hash.add(str(node.data),None)
        if node.left:
            walk(node.left)
        if node.right:
            walk(node.right)
    walk(tree1.root)
    def walk2(node:Node):
        if node:
            if hash.contains(str(node.data)):
                arr.append(node.data)
        if node.left:
            walk2(node.left)
        if node.right:
            walk2(node.right)
        return arr
    return walk2(tree2.root)


# one2 = Node(42)
# two2 = Node(100)
# three2 = Node(150)
# four2 = Node(200)
# five2 = Node(250)
# six2 = Node(300)
# seven2 = Node(350)
# eight2 = Node(400)
# tree2 = BinaryTree()
# tree2.root = one2
# one2.left = two2
# one2.right = three2
# two2.left = four2
# two2.right = five2
# three2.left = six2
# three2.right = seven2
# seven2.right = eight2


# one = Node(42)
# two = Node(50)
# three = Node(70)
# four = Node(100)
# five = Node(250)
# six = Node(300)
# seven = Node(350)
# eight = Node(400)
# tree = BinaryTree()
# tree.root = one
# one.left = two
# one.right = three
# two.left = four
# two.right = five
# three.left = six
# three.right = seven
# seven.right = eight

# print(tree_intersection(tree, tree2))
