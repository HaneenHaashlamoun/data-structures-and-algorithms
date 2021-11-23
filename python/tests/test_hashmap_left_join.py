from code_challenges.hashmap_left_join.hashmap_left_join import left_join
from code_challenges.hashmap_left_join.hashmap_left_join import HashTable

def test_left_join():
    hashtable1 = HashTable()
    hashtable1.add("foo","ff")
    hashtable1.add("moo","m")
    hashtable1.add("soo","ss")

    hashtable2 = HashTable()
    hashtable1.add("fo","ff")
    hashtable1.add("moo","mmm")
    hashtable1.add("soo","sss")

    actual = left_join(hashtable1, hashtable2)
    excepted = [['foo', 'ff', None], ['moo', 'mmm', None], ['soo', 'sss', None], ['fo', 'ff', None]]
    assert excepted == actual


def test_left_join_backwards():
    hashtable1 = HashTable()
    hashtable1.add("foo","ff")
    hashtable1.add("moo","m")
    hashtable1.add("soo","ss")

    hashtable2 = HashTable()
    hashtable1.add("fo","ff")
    hashtable1.add("moo","mmm")
    hashtable1.add("soo","sss")

    actual = left_join(hashtable2, hashtable1)
    excepted = []
    assert excepted == actual

def test_left_join_empty_hashes():
    hashtable1 = HashTable()
    hashtable2 = HashTable()
    actual = left_join(hashtable2, hashtable1)
    excepted = []
    assert excepted == actual
