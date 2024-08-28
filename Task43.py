'''Write a Python program to create Fibonacci series up to n using Lambda'''

# def fibonacci(count):
#     listA = [0,1]

#     list(map(lambda x: listA.append(sum(listA[-2:])),range(2,count)))

#     return listA[:count]

# print(fibonacci(8))

number=int(input('Enter the number:'))

fibonacci=lambda x:x if x<=1 else fibonacci(x-1) + fibonacci(x-2)
for i in range(number):
    print(fibonacci(i),end=",")