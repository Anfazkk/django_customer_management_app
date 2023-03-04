from django import forms

from users.models import Customer


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'phone', 'email', 'date_of_birth', 'address']

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'updateform'}),
            'phone': forms.TextInput(attrs={'class':'updateform'}),
            'email': forms.TextInput(attrs={'class':'updateform'}),
            'date_of_birth': forms.TextInput(attrs={'class':'updateform'}),
            'address': forms.Textarea(attrs={'class':'textarea'}),
        }