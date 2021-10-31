from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_validate_bracket_1():
    actual = validate_brackets('{}(){}')
    expected = True
    assert actual == expected


def test_validate_bracket_2():
    actual = validate_brackets('()[[Extra]]')
    expected = True
    assert actual == expected


def test_validate_bracket_3():
    actual = validate_brackets('[({[({})]})]')
    expected = True
    assert actual == expected


def test_validate_bracket_4():
    actual = validate_brackets('{(})')
    expected = False
    assert actual == expected
