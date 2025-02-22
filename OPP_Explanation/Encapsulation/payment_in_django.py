from django.shortcuts import render, redirect
from django.contrib import messages
from practicec_dsa.model import Order

class PaymentProcessor:
    def __init__(self, order):
        self.order = order

    def process_payment(self):
        """Encapsulated method to process payment."""
        if self.order.total_amount <= 0:
            raise ValueError("Invalid order amount.")
        # Simulate payment processing
        self.order.status = "Paid"
        self.order.save()

def checkout(request, order_id):
    order = Order.objects.get(id=order_id)
    payment_processor = PaymentProcessor(order)

    try:
        payment_processor.process_payment()
        messages.success(request, "Payment successful!")
    except ValueError as e:
        messages.error(request, str(e))

    return redirect("order_detail", order_id=order.id)