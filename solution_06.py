"""
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]
"""

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

# This first loop reverses the values in the tuples
reversed_values = []
for i in unsorted_list:
    reversed_values.append((i[1], i[0]))

sorted_values = sorted(reversed_values)  # They can then be sorted
print(sorted_values)                     # This is in fact already a solution to the problem

# This loop just reverses the tuple values back to original order
sorted_list = []
for i in sorted_values:
    sorted_list.append((i[1], i[0]))

print(sorted_list)
