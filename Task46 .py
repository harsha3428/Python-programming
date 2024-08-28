'''Write a function in python to count the number of lines from a text file "story.txt" 
which is not starting with an alphabet "T"'''
def line_count():
    file = open("story.txt","r")
    count =0
    for line in file:
        if line[0] not in 'T':
            count+=1
    file.close()
    print("No of files not starting with 'T'=",count)
line_count()