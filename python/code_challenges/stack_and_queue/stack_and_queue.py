class Node:
  """
  A class Initializing Node
  """

  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_


class Stack:
    """
    class will implement the Stack data structure
    top = top of the last entered node in stack.
    push() => add node to stack
    pop() => remove node from stack
    peek() => view the top value
    is_empty() => return  => True if the stack is empty
    """
    def __init__(self) :
       self.top = None

    def push(self ,value):
        node=Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top :
            raise Exception("You can't pop from Empty Stack !!!")
        else :
           temp = self.top
           self.top = self.top.next
           temp.next = None
        return temp.data

    def peek(self):
        if not self.top :
            raise Exception("Empty Stack !!!")
        else :
            return self.top.data

    def is_empty(self):
        if not self.top:
            return True
        return False

class Queue:
    """
    class with Queue data structure
    enqueue() => add node to the queue
    dequeue () => remove node from the queue    
    peek() => view the value of the front Node in the queue
    is_empty() => return => True if the queue empty
    """
    def __init__(self) :
       self.front = None
       self.rear = None

    def enqueue(self ,value):
        node = Node(value)
        if not self.rear:
           self.front = node
           self.rear= node
        else :
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front :
            raise Exception("not allowed to dequeue ... empty Queue")
        else :
            temp = self.front
            self.front = self.front.next
            temp.next = None

        return temp.data

    def peek(self):
        if not self.front :
            raise Exception("empty Queue")
        else :
            return self.front.data

    def is_empty(self):
        if not self.front:
            return True
        return False