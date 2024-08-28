'''Write a function in Python to count words in a text file those are ending with 
alphabet "e"   '''

def count_words():
    file = open("word.txt","r")
    count= 0
    data = file.read()
    words = data.split()
    for i in words:
        if i [-1] == 'e' :
            count+=1
    print(count)
    file.close()
count_words()