# Created by Ganesh on 28 March 2022.
# To learn data structures
from array import *

# 1 Create an array and traverse.

my_array = array("i", {1, 2, 3, 4, 5})
print("\nstep 1")
for i in my_array:
    print(i)
# 2 Accessing Individual elements through indexes
print("\nstep 2")
print(my_array[0])

# 3 Append any value to the array using append() method.

my_array.append(6)
print("\nstep 3")
print(my_array)

# 4. Insert value in an array using insert() method

print("\nstep 4")
my_array.insert(1, 7)
print(my_array)

# 5. Extend python array using extend() method

my_array1 = array("i", {10, 11, 12})
my_array.extend(my_array1)
print("\nstep 5")
print(my_array)

# 6. Add items from list into array using fromlist() method.

list1 = [13, 14, 15]
my_array.fromlist(list1)
print("\nstep 6")
print(my_array)

# 7. Remove any array element using remove() method
print("\nstep 7")
my_array.remove(15)
print(my_array)

# 8. Remove list element using pop() method.
print("\nstep 8")
list1.pop(2)
print(list1)

# 9. Fetch any element through its index using index() method.

print("\nstep 9")
print(my_array.index(14))

# 10. Reverse a python array using reverse() method.

print("\nstep 10")
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method.
print("\nstep 11")






