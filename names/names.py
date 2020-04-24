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

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# runtime: 0.198 complexity:
# loop through names_1 and insert each into bst (O(log n))
bst = BinarySearchTree(names_1[0])
for name_1 in names_1[1:]:
    bst.insert(name_1)

# loop through names_2 and see if bst contains the name (O(log n))
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)


'''stretch'''
# runtime 0.0089 complexity:
name_dict = {}

# loop through names_1 and put them in a dict (will not have duplicates)
for name in names_1:
    # put the names in a dict
    # if the name is not already there, set the value to 1
    if name not in name_dict:
        name_dict[name] = 1
    # if the name is already there, don't add it again, just increase the value by 1
    else:
        name_dict[name] += 1

# loop through names_2 and if the name is in name_dict, append to duplicates
for name in names_2:
    if name in name_dict:
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
#----------Efficient solution above----------------#
