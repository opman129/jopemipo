from django import forms

from .models import PortfolioForm

class PortfolioContactForm(forms.ModelForm):
    Name = forms.CharField(label='Name',required=True, widget=forms.TextInput(attrs={"placeholder": "Your Name"}))
    Email = forms.EmailField(label='Email',required=True, widget=forms.TextInput(attrs={"placeholder": "Your Email"}))
    Subject = forms.CharField(label='Subject', required=True,widget=forms.TextInput(attrs={"placeholder": "Input your Subject"}))
    Message = forms.CharField(label='Message',required=True,widget=forms.Textarea(attrs={"placeholder": "Your Message"})) 
    

    class Meta:
        model   = PortfolioForm
        fields  = [
            'Name',
            'Email',
            'Subject',
            'Message',
]