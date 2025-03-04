from .Array import Array

class StackArray():
    def __init__(self, max):
        self.__stackArray = Array(max)

    def __str__(self):
        return str(self.__stackArray)
    
    def __len__(self):
        return len(self.__stackArray)
    
    # def push(self, item):


    # def pop(self):


    # def peek(self):


    # def isEmpty(self):


    # def isFull(self):