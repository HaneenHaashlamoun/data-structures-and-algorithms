class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class Queue:
    def __init__(self):
        """
        It creates an empty Queue when instantiated
        """
        self.front=None
        self.rear=None

    def enqueue(self,value):
        """
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        """
        new_node=Node(value)
        if not self.rear :
            self.rear=new_node
            self.front=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    def dequeue(self):
        """
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        """
        if self.isEmpty():
            raise Exception("Empty queue")
        else:
            temp=self.front
            self.front=self.front.next
            temp.next=None
        if self.front==None: # if size of queue is 1
            self.rear=None
        return temp.value
    def isEmpty(self):
        """
        Arguments: none
        Returns: Boolean indicating whether or not the queue is empty
        """
        if self.front is None and self.rear is None:
            return True
        else:
            return False
    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        """
        if self.isEmpty():
            raise Exception("Empty queue")
        else:
            return self .front.value


class TreeNode:
    """
    Class to instanitation node
    Attribute :data , children as list
    """
    def __init__(self,data=None,children=[]):
        self.data = data
        self.children = children


class karyTree:
    def __init__(self,root=None):
        self.root = root

    def breadth_first(self):
        """
        breadth first search function use level search that returns list of values that Contains
        input -> tree
        return -> list
        """
        queue =Queue()
        queue_output = []


        queue.enqueue(self.root)

        while not queue.isEmpty():
            front=queue.dequeue()

            for child in front.children:
                queue.enqueue(child)
            queue_output.append(front.data)
        return queue_output

def fizz_buzz(number):

    if not number % 15:
        return "FizzBuzz"
    elif not  number%3 :
        return "Fizz"
    elif not number%5:
        return "Buzz"
    else:
        return str(number)

def fizz_buzz_tree(k_ary_tree : karyTree):
    """
    function takes k-ary tree and modifies values whether or not the value of each node is divisible by 3 -> "Fizz", 5 -> "Buzz",or both ("FizzBuzz").
    Arguments: k-ary tree
    Return: new k-ary tree
    """
    if not k_ary_tree.root:
        return 'Tree is empty'

    queue = Queue()
    queue.enqueue(k_ary_tree.root)

    while not queue.isEmpty():
        front=queue.dequeue()
        front.data = fizz_buzz(front.data)
        for child in front.children:
            queue.enqueue(child)

    return k_ary_tree