from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter

def test_enqueue():
    actual = []
    animal = AnimalShelter()
    animal.enqueue('bull', 'dog')
    actual += [animal.dog.peek()]
    animal.enqueue('soker', 'cat')
    actual += [animal.cat.peek()]
    excepted = ['bull', 'soker']
    assert actual == excepted

def test_enqueue_fail():
    animal = AnimalShelter()
    actual = animal.enqueue('pummy', 'hamster')
    excepted = 'Invalid enter cat/dog only'
    assert actual == excepted

def test_dequeue():
    animal = AnimalShelter()
    animal.enqueue('bull', 'dog')
    animal.enqueue('soker', 'cat')
    actual = [animal.dequeue('dog'), animal.dequeue('cat')]
    excepted = ['bull', 'soker']
    assert actual == excepted

def test_dequeue_fail():
    animal = AnimalShelter()
    actual = animal.dequeue('rabbit')
    excepted = 'Invalid enter cat/dog only'
    assert actual == excepted