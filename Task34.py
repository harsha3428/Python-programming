'''You are developing a class called MathUtils that provides various mathematical
utility functions. Implement a static method called calculateSum() in the
MathUtils class. The calculateSum() method should accept an array of numbers
and return the sum of those numbers.
Write the MathUtils class with the static calculateSum() method and provide
code to test the functionality. '''



# class MathUtils:
#     @staticmethod
#     def CalculateSum():
#         sum(list1)
        

# list1=[155,54655,557]
# Sum = MathUtils.CalculateSum(list1)
# obj= MathUtils()
# obj.CalculateSum() 
# print('Sum of the numbers in list is ', obj.CalculateSum() )
        

class MathUtils:
    @staticmethod
    def calculate(n):
        return sum(n)

list1= [1245,457,6556]
sum= MathUtils.calculate(list1)
print("Sum of numbers :",sum)