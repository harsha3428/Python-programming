
'''Task 18
Print the Fibonacci series for first 12 numbers.'''


n=12
a=0
b=1
for i in range(n):
    print(a, end=",")
    temp = a + b
    a=b
    b = temp

