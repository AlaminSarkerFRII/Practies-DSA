# Example: User Registration Form
# Suppose you’re building a user registration system and want to encapsulate password validation.
from click import confirm
from django.forms import forms
from django.contrib.auth.models import  User

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def clean_password(self):
        """Encapsulated method to validate passwords."""
        clean_data = super().clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long')
        return clean_data


'''
Encapsulation in Action:
The clean method encapsulates the logic for validating that the passwords match.
The form hides the complexity of password validation from the view.
'''