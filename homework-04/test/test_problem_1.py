from src.my_array import MyArray

def test_it_should_get_max_num_int():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    a._MyArray__nItems = 10

    assert a.getMaxNum() == 10

def test_it_should_get_max_num_float():
    a = MyArray(10)
    a._MyArray__a = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1]
    a._MyArray__nItems = 10

    assert a.getMaxNum() == 10.1

def test_it_should_get_max_num_mixed():
    a = MyArray(10)
    a._MyArray__a = [1,"s",(1,2),5, 10]
    a._MyArray__nItems = 5

    assert a.getMaxNum() == 10

def test_it_should_get_max_num_empty(): 
    a = MyArray(10)
    a._MyArray__nItems = 0

    assert a.getMaxNum() == None

def test_it_should_get_max_num_no_number(): 
    a = MyArray(10)
    a._MyArray__a = ["s", [1,2], (1,2)]
    a._MyArray__nItems = 3

    assert a.getMaxNum() == None

def test_it_should_get_max_num_empty_array(): 
    a = MyArray(0)

    assert a.getMaxNum() == None