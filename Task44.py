'''Write a Python program to find numbers divisible by nineteen or thirteen from a list 
of numbers using Lambda'''

nums = [26, 12, 52, 65, 42, 91, 104, 117, 67]

print("Original numbers of the list")
print(nums)

result = list(filter(lambda x: x % 19 == 0 or  x % 13 ==0,nums ))
print("\nNumbers of the above list divisible by nineteen or thirteen: ")
print(result)