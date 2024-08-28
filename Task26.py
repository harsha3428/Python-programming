'''Write a Python program that uses a list comprehension to create a new list that 
contains only the uppercase letters in an existing list of strings'''

string= input("Enter your strings : ")
print("Original string is: " + string)

upper= list(char for char in string if char.isupper())
print("Uppercase characters in string are:" ,upper)