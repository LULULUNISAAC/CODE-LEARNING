# CODE-LEARNING

HW4:
Manual testing

Add code into main.py and run python main.py to manually run code.

Running tests

Run tests

python -m pytest
Generating Coverage Reports

python -m coverage run -m pytest
View Coverage Reports

python -m coverage report --show-missing
Problem 1

In the MyArray class, add a method called getMaxNum() that returns the value of the highest number in the array, or None if the array has no numbers. An array can hold many different types of objects, not just numbers, for example, an array of strings. You can use the expression isinstance(x,(int,float)) to test if x is a number. Add code to main.py to exercise this method. You should try it on a variety of data types in an array.

Problem 2

In the MyArray class, add a method called deleteMaxNum(), which returns the highest value in the array, and deletes matching numbers in the array, in the case that the highest number has duplicates.

Problem 3

Write a removeDupes() method for the MyArray class that removes any duplicate entries in the array. That is, if three items with the value 'bar' appear in the array, removeDupes() should remove two of them. Array size should decrease by the number of duplicates removed. This function does not return a value
