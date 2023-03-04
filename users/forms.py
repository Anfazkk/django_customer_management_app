from django import forms

from users.models import Customer


class UserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'phone', 'email', 'address', 'date_of_birth', 'password']

        