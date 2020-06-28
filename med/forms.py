from django import forms
from med.models import medicine
from med.models import blog, subscribe, contactus, upload
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#create your model here.
class medicineform(forms.ModelForm):
    name= forms.CharField(max_length=200)
    brand= forms.CharField(max_length=200)
    price= forms.CharField(max_length=200)
    photo= forms.ImageField()
    class Meta:
        model=medicine
        fields="__all__"
        
class blogform(forms.ModelForm):
    title= forms.CharField(max_length=200)
    detail= forms.CharField(max_length=50000)
    name= forms.CharField(max_length=200)
    date= forms.CharField(max_length=200)
    photo= forms.ImageField()
    class Meta:
        model=blog
        fields="__all__"
        
class SubscribeForm(forms.ModelForm):
    email=forms.CharField(max_length=200)
    class Meta:
        model=subscribe
        fields="__all__"
        
class contactusForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    subject=forms.CharField(max_length=200)
    email=forms.CharField(max_length=200)
    message=forms.CharField(max_length=200)
    class Meta:
        model=contactus
        fields="__all__"
        
class uploadForm(forms.ModelForm):
    name= forms.CharField(max_length=200)
    address= forms.CharField(max_length=200)
    phone= forms.CharField(max_length=200)
    image= forms.ImageField()
    class Meta:
        model=upload
        fields="__all__"
        
        
