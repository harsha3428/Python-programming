'''Write a Python program that takes a list of numbers as input and calculates and
prints the sum and average of those numbers.'''

'''lst= [int(i) for i in input("Enter your numbers : ").split()]
sum=0
avg=0
for i in lst:
    sum=sum+i
    avg=sum/len(lst)
print(sum)
print(avg)
print(type(lst))
'''
    
'''a=[]

for i in ele:
    a.append(i) 

print(ele)
print(type(ele))
print("The list of elements: ",a)

Addition = sum(a)
#n=len(a)
#Average= sum/n
print("Sum : ",Addition)
#print("Average : ",Average)'''


'''Write a Python program that takes a list of numbers as input and calculates and
prints the sum and average of those numbers.'''


input_value=input("Enter the numbers: ")

numbers=input_value.split()


for i in range(len(numbers)):
    numbers[i]=int(numbers[i])

s=sum(numbers)
avg=sum(numbers)/len(numbers)
print("Sum of numbers: ",s )
print("Average of numbers: ", avg)

