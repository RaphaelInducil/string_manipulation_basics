# Inducil, Raphael CLouiee A.
# 3-22-25
# batch 5, Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# ask user input full name

full_name = input("Enter your full name with spaces at the beginning: ")

# strip unnecessary spaces before the name
# print stripped output

print(full_name.strip())

# end