# Inducil, Raphael Clouiee A.
# 3-22-25
# batch 5, prog09: create a program that ask the user to input their fullname in incorrect casing. print the input in pascal case.

# ask user to input their full name in incorrect casing

full_name = input("Enter your full name: ")

# convert input to pascal case (capitalize first letter of each word and remove spaces)

pascal_case_name = full_name.title().replace(" ", "")

# print output

print(pascal_case_name)

# end