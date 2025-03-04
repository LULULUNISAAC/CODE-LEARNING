import pytest
from src.my_array import MyArray



# Constructor Tests

def test_it_should_create_an_empty_array_on_instantiation():
    a = MyArray(10)
    a.insert(1)

    assert len(a) == 1

def test_it_should_have_items_set_to_0():
    a = MyArray(10)

    assert len(a) == 0

# len tests
def test_it_should_return_the_number_of_items_in_the_array():
    a = MyArray(10)
    a._MyArray__nItems = 5

    assert len(a) == 5

# get Tests

## It should get in index
def test_it_should_return_value_by_index():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    a._MyArray__nItems = 10

    assert a.get(0) == 1
    assert a.get(9) == 10
    assert a.get(4) == 5


## should return None if less than 0
def test_it_should_return_None_if_out_of_bounds_lower():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    assert a.get(-1) == None

## should return None if greater than 
def test_it_should_return_None_if_out_of_bounds_upper():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    assert a.get(10) == None

# set Tests
def test_it_should_set_value_at_index():
    a = MyArray(10)
    a._MyArray__nItems = 1
    a.set(0, 1)

    assert a._MyArray__a[0] == 1

def test_it_should_not_set_value_if_out_of_bounds_lower():
    a = MyArray(2)
    a._MyArray__nItems = 1
    a.set(-1,1)

    assert a._MyArray__a == [None, None]

def test_it_should_not_set_value_if_out_of_bounds_upper():
    a = MyArray(2)
    a._MyArray__nItems = 1
    a.set(1,1)

    assert a._MyArray__a == [None, None]

# Insert Tests
def test_it_should_insert_at_end_end_of_array():
    a = MyArray(10)
    a.insert(1)
    a.insert(2)

    assert a._MyArray__a[0] == 1
    assert a._MyArray__a[1] == 2
    assert a._MyArray__nItems == 2

# Find tests
def test_it_should_find_the_index_of_an_item():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    a._MyArray__nItems = 10

    assert a.find(1) == 0
    assert a.find(10) == 9
    assert a.find(5) == 4

def test_it_should_return_negative_one_if_item_not_found():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    a._MyArray__nItems = 10

    # search for value 11
    assert a.find(11) == -1

# Search tests
def test_it_should_search_for_an_item():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    a._MyArray__nItems = 10

    assert a.search(1) == 1
    assert a.search(10) == 10
    assert a.search(5) == 5

def test_it_should_return_None_if_item_not_found():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    a._MyArray__nItems = 10

    # search for value 11
    assert a.search(11) == None

# Test Delete
def test_it_should_delete_an_item():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    a._MyArray__nItems = 10

    res = a.delete(5)

    assert res == True
    assert a._MyArray__nItems == 9

    # when deleting an item, the items after the deleted item
    # are shifted to the left, the last item is not deleted
    # but it cannot be accessed through the class methods
    # because the nItems is decremented
    assert a._MyArray__a == [1,2,3,4,6,7,8,9,10,10]

def test_it_should_return_false_if_item_not_found():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    a._MyArray__nItems = 10

    res = a.delete(11)

    assert res == False
    assert a._MyArray__nItems == 10
    assert a._MyArray__a == [1,2,3,4,5,6,7,8,9,10]

# Traverse tests
def test_it_should_traverse_the_array():
    a = MyArray(10)
    a._MyArray__a = [1,2,3,4,5,6,7,8,9,10]
    a._MyArray__nItems = 10

    res = []
    a.traverse(lambda x: res.append(x))

    assert res == [1,2,3,4,5,6,7,8,9,10]