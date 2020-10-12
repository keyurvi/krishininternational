from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import ContactUs
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['email', 'name', 'phone_number', 'message']
        widgets = {
            'name': TextInput(attrs={'placeholder':'Your Name'}),
            'email': TextInput(attrs={'placeholder':'Your email'}),
            'phone_number': TextInput(attrs={'placeholder':'Your Phone number'}),
            'message': Textarea(attrs={'placeholder':' Message'}),
        }
        # email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'Your email'}))
        # name = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Your Name'}))
        # contact = forms.CharField(max_length=15,widget= forms.TextInput(attrs={'placeholder':'Your Phone number'}))
        # message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}))
# class ContactForm(forms.Form):
#     pass