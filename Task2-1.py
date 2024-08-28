string = 'Malayalam'
def palindrome(string):
    string = string.lower()
    reversed_string= ''
    for i in range(len(string),0,-1):
        reversed_string+= string[i-1]
    return string == reversed_string
print(palindrome(string))