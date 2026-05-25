from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")