elements = (input("Enter the values: ").split())
list1 = list(elements)
print (list1)
new_list= []
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)
