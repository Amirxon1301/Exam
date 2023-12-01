from django import forms
from .models import *

class MaqolaForm(forms.ModelForm):
    class Meta:
        model = Maqola
        fields = "__all__"
# class MaqolaForm(forms.Form):
#     s = forms.CharField(label="sarlavha", max_length=30, min_length=3)
#     m = forms.IntegerField(label="mavzu", max_value=5)
#     sana = forms.DateField(label="sana")
#     mu = forms.