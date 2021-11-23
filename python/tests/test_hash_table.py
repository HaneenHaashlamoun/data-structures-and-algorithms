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


################### CodeChallange31 ########################

def test_repeated_word():
	assert HashTable().repeated_word("Once upon a time, there was a brave princess who...") == 'a'
	assert HashTable().repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == 'it'
	assert HashTable().repeated_word("very sunny and cloudy but sunny") == 'sunny'
