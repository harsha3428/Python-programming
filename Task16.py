'''Task 16
Write a program to check palindrome number.'''

n= 1533553351
temp=n
reverse=0
while temp>0:
    remainder = temp %10
    reverse = (reverse * 10) + remainder
    temp=temp // 10
if n == reverse:
    print("{} is Palindrome".format(n))
else:
    print("{} is not palindrome".foramt(n))
