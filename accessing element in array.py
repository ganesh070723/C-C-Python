# accessing element in array

from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])


def accessingElementinArray(array, index):
    if index > len(array) - 1:
        print(f"\n\nTHERE ISN'T ANY ELEMENT AT INDEX {index}\n\n")
    else:
        print(f"The Element Found At Index {index} is : {array[index]}")


accessingElementinArray(arr1, 5)
