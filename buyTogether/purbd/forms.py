from django import forms
from .models import Pur

class Purmodelform(forms.ModelForm):
	class Meta:
		model = Pur
		fields = ['title','body','date','category','wpeople','price','location']
