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
        self.size = size
        self.buckets = [None] * size

    def hash(self, key):
        return sum([ord(char) for char in key]) * 7 % self.size

    def add(self, key, value):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = LinkedList()
        my_value = [key, value]
        self.buckets[index].insert(my_value)

    def get(self, key):
        index = self.hash(key)
        if self.buckets[index]:
            linked_list = self.buckets[index]
            current = linked_list.head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        return None

    def contains(self, key):
        index = self.hash(key)
        return True if self.buckets[index] else False


def left_join(hash1: HashTable, hash2: HashTable):
    arr = []
    if len(hash1.buckets) < 0 or len(hash2.buckets) < 0:
        return 'hash table is empty'
    for i in range(len(hash1.buckets)):
        if hash1.buckets[i]:
            if hash2.contains(hash1.buckets[i].head.value[0]):
                arr.append([hash1.buckets[i].head.value[0],
                           hash1.buckets[i].head.value[1], hash2.buckets[i].head.value[1]])
            else:
                arr.append([hash1.buckets[i].head.value[0],
                           hash1.buckets[i].head.value[1], None])
    return arr


# hashtable1 = HashTable()
# # hashtable1.add("foo","ff")
# # hashtable1.add("moo","m")
# # hashtable1.add("soo","ss")

# hashtable2 = HashTable()
# # hashtable1.add("fo","ff")
# # hashtable1.add("moo","mmm")
# # hashtable1.add("soo","sss")

# print(left_join(hashtable2, hashtable1))
