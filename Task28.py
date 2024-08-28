'''Write a Python program to remove duplicates from a list while preserving the 
order of elements'''

my_list = input("Enter your elements of list:   ").split()
my_list1= []
[my_list1.append(x) for x in my_list if x not in my_list1]

print(my_list1)