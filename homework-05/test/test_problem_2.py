from src.OrderedArray import OrderedArray

# Problem 2 tests
# test merge method
def test_it_should_merge_two_arrays_1():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 3, 5]
    a._OrderedArray__nItems = 3

    b = OrderedArray(10)
    b._OrderedArray__a = [2, 4, 6]
    b._OrderedArray__nItems = 3

    a.merge(b)
    assert a._OrderedArray__a == [1, 2, 3, 4, 5, 6]
    assert a._OrderedArray__nItems == 6
    assert len(a) == 6

def test_it_should_merge_two_arrays_2():
    a = OrderedArray(10)
    a._OrderedArray__a = [2, 4, 6]
    a._OrderedArray__nItems = 3

    b = OrderedArray(10)
    b._OrderedArray__a = [1, 3, 5]
    b._OrderedArray__nItems = 3

    a.merge(b)
    assert a._OrderedArray__a == [1, 2, 3, 4, 5, 6]
    assert a._OrderedArray__nItems == 6
    assert len(a) == 6