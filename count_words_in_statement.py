# Inducil, Raphael Clouiee A.
# 3-22-25
# batch 5, prog07: create a program that ask the user to input a complete statement. print the number of words in the input.

# ask user to input a complete statement

statement = input("Enter a complete statement: ")

# split the statement into words
# count the number of words

word_count = len(statement.split())

# print output

print(word_count)

# end