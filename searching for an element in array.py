from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])


def searchingAnElement(array, value):
    for i in array:
        if i == value:
            return f'The value {value} found at Index {array.index(value)}'
    return f"The value {value} doesn't exist in this Array"


print(searchingAnElement(arr1, 7))
