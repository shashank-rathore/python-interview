"""Write a python program to reverse a string"""

# read input from command prompt
STRING=input("Give me a sentence to reverse:")
#split the string and save as a list. empty split() means split on standard delemiters as whitespaces, \n, \t etc.
STRING_LIST=STRING.split()
print(f"List: {STRING_LIST}")

# Reverse the list of strings and print.
STRING_LIST_REV=STRING_LIST[::-1]
print(f"Reverse List: {STRING_LIST_REV}")

print(" ".join(STRING_LIST_REV))
