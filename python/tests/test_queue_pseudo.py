from code_challenges.stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
import pytest

def test_enqueues_queue():
    expected = 5
    queue = PseudoQueue()
    queue.enqueue(5)
    actual = queue.first_stack.top.data
    assert expected == actual

def test_dequeue_queue(queue):
    expected = 20
    actual = queue.first_stack.top.data
    assert expected == actual

def test_dequeue_empty_queue(queue):
    with pytest.raises(Exception, match="empty Queue !"):
        queue.dequeue()


# ********** fixture ***********
@pytest.fixture
def queue():
    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)

    return queue