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
            raise Exception("You can't pop from Empty Stack !")
        else :
           temp = self.top
           self.top = self.top.next
           temp.next = None
        return temp.data

    def peek(self):
        if not self.top :
            raise Exception("Empty Stack !")
        else :
            return self.top.data

    def is_empty(self):
        if not self.top:
            return True
        return False

class PseudoQueue:
    """
    class with Queue data structure
    enqueue() => add node to the queue
    dequeue () => remove node from the queue    
    peek() => view the value of the front Node in the queue
    is_empty() => return => True if the queue empty
    """
    def __init__(self) :
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self ,value):
        self.first_stack.push(value)

    def dequeue(self):
        if self.first_stack.is_empty:
            raise Exception("empty Queue !")
        #remove nodes (values) from first stack to second
        while not self.first_stack.is_empty:
            popped_value = self.first_stack.pop()
            self.second_stack.push(popped_value)

        #the value we wanted to remove
        removed_value = self.second_stack.pop()

        #push back nodes (values) to first stack from second)
        while not self.second_stack.is_empty:
            popped_value = self.second_stack.pop()
            self.first_stack.push(popped_value)
        
        return removed_value
