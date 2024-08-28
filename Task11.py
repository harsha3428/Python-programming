'''Create a Python program that takes two sets and returns a new set containing 
elements that are common in both input sets '''


set_data1 = {'pencil','pen', 'book','ruler','marker'}
set_data2 = {'pen','ruler','whitener','geometry box','marker'}

#common_element= set_data1.intersection(set_data2)
#print("Common elements are : ", common_element)

common_elements = {x for x in set_data1 if x in set_data2}
print(common_elements)
    
