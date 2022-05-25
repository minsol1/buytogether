from django import forms
from .models import Free,Comment

class Freemodelform(forms.ModelForm):
	class Meta:
		model = Free
		fields = ['title','body']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']