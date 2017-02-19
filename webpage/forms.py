from django import forms

class UsernameForm(forms.Form):
	username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'search', 'id':'search'}))