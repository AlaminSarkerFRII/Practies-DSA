from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def get_age(self):
        """User এর age calculate করার encapsulated method।"""
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def set_email(self, new_email):
        """Email update করার encapsulated method with validation।"""
        if "@" not in new_email:
            raise ValidationError("Invalid email format.")
        self.email = new_email
        self.save()
        
        
'''
Encapsulation কিভাবে কাজ করছে:

1. email এবং date_of_birth fields গুলো directly modify করা যাবে না।

2. get_age method টি user এর age calculate করার logic encapsulate করে রেখেছে।

3. set_email method টি email update করার সময় validation logic encapsulate করে রেখেছে।

'''