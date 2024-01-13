# Lists and tuples
# Task 1
fruits = []
for i in range(5):
    fruit = input("Enter a favorite fruit: ")
    fruits.append(fruit)
print("List of favorite fruits:", fruits)

# Task 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle_five = numbers[2:7]
print("Middle five numbers:", middle_five)

# Task 3
num1 = int(input())
num2 = int(input())
num3 = int(input())
num_tuple = (num1, num2, num3)

print(num_tuple)

# Task 4
my_list = [1, 3, 5, 2, 4]
my_list.append(6)
my_list.pop(0)
my_list.sort()
print("Modified list:", my_list)

# Task 5
num_list = [2, 4, 6, 8, 10]
search_num = int(input())
if search_num in num_list:
    print("Number exists in the list")
else:
    print("Number does not exist in the list")

# Task 6
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print("Reversed list:", reversed_list)

# Task 7
my_tuple = (10, 20, 30, 40)
a, b, c, d = my_tuple
print(a, b, c, d)

# Task 8
my_list = int(input())
max_num = max(my_list)
min_num = min(my_list)
print(max_num, min_num)

# Task 9
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# Task 10
num_list = int(input())
num_tuple = tuple(num_list)
print(num_tuple)

# sets and dictionaries
# Task 1
unique_numbers = set()
for i in range(5):
    number = int(input("Enter a unique number: "))
    unique_numbers.add(number)
print(unique_numbers)

# Task 2
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)

# Task 3
my_dict = {}
for i in range(3):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    my_dict[key] = value
print(my_dict)

# Task 4
key = input()
if key in my_dict:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")

# Task 5
input_string = input()
char_frequency = {}
for char in input_string:
    char_frequency[char] = char_frequency.get(char, 0) + 1
print(char_frequency)

# Task 6
given_element = int(input())
if given_element in unique_numbers:
    print("Element is present in the set.")
else:
    print("Element is not present in the set.")

# Task 7
print(list(my_dict.values()))

# Task 8
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print( merged_dict)

# Task 9
key_to_remove = input()
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print("Without key:", my_dict)
else:
    print("Key not found in the dictionary.")

# Task 10
input_list = [1, 2, 3, 4, 2, 3, 5, 6, 7, 8, 7, 9]
unique_elements_set = set(input_list)
print(unique_elements_set)

