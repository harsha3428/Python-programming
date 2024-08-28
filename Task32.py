'''You are working on a project to develop a class representing a Book. The Book
class should have properties such as title, author, and year of publication.
Implement the constructor for the Book class that initializes these properties
when a new Book object is created. Additionally, provide a method called
getBookInfo() that returns a string with the book's details in the format "Title:
[title], Author: [author], Year: [year]".
Write the constructor and the getBookInfo() method for the Book class.
'''

class Book:
    def __init__(self,Title,Author,Year):
        self.Title = Title
        self.Author = Author
        self.year = Year

    def getBookInfo(self):
        print(f'Title:[{self.Title}], Author:[{self.Author}],Year:[{self.year}]')


Bookdetails = Book(Title= "Adujeevitham",Author= "Benyamin",Year= "1996")
Bookdetails.getBookInfo()
