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
        current = self.head
        while current is not None:
            if current.value == value:
                break
            current = current.next
        if current is None:
            raise Exception(" the value does not exist ")
        else:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node
        # new_node = Node(new_value)
        # current = self.head
        # while current:
        #     if current.value == value:
        #         new_node.next = current.next
        #         current.next = new_node
        #         break
        #     current = current.next

    def __str__(self):
        """
        to string method to print out the linked list in "{ a } -> { b } -> { c } -> NULL" format        

        """
        current = self.head
        result = ''
        while current is not None:
            result += "{ " + str(current.value) + " } -> "
            current = current.next
        result += 'NULL'
        return result

    def kth_from_end(self, k):
        current = self.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        current = self.head
        if k < 0:
            return 'negative value not allowed'
        elif k >= length:
            return 'out of range'
        value = length-k-1
        for i in range(length):
            if i == value:
                return current.data
            current = current.next


def zip_Lists(list1, list2):    
    first_list = list1.head
    second_list = list2.head

    if not first_list and not second_list:
        return 'empty list'
    elif not first_list:
        return str(list2)
    elif not second_list:
        return str(list1)

    hold_node = ''
    while first_list and second_list:
        if second_list:
            hold_node = first_list.next
            first_list.next = second_list
            first_list = hold_node

        if first_list:
            hold_node = second_list.next
            second_list.next = first_list
            second_list = hold_node
    return str(list1)


# test
# if __name__ == "__main__":
#     pass
