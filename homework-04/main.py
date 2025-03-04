
from src.my_array import MyArray


a = MyArray(10)

a.insert(2)
a.insert(4)
a.insert("foo")
a.insert("bar")
a.insert(44)
a.insert(55)
a.insert(12.34)
a.insert(0)
a.insert("baz")
a.insert(17)

print("Array containing", len(a), "items")
a.traverse()

print("Search for 12 returns", a.search(12))

print("Search for 12.34 returns", a.search(12.34))

print("Deleting 0 returns", a.delete(0))
print("Deleting 17 returns", a.delete(17))

print("Setting item at index 3 to 33")
a.set(3, 33)

print("Array after deletion has", len(a), "items")
a.traverse()