'''Part 1 
Write a Python program to check that a string contains only a certain set of 
characters (in this case a-z, A-Z and 0-9).'''
# import re
# txt = input("Enter the string:")
# string = '[^a-zA-Z0-9]*$'
# x = re.match(string,txt)
# if x:
#     print("String contains only a certain set of characters")
# else:
#     print("String contains other characters")
import re
def x(k):
   y = re.compile(r'[^a-zA-Z0-9]')
   k = y.search(k)
   return not bool(k)

print(x("ABCghfvjDEF@@#abcdef123450"))
print (x("abc456789ok"))

'''Part 2
Write a Python program that matches a string that has an a followed by zero or 
one 'b
'''
# import re
# def text_match(text):
#    pattern= 'ab?'
#    if re.search (pattern,text):
#       return 'Text matched!'
#    else:
#       return 'Text Not Matched! '
# print(text_match("a"))
# print(text_match("ab"))
# print(text_match("abcba"))
# print(text_match("acacb"))
# print(text_match("aac"))
# print(text_match("bc"))