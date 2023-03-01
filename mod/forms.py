from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(min_length=1, max_length=20)
    last_name = forms.CharField(min_length=1, max_length=20)
    password = forms.CharField(min_length=1, max_length=20)
    password2= forms.CharField(min_length=1, max_length=20)
    email = forms.EmailField(min_length=1,max_length=50)
#
class LoginForm(forms.Form):
    password = forms.CharField(min_length=1, max_length=20)
    email = forms.EmailField(min_length=1,max_length=50)

# class LoginForm(forms.Form):
#     password = forms.CharField(widget=forms.PasswordInput)
#     email = forms.EmailField(min_length=1,max_length=50)

class WallPostForm(forms.Form):
    text = forms.CharField(max_length=500)
    title = forms.CharField(max_length=50)

