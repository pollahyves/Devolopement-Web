from django import forms
from .models import *

# on cree notre formulaire
class FormTask(forms.ModelForm):
    amount = forms.IntegerField( widget=forms.NumberInput(
        attrs={'placeholder':'enter the amount sold today',
                'class':'form-control form-control-lg'}
    ))
    
    bank = forms.IntegerField( widget=forms.NumberInput(
        attrs={'placeholder':'enter the amount save at bank',
                'class':'form-control form-control-lg'}
    ))

    date = forms.DateField( widget=forms.DateInput(
        attrs={'placeholder':'ex:12-04-2023',
                'class':'form-control form-control-lg'}
    ))
#pour rendre ce formullaire rhobuste,on va utiliser la class meta
    class Meta:
        model = Task
        fields = ['amount','bank','date']