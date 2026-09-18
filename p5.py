#find common elements in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [5,3,7,9,6]
common_elements = [x for x in list1 if x in list2]
print(common_elements)