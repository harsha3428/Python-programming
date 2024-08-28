'''You are developing a system to handle different payment methods. Implement an
abstract class called PaymentMethod with an abstract method processPayment().
The processPayment() method should be implemented by the concrete classes
that inherit from PaymentMethod and should simulate the payment processing
for each specific payment method.
Create two concrete classes CreditCardPayment and PayPalPayment that
extend the PaymentMethod class. Implement the processPayment() method in
both classes to display a message indicating the payment method being
processed.
Write the abstract class PaymentMethod, the concrete classes CreditCardPayment
and PayPalPayment, and the code to demonstrate polymorphism.'''
# from abc import ABC,abstractmethod
# class PaymentMethod(ABC):
#     @abstractmethod
#     def processPayment(self,credit,Paypal):
#         pass
        
# class CreditCardPayment(PaymentMethod):
#     def processPayment (self,credit):
#         print("The Payment method being processed")
# class PayPalPayment(PaymentMethod):
#     def processPayment(self,Paypal):
#         print("The Payment method being processed")

# Payment1 =  CreditCardPayment()
# Payment2 = PayPalPayment()

# Payment1.processPayment()
# Payment2.processPayment()

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self):
        pass

class CreditCardPayment(PaymentMethod):
    def processPayment(self):
        return ("Credit Card Payment Processing")

class PayPalPayment(PaymentMethod):
    def processPayment(self):
        return ("PayPal Payment Processing")

credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
pay1 = credit_card_payment.processPayment()
pay2 = paypal_payment.processPayment()
print(pay1)
print(pay2)
# print(credit_card_payment.processPayment())
# print(paypal_payment.processPayment())