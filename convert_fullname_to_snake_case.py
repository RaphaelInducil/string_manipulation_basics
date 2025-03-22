# Inducil, Raphael Clouiee A.
# 3-22-25
# batch 5, prog10: create a program that ask the user to input their fullname in incorrect casing. print the input in snake case.

# ask user to input their full name in incorrect casing

full_name = input("Enter your full name: ")

# convert input to lowercase
# replace spaces with underscores

snake_case_name = full_name.lower().replace(" ", "_")

# print output

print(snake_case_name)

# end