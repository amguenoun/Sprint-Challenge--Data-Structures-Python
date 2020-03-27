import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#      RUNTIME IS O(N^2)
# Replace the nested for loops below with your improvements 
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# RUNTIME is O(n log n)

# tree = BinarySearchTree(names_1.pop()) #pop last item is constant time

# for name in names_1: #loop once is O(n)
#     tree.insert(name)

# for name in names_2:  #loop once is O(n)
#     if tree.contains(name): #contains is O(log n)
#         duplicates.append(name)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# Runtime O(4n) -> O(n)

name_set = {'first'}

set1 = set(names_1)
set2 = set(names_2)

for name in set1:
        name_set.add(name)

for name in set2:
    if name in name_set:
        duplicates.append(name)
    else:
        name_set.add(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")