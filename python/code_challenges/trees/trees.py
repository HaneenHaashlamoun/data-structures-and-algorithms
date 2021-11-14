"""
This Module defines a Node and a Binary Tree
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)


class BinaryTree:

    def _init_(self):
        self.root = None

    def bfs(self):
        breadth = Queue()
        breadth.enqueue(self.root)
        list_of_items = []
        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.data]

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_of_items

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

    def in_order(self):
        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                list_of_items.append(node.data)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

    def post_order(self):
        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
                list_of_items.append(node.data)

        walk(self.root)
        return list_of_items

    def get_max(self):
        if not self.root:
            raise Exception("empty")
        self.max_val = self.root.data

        def max_node(node):
            if node.data > self.max_val:
                self.max_val = node.data
            if node.left:
                max_node(node.left)
            if node.right:
                max_node(node.right)
            return self.max_val
        return max_node(self.root)

    def breadth_first(self):
      queue = Queue()
      queue.enqueue(self.root)
      node_val = []
      while queue.peek():
          front = queue.dequeue()
          node_val += [front.data]
          if front.left:
              queue.enqueue(front.left)
          if front.right:
              queue.enqueue(front.right)
      return node_val

    # def tree_fizz_buzz(tree):
    #     fizz_buzz_list = []
    #     if tree.root:
    #         node= tree.root
    #         def walk(node):
    #             if node.data % 3 == 0 and node.data % 5 == 0:
    #                 node.data = "FizzBuzz"
    #             elif node.data % 3 == 0:
    #                 node.data = "Fizz"
    #             elif node.data % 5 == 0:
    #                 node.data = "Buzz"
    #             else:
    #                 node.data = str(node.data)            
    #             if node.left:
    #                 walk(node.left)
    #             if node.right:
    #                 walk(node.right) 
    #             fizz_buzz_list.append(node.data)                   
    #         walk(node)            
    #         return fizz_buzz_list


class Binary_Search_Tree(BinaryTree):
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            def walk(root):
                if data <= root.data:
                    if root.left:
                        walk(root.left)
                    else:
                        root.left = Node(data)
                elif data >= root.data:
                    if root.right:
                        walk(root.right)
                    else:
                        root.right = Node(data)
            return walk(self.root)

    def contains(self, data):
        if self.root == None:
            return False

        def walk(root):
            if root:
                if data == root.data:
                    return True

                elif root.data != data:

                    if walk(root.left):
                        return True

                    if walk(root.right):
                        return True

                return False
        return walk(self.root)
