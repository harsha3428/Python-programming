'''Write a program to create an iterator to print English alphabets from A to Z'''
class ALPHABET():
    def __init__(self):
        self.alpha = ord('A')
    def __iter__(self):
        return self
    def __next__(self):
        if self.alpha > ord('Z'):
            raise StopIteration
        else:
            alphabet = chr(self.alpha)
            self.alpha += 1
            return alphabet
        
alphabet_iterator=ALPHABET()

for alphabet in alphabet_iterator:
    print(alphabet,end=" ")