from code_challenges.merge_sort.merge_sort import merge_sort

def test_merge_sort():
    theList = [8, 4, 23, 42, 16, 15]
    actual = merge_sort(theList)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected