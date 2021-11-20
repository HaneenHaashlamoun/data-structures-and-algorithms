from code_challenges.quick_sort.quick_sort import quick_sort

def test_quick_sort():
    list = [8, 4, 23, 42, 16, 15]
    actual = quick_sort(list, 0, len(list)-1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected
