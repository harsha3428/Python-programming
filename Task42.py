'''Write a Python program to square and cube every number in a given list of integers
using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''


list1 =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers: ")
print(list1)
print("\nSquare every number of the list:")

square_list1 = list(map(lambda x: x**2, list1))
print(square_list1)


print("\nCube every number of the list: ")

cube_list1 = list(map(lambda x: x**3, list1))
print(cube_list1)
