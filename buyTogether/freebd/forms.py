from django import forms
from .models import Free,Comment

class Freemodelform(forms.ModelForm):
	class Meta:
		model = Free
		fields = ['title','body','photo']

		widgets = {
			'title' : forms.TextInput(
				attrs={'class': 'form-control', 'style': 'width: 400px', 'placeholder': '제목을 입력하세요.'}
			),
			'body' : forms.TextInput(
				attrs={'class': 'form-control', 'style': 'width: 400px', 'placeholder': '내용을 입력하세요.'}
			),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['body']

