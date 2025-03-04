
class Stack(object):
    def __init__(self, max):
        self.__stackList = [None] * max
        self.__top = -1 # Stack is empty

    # Add an item to the top of the stack
    # No safety checks to see if stack is full
    def push(self, item):
        # Advance the pointer
        self.__top += 1
        # store item
        self.__stackList[self.__top] = item

    # Remove the item from the top of the stack
    def pop(self):
        # get the last item inserted
        top = self.__stackList[self.__top]
        # Remove reference for item
        self.__stackList[self.__top] = None
        # Decrease the pointer, and the size of the stack
        self.__top -= 1
        # return the item at the top
        return top
    
    # Return item at the top of the stack
    def peek(self):
        # if the stack is not empty
        if not self.isEmpty():
            # return item at the top of the stack
            return self.__stackList[self.__top]
        
    # Check to see if the stack is empty
    def isEmpty(self):
        return self.__top < 0
    
    # Check if stack is full
    def isFull(self):
        return self.__top >= len(self.__stackList) - 1
    
    # Return items in the stack
    def __len__(self):
        return self.__top + 1
    
    # Print out contents of the stack
    def __str__(self):
        if self.__top == -1:
            return "[ ]"
        result = "[ "
        for i in range(self.__top+1):
            if i == self.__top:
                result += f"{self.__stackList[i]} "
            else:
                result += f"{self.__stackList[i]}, "

        result += "]"
        return result
