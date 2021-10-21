from stack_and_queue import Queue
import pytest

def test_enqueues_queue():
    expected = 6
    queue = Queue()
    queue.enqueue(6)
    actual = queue.rear.data
    assert expected == actual

def test_dequeue_queue(queue):
    expected = 1
    actual = queue.dequeue()
    assert expected == actual

def test_peek_queue(queue):
    expected = 1
    actual = queue.peek()
    assert expected == actual

def test_peek_from_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()
        actual = queue.peek()



# ********** fixture ***********
@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    return queue