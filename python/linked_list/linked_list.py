class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        new_node = Node(value)
        current = self.head
        if current == None:
            current = new_node
        else:
            while current.next != None:
                current = current.next
        current.next = new_node

    def insert(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        """
        Create function includes :
         - define the head, which is the current variable
         - Return T/F if value is in the linked list or not
        """
        current = self.head
        while (current):
            if current.value == value:
                return True
            current = current.next
        return False

    def insert_before(self, value, new_value):
        node = Node(new_value)
        current_node = self.head
        if current_node.value == value:
            node.next = self.head
            self.head = node
        else:
            while current_node.next:
                if current_node.next.value == value:
                    node.next = current_node.next
                    current_node.next = node
                    break
                current_node = current_node.next

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def __str__(self):
        """
        to string method to print out the linked list in "{ a } -> { b } -> { c } -> NULL" format        
        
        """
        current =self.head
        result =''
        while current is not None:
            result += "{ " + str(current.value)+ " } -> "
            current = current.next
        result += 'NULL'
        return result

# test
# if __name__ == "__main__":
#     pass
