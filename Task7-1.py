
list1= [1,2,2,3,4,4,5,6,7,7,8,9,12,12,12,22,23,23,28,29,29,32,36,55,55,60,61,62,63,63,65,78,79,80,80,89]
list2= [1,2,3,3,4,8,9,12,13,16,19,22,55,23,56,62,78,79,80,89]
list3 = []
for i in list1:
    if i in list2 and i not in list3:
        list3.append([i])
print(list3)
print(type(list3))