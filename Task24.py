'''Write a Python program that uses list comprehension to create a new list
containing the squares of the numbers from 1 to 10.'''

# lst = [1,2,3,4,5,6,7,8,9,10]
# new_lst =[]
# for i in lst:
#     a=i**2
#     new_lst.append(a)
# print(new_lst)


squares=[x**2 for x in range (1,11)]
print(squares)
