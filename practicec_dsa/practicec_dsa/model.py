from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class Order(BaseModel):
    order_id = models.AutoField(max_length=50, unique=True)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"Order #{self.id} - {self.status}"