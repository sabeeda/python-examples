from django import forms
from .models import Loginmodel
from formset.widgets import DateTimeInput
class Login(forms.ModelForm):
    class Meta:
        model=Loginmodel
        fields="__all__"
class InputForm(forms.Form):
    first_name=forms.CharField(max_length=200)
    Lastname=forms.CharField(max_length=100)
    roll_number=forms.IntegerField(help_text="Enter 6 digit roll_number")  
    Password=forms.IntegerField(widget=forms.PasswordInput())

class CV_Submission(forms.Form):
     first_name=forms.CharField(max_length=200)
     Lastname=forms.CharField(max_length=100)
     Place=forms.CharField(max_length=200)
     Age=forms.IntegerField()
     Date_ofbirth=forms.DateField(widget=forms.DateInput(format="%d-%m-%y",attrs={"type":"date"}))
     Time=forms.DateTimeField(widget=DateTimeInput,)
     Photo=forms.ImageField()
     Sex=forms.ChoiceField(choices=((0,"Male"),(1,"Female"),(2,"other")))
     Cv=forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'form-control-file'})) 
     Email_Address=forms.EmailField(widget=forms.EmailInput(attrs={'input_type':"email"}))
     Married=forms.BooleanField(widget=forms.CheckboxInput())
     mark=forms.DecimalField(widget=forms.NumberInput())
     tags = forms.MultipleChoiceField(choices=((0,"Male"),(1,"Female"),(2,"other")))
     who_can_message= forms.CheckboxSelectMultiple(choices=((1,"Male"),(2,"Female"),(3,"other")))

class BookForm(forms.Form):
    Title=forms.CharField(max_length=200)
    Author=forms.CharField(max_length=200)
    Publication_Date=forms.DateField()

    
