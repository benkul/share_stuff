from django import forms
from sharing.models import Member
from django.contrib.auth.models import User

class MemberForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class MemberProfileForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ('picture')


