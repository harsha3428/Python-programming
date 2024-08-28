'''Task 13
Write a Python function that takes a dictionary of items and their prices as input 
and finds and prints the keys (items) with the highest prices.
Find Keys with Maximum Value'''

user_dict = {}
number_entries = int(input("Enter the number of entries: "))

for i in range(number_entries):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print("Dictionary: ", user_dict)
print(type(user_dict))
print("Key with highest price is {} and highest value is {}".format(max(user_dict),max(user_dict.values())))
