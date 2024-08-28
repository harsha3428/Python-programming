'''Write a function in Python to count and display the total number of words in a 
text file'''




def total_words():
    file = open("word.txt","r")
   
    count =0
    data = file.read()
    words =data.split()
    for line in words:
        count += 1
    # file=open('word.txt','a')
    # print(file.write("Total words are",count))
    print("Total words are", count)
    file.close()
    
total_words()        
