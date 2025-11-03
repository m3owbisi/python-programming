my_tuple = ('F', 'I', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'd')
new_tuple = my_tuple + ('!',)
my_string = ''.join(my_tuple)
extracted_subtuple = my_tuple[3:5]
count_e = my_tuple.count('e')
is_r_present = 'r' in my_tuple
my_list = list(my_tuple)
for char in ('b', 'e', 'r'):
    my_list.remove(char)
modified_tuple = tuple(my_list)
print(f"original tuple : {my_tuple}")
print(f"tuple with exclamation mark : {new_tuple}")
print(f"string from tuple : {my_string}")
print(f"extracted subtuple : {extracted_subtuple}")
print(f"count of 'e' : {count_e}")
print(f"is 'r' present : {is_r_present}")
print(f"list from tuple : {my_list}")
print(f"modified_tuple (after modifying list) : {modified_tuple}")
