str= input("enter text here:")
vowels ='aeiouAEIOU'
vcount=0
ccount=0
for i in str:
    if i in vowels:
        vcount+=1
    else:
        ccount+=1
print("Number of vowels in string", vcount)
print("Number of consonants in string", ccount)
print(type(vowels))
print(type(str))