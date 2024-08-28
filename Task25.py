'''Write a Python program that uses a "for" loop to iterate over a string and prints 
out each character along with its count'''



string=input("Enter your string: ")
count={ }
char= {i: string.count(i) for i in set(string)}


print(char)

