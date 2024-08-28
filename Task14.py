'''Task 14
Convert two lists into a dictionary in Python without using a built-in method'''

text_key = ['Mango','Orange','Apple','Strawberry']
text_value = [65,54,60,100]

print("Original key list is " , str(text_key))
print("Original value list is ", str(text_value))

dict1={}

for key in text_key:
    for value in text_value:
        dict1[key]=value
        text_value.remove(value)
        break
print("New dictionary is ",str(dict1))