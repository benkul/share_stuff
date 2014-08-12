from django import forms
from sharing.models import Member, Item, Group, JoinRequest
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	username = forms.CharField(widget=forms.TextInput(attrs=
			{'placeholder': '3 or more characters, no spaces'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')


class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ('zip_code','profile_picture',)

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('name', 'category', 'description', 'photo')


class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ('name', 'description', 'group_picture')

class AcceptRequestForm(forms.ModelForm):
	class Meta:
		model = JoinRequest
		fields = ('accept', 'reject')

