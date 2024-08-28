'''Create a Python function that takes a string as input and counts the number of 
vowels and consonants in the string.'''
def vowel_count(str):

    count = 0
     
    
    vowel = set("aeiouAEIOU")
     
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
     
    print("No. of vowels :", count)
     

str = input("Enter your string: ")
 
vowel_count(str)