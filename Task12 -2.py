'''Question 12- Create a Python program that takes a string as input and checks if all the
characters in the string are unique (i.e., no character repeats). Return True if all 
characters are unique, and False otherwise'''

st = input("Enter the string: ")
x=list(set(st))
y=list(st)
x.sort()
y.sort()
if(x==y):
    print(True)
else:
    print(False)