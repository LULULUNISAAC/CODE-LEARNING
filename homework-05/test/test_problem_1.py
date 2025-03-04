from src.OrderedArray import OrderedArray

# Problem 1 tests
# Test increase storage for OrderedArray
def test_it_should_increase_storage_when_array_is_full():
    a = OrderedArray(2)
    a.insert(1)
    a.insert(2)
    a.insert(3)
    assert len(a._OrderedArray__a) == 4
    assert str(a) == "[ 1, 2, 3 ]"

# This test is expected to pass with out any changes to the
# OrderedArray class for Problem 1
# It should still pass after you solve Problem 1
def test_it_should_not_increase_storage_when_array_is_not_full():
    a = OrderedArray(10)
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    assert len(a._OrderedArray__a) == 10