# homework-05

## Prep Work

- Turn off any autocomplete provider by AI, for example, ChatGPT or Copilot
- You can add code to `main.py` to manually test your code changes

## Manual testing

Add code into `main.py` and run `python main.py` to manually run code.

## Running tests

**Run tests**

```
python -m pytest
```

**Generating Coverage Reports**

```
python -m coverage run -m pytest
```

**View Coverage Reports**

```
python -m coverage report --show-missing
```

## Problem 1

Modify the `OrderedArray` class, so that, if the array is full (the array size is the same size as the python list used for storage), a new storage list is created that is **twice** the size of to current list size, the contents of the old (smaller) list are copied over to the new list, and the new item is inserted into the list.

The whole logic to double the storage can live in the `insert()` function. Currently, there is logic there to throw an error when the Array storage is full, replace the error with the ability to add more storage.

## Problem 2

Add a `merge()` method to the `OrderedArray` class. It merges an Ordered array into the objects existing ordered array.

There is a function definition already started in the `OrderedArray` class at the end of the file

**Example Usage**

``` python
a1 = OrderedArray(5)
a1.insert(34)
a1.insert(23)
a1.insert(54)

print(len(a1)) # 3
# a1 contains the ordered data [23,34,54]

a2 = OrderedArray(5)
a2.insert(64)
a2.insert(13)
a2.insert(29)

print(len(a2)) # 3
# a2 contains the ordered data [13,29,64]

a1.merge(a2)
print(len(a1)) # 6
# a1 contains the ordered data [13,23,29,24,54,64]
```

