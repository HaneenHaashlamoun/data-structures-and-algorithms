import pytest
from code_challenges.hash_table.hash_table import HashTable


@pytest.fixture
def hashtable():
	return HashTable()

def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected

def test_hash_word(hashtable):
	expected = 376
	actual =  hashtable._HashTable__hash("dd")
	assert actual == expected

"""
"a"
ord("d") = 100
100 * 7 = 700
700 % 1024 = 700

-----------------
"dd"
200
200 * 7 = 1400
1400 % 1024 = 376
"""

def test_adding_a_key_and_value_to_hashtable():
  hash_table = HashTable()
  hash_table.add('haneen','32')
  assert hash_table.get('haneen') == '32'

def test_key_returns_the_value_stored():
  hash_table = HashTable()
  hash_table.add('haneen','32')
  assert hash_table.get('haneen') == '32'

def test_key_not_exist():
  hash_table = HashTable()
  assert hash_table.get('test') == None

def test_handle_a_collision():
  hash_table = HashTable()
  hash_table.add('haneen','32')
  hash_table.add('haneen','33')
  print(hash_table.contains('haneen'))
  print(hash_table.contains('haneen'))

def test_bucket_in_hashtable_have_collision():
  hash_table = HashTable()
  hash_table.add('haneen','32')
  hash_table.add('hanin','30')
  assert hash_table.get('haneen') == '32'
  assert hash_table.get('hanin') == '30'
