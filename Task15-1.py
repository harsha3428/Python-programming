'''Write a program to check Armstrong number

'''

no_di = int(input("Enter number of digit: ")) # number of digit of the number entering
number=int(input("Enter your number: "))
sum=0
n= number
while n>0:
    digit = n % 10  #digit will be 
    sum += digit ** no_di
    n //= 10

if number==sum:
    print(number,"is a Armstrong number")
else:
    print(number,"is not a Armstrong number")

