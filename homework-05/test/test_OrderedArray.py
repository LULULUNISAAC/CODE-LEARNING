from src.OrderedArray import OrderedArray

# Test the OrderedArray class

# Test the constructor
def test_it_should_initialize_with_an_initial_size_of_10():
    a = OrderedArray(10)
    assert len(a._OrderedArray__a) == 10
    assert a._OrderedArray__nItems == 0

# Test the __len__ method
def test_it_should_return_the_number_of_items_in_the_array():
    a = OrderedArray(10)
    a._OrderedArray__nItems = 3
    assert len(a) == 3

# Test the __str__ method
def test_it_should_return_a_string_representation_of_the_array():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert str(a) == "[ 1, 2, 3 ]"

def test_it_should_return_an_empty_string_representation_of_an_empty_array():
    a = OrderedArray(10)
    assert str(a) == "[ ]"

# Test the get method
def test_it_should_return_the_item_at_the_specified_index():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert a.get(1) == 2

def test_it_should_return_none_if_the_index_is_out_of_range():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert a.get(3) == None

# Test the find method
# item is in the mid
def test_it_should_return_the_index_of_the_item_1():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert a.find(2) == 1

# item is at the end
def test_it_should_return_the_index_of_the_item_2():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert a.find(3) == 2

# item is at the beginning
def test_it_should_return_the_index_of_the_item_3():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert a.find(1) == 0

def test_it_should_return_the_index_of_insertion_point_if_not_found():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 4]
    a._OrderedArray__nItems = 3
    assert a.find(3) == 2

# Test the insert method
def test_it_should_insert_an_item_at_the_end_of_the_array():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3, None, None, None, None, None, None, None]
    a._OrderedArray__nItems = 3
    a.insert(4)
    assert a._OrderedArray__a == [1, 2, 3, 4, None, None, None, None, None, None]
    assert a._OrderedArray__nItems == 4

def test_it_should_insert_an_item_at_the_beginning_of_the_array():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3, None, None, None, None, None, None, None]
    a._OrderedArray__nItems = 3
    a.insert(0)
    assert a._OrderedArray__a == [0, 1, 2, 3, None, None, None, None, None, None]
    assert a._OrderedArray__nItems == 4

def test_it_should_insert_an_item_in_the_middle_of_the_array():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 4, None, None, None, None, None, None, None]
    a._OrderedArray__nItems = 3
    a.insert(3)
    assert a._OrderedArray__a == [1, 2, 3, 4, None, None, None, None, None, None]
    assert a._OrderedArray__nItems == 4

# Test the search method
def test_it_should_return_the_item_if_found():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert a.search(2) == 2

def test_it_should_return_None_if_not_found():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert a.search(4) == None

# test the delete method
def test_it_should_delete_an_item():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert a.delete(1) == True
    assert a._OrderedArray__a == [2, 3, 3]
    assert a._OrderedArray__nItems == 2

def test_it_should_return_false_if_item_not_found():
    a = OrderedArray(10)
    a._OrderedArray__a = [1, 2, 3]
    a._OrderedArray__nItems = 3
    assert a.delete(4) == False
    assert a._OrderedArray__a == [1, 2, 3]
    assert a._OrderedArray__nItems == 3

