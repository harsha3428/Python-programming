'''Write a Python program to calculate the sum of the positive and negative numbers 
of a given list of numbers using the lambda function'''

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]
print("Original list:", numbers) 
total_negative_nums = list(filter(lambda numbers: numbers < 0, numbers))
total_positive_nums = list(filter(lambda numbers: numbers > 0, numbers))
print("Sum of the negative numbers: ", sum(total_negative_nums))
print("Sum of the positive numbers: ", sum(total_positive_nums))
