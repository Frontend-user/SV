from django import forms


class UserForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20)
    family_name = forms.CharField(min_length=2, max_length=20)
    passworf = forms.CharField(min_length=2, max_length=20)
    mail = forms.CharField(min_length=2, max_length=20)
