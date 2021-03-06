from django import forms
from .models import User

class UserLoginform(forms.ModelForm):
	class Meta:
		model = User
		fields = ['userID','password']
		widgets = {
            'userID': forms.EmailInput(attrs={'class': 'form-control item', 'placeholder':'이메일'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control item', 'placeholder':'비밀번호'}),
        }

class UserSignupform(forms.ModelForm):
	class Meta:
		model = User
		fields = ['userID','password','username']
		widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control item', 'placeholder':'닉네임'}),
            'userID': forms.EmailInput(attrs={'class': 'form-control item', 'placeholder':'이메일'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control item', 'placeholder':'비밀번호'}),
        }
