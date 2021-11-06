from stack_and_queue import Stack
import pytest


def test_push_stack(stack):
    expected = 10
    actual = stack.top.data
    assert expected == actual

def test_pop_from_stack(stack):
    expected = 10
    actual = stack.pop()
    assert expected == actual

def test_pop_from_empty():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()

def test_peek_from_empty():
    with pytest.raises(Exception):
        stack = Stack()
        stack.peek()

def test_peek_from_not_empty_stack(stack):
    expected = 10
    actual = stack.peek()
    assert expected == actual

def test_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True




# ********** fixture ***********
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(2)
    stack.push(6)
    stack.push(4)
    stack.push(8)
    stack.push(10)

    return stack