people = [('Anu',23), ('Joseph',47),('Amala',15),('Kiran',20)]
print("Original list is: ",people)


#accessing item from list of tuples



c= [x[1] for x in people]
print("Age of people: ", c)
#number of items in c
n= len(c)
print("Number of items: ",n)

#Finding average of age

addition= sum(c)
print("sum of age: ",addition)
print("Average age of people: ", addition/n)