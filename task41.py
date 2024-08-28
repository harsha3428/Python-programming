'''Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 
'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
'''

mobile = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("Original dictionary is:")
print(mobile)
mobile_model =sorted(mobile,key = lambda x:x['make'])
print("\nSorting the List of dictionaries:")
print(mobile_model)