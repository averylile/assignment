#ASSIGNMENT #1
def remove_dupe(data : list) -> list:
    unique_set = set(data)
    return list(unique_set)

my_list = [1, 2,3,4, 5, 6, ]
print(my_list)

#ASSIGNMENT 2
set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}

union_set = set1 | set2
print(union_set)

intersection_set = set1 & set2
print(intersection_set)

different_set = set1 - set2
print(different_set)

sym_diff_set = set1 ^ set2
print(sym_diff_set)

#ASSIGNMENT 3
set_3 = {1, 2, 3}
element_to_find = 4
for element in set_3:
        if element == element_to_find:
            print(element_to_find)
            break