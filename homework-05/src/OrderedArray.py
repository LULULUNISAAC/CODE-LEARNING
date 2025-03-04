"""OrderedArray 

This module contains the OrderedArray class. Which maintain an ordered array of items.
"""


class OrderedArray(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    
    # Returns the length of the Ordered Array
    # Usage:
    # a = OrderedArray(10)
    # print(len(a))
    def __len__(self):
        return self.__nItems
    
    # Creates a string of the contents of the Array
    # Usage:
    # a = OrderedArray(10)
    # a.insert(1)
    # a.insert(2)
    # print(a)
    # [ 1, 2 ]
    # or
    # s = str(a)
    # print(s)
    # [ 1, 2 ]
    def __str__(self):
        result = "[ "
        for i in range(self.__nItems):
            if i == self.__nItems - 1:
                result += f"{self.__a[i]} "
            else:
                result += f"{self.__a[i]}, "

        result += "]"
        return result

    def get(self, n):
        # if the index is within the bounds of the array
        if 0 <= n and n < self.__nItems:
            # return the item at the index
            return self.__a[n]
        else:
            return None
    
    # Uses binary search to find the index of an item
    def find(self, item):
        # These 2 variable are run the binary search
        # from the left side of the array
        # and from the right side of the array
        lo = 0
        hi = self.__nItems - 1

        # while the tracking variables have not met in the "middle"
        while lo <= hi:
            # get the middle point between the left and right
            mid = (lo + hi) // 2

            # if the middle point is the item, return the index
            if self.__a[mid] == item:
                return mid
            # if the item in the middle is less than the item being searched for
            # update the tracking variables to look to the right of the middle
            elif self.__a[mid] < item:
                lo = mid + 1
            # otherwise,
            # update the tracking variables to look to the left of the middle
            else:
                hi = mid - 1
        # if the item is not found, return the index where the item should be inserted
        return lo

    def insert(self, item):
        # if the array storage is full
        # throw an error
        if self.__nItems >= len(self.__a):
            # Solve Problem 1 here
            # comment out the following line, and implement your solution
            raise Exception("Array Overflow")
            
        # find the index where the item should be inserted
        index = self.find(item)

        # shift all the elements to the right
        for j in range(self.__nItems, index, -1):
            self.__a[j] = self.__a[j-1]

        # insert the item
        self.__a[index] = item
        # increment the number of items in the array
        self.__nItems += 1

    def search(self, item):
        index = self.find(item)

        # the find() method does not differentitate between
        # finding an item, or finding insertion point for a
        # new item in the ordered array
        # 
        # the following if statement checks to see if the index
        # that find() return is with in bounds of the array
        # and it actually contains what is being searched for
        if index < self.__nItems and self.__a[index] == item:
            return self.__a[index]
        
        return None
        # if item is not found, return None
    
    def delete(self, item):
        # find the index of the item
        j = self.find(item)

        # if the index is within the bounds of the array
        # and the item is found
        if j < self.__nItems and self.__a[j] == item:
            # decrement the size of the array
            self.__nItems -= 1

            # shift all the elements to the left
            for k in range(j, self.__nItems):
                self.__a[k] = self.__a[k+1]
            return True
        
        return False
    
    # Solve problem 1 here
    # def merge(self, other):
    def merge(self, other):
        for i in range(other.__nItems):
            self.insert(other.__a[i])

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