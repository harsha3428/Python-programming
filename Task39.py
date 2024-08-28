'''Write a program to create a custom iterator that iterates from 1 to 10 in 0.5 intervals'''
class numbers:
    def __iter__ (self):
        self.value = 1
        return self
    def __next__(self):
        if self.value > 10:
            raise StopIteration
        num = self.value
        self.value += 0.5
        return num

obj = numbers()
obj_iter =iter(obj)
print(next(obj_iter))
print(next(obj_iter))
print(next(obj_iter))
print(next(obj_iter))
print(next(obj_iter))
print(next(obj_iter))
print(next(obj_iter))
print(next(obj_iter))
# class one_to_ten:
#    def __iter__(self):
#        self.value = 1
#        return self
#    def __next__(self):
#        if self.value > 10:
#            raise StopIteration
#        temp = self.value
#        self.value += 0.5
#        return temp
# obj = one_to_ten()
# obj_iter = iter(obj)
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))
