from django import forms
from .models import Pur

class Purmodelform(forms.ModelForm):
	class Meta:
		model = Pur
		fields = ['title','body','date','category','wpeople','price','location','photo']

		widgets = {
			'title' : forms.TextInput(
				attrs={'class': 'form-control', 'style': 'width: 400px', 'placeholder': '제목을 입력하세요.'}
			),
			'body' : forms.TextInput(
				attrs={'class': 'form-control', 'style': 'width: 400px', 'placeholder': '내용을 입력하세요.'}
			),ㄴㄴ
			'wpeople' : forms.TextInput(
				attrs={'class': 'form-control', 'style': 'width: 400px', 'placeholder': '모집인원을 입력하세요.'}
			),
			'location' : forms.TextInput(
				attrs={'class': 'form-control', 'style': 'width: 400px', 'placeholder': '장소를 입력하세요.'}
			),
			'category' : forms.Select(
				attrs={'class': 'custom-select'}
			),
		}