# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MbFiMSGmJ3EI41YnKG82i1LdeNWUMgqW
"""

my_int = 42
print("Original Integer:", my_int)
result = my_int * 2
print("Result after multiplication:", result)

my_list = [1,'hello', 3.14, True]
print("Original List:", my_list)
my_list.append('world')
print("List after appendingg 'word':",my_list)
my_list.remove(3.14)
print("List after removing 3.14:",my_list)



my_tuple = (1, 'apple', 3.14, False)
print("Original Tuple:", my_tuple)
print("Original Tuple:", my_tuple)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])



my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
my_set.add(6)
print("Set after adding 6:", my_set)

my_dict = {"name": "John", "age": 30, "city": "New York"}
print("Original Dictionary:", my_dict)
my_dict["occupation"] = "Engineer"
print("Dictionary after adding occupation:", my_dict)

my_list = [1, 2, 3, 4, 5]
my_list.insert(0, 1)
print("List after insterting at the begining:", my_list)
middle_index=len(my_list)
my_list.insert(middle_index, 3.5)
print("List afetr inserting in the middle:", my_list)
my_list.append(6)
print("List after appending 6:", my_list)
print("\nSlicing with step(start:stop:step):")
print(my_list[1:8:2])

my_list = [1, 2, 3, 4, 5]
my_list.insert(0, 1)
print("List after insterting at the begining:", my_list)

middle_index=len(my_list)
my_list.insert(middle_index, 3.5)
print("List afetr inserting in the middle:", my_list)

my_list.append(6)
print("List after appending 6:", my_list)
print("\nSlicing with step(start:stop:step):")
print(my_list[1:8:2])

print ("\nReversing the list using slicing:")
print(my_list)

my_list = [1, 2, 3, 4 ,5, 6]
my_list.insert(7,9)
print("List after inserting at the begining:", my_list)

