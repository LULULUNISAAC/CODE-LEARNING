from src.my_array import MyArray


# deteMaxNum Tests
def test_it_should_delete_max_num():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,10,6,7,8,9]
    a._MyArray__nItems = 10

    assert a.deleteMaxNum() == 10
    assert a._MyArray__a == [1,2,3,4,5,6,7,8,9,9]
    assert a._MyArray__nItems == 9

def test_it_should_delete_max_num_empty():
    a = MyArray(10)
    a._MyArray__nItems = 0

    assert a.deleteMaxNum() == None

def test_it_should_delete_max_num_no_number():
    a = MyArray(10)
    a._MyArray__a = ["s", [1,2], (1,2)]
    a._MyArray__nItems = 3

    assert a.deleteMaxNum() == None

def test_it_should_delete_max_num_multiple():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,10,10,7,8,9]
    a._MyArray__nItems = 10

    assert a.deleteMaxNum() == 10
    assert a._MyArray__a == [1,2,3,4,5,7,8,9,9,9]
    assert a._MyArray__nItems == 8