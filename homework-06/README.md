# homework-06

## Prep Work

- Turn off any autocomplete provider by AI, for example, ChatGPT or Copilot

## Problem 1

Revise the `Stack` class in `SimpleStack.py` to throw exceptions if something is pushed on to a full stack. Write a test program in `problem-01.py` that demonstrates that the revised class properly accepts items up to the original stack size and then throws an exception when another item is pushed

## Problem 2

Create a program in `problem-02.py` that determines whether an input string is a palindrome or not, ignoring whitespaces, digits, punctuation, and the case letters. Palindromes are words or phrases that have the same letter sequence forward or backward. Use the `Stack` class implementation in `SimpleStack.py`

## Problem 3

Implement the methods of a stack in `SimpleStackArray.py`, but instead of the class managing its own storage, use the `Array` class. In `problem-03.py` there are sample calls for the `StackArray` class that should work when the work is complete.

You'll have to update the `Array` class to be able to remove the an item and a given index.

As and example, 

```python
class Array(object):
    # existing methods here
    
    # create new method in Array class
    def remove(self, index):
        # your code here
```