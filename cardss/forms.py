from django import forms
from .models import Cards

class CardsForm(forms.ModelForm):
	upload_date=forms.DateField(widget=forms.SelectDateWidget)

	

	class Meta:
		model = Cards
		fields = ['name', 'image', 'desc', 'v_type','upload_date']
