from code_challenges.selection_sort.selection_sort import selection_sort

def test_selection_sort():
    theList = [8, 4, 23, 42, 16, 15]
    actual = selection_sort(theList)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected