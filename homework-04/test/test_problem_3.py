from src.my_array import MyArray


# removeDupes Tests
def test_it_should_remove_dupes():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,5,6,7,8,9]
    a._MyArray__nItems = 10

    a.removeDupes()

    assert a._MyArray__a == [1,2,3,4,5,6,7,8,9,9]
    assert a._MyArray__nItems == 9

def test_it_should_remove_dupes_multiples():
    a = MyArray(10)
    a._MyArray__a = [1,1,1,2,2,2,3,4,5,6,7,8]
    a._MyArray__nItems = 12

    a.removeDupes()

    # there are 4 duplicates removed
    assert a._MyArray__a == [1,2,3,4,5,6,7,8,8,8,8,8]
    assert a._MyArray__nItems == 8