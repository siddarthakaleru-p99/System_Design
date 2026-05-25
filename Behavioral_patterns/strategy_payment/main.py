from payment_strategy import (
    CreditCardPayment,
    UPIPayment,
    PayPalPayment
)


class PaymentContext:

    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


card_payment = PaymentContext(CreditCardPayment())
card_payment.make_payment(5000)

upi_payment = PaymentContext(UPIPayment())
upi_payment.make_payment(1200)

paypal_payment = PaymentContext(PayPalPayment())
paypal_payment.make_payment(3000)