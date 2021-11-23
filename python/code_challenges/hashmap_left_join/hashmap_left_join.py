class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        self.head = Node(value, self.head)


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
        my_value = [key,value]
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



def left_join(table1:HashTable, table2:HashTable)  :
    main_list = []

    for table1.__buckets[index].value[0] in table1:
        inner_list = []
        if table2.contains(key):
            inner_list.append(key)
            inner_list.append(key.value)
            inner_list.append(table2.key.value)
        else :
            inner_list.append(key)
            inner_list.append(key.value)
            inner_list.append('None')
        if inner_list.length > 0:
            main_list.append(inner_list)
    return main_list
