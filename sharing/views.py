# ****** Sharing Views.py ***********
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from sharing.forms import MemberForm, MemberProfileForm, ItemForm
from sharing.models import Member, Group, Item


# Create your views here.

def index(request):
	# context_dict = {}
	return render(request, 'sharing/index.html')


def about(request):
    # context_dict = {'welcome': "Welcome to the About Page!"}
    return render(request, 'sharing/about.html')


def register(request):
	registered = False

	if request.method == "POST":
		print request.POST
		member_form = MemberForm(data=request.POST)
		profile_form = MemberProfileForm(data=request.POST)

		if member_form.is_valid() or profile_form.is_valid():
			member = member_form.save()
			member.set_password(member.password)
			member.save()

			profile = profile_form.save(commit=False)
			profile.member = member

			if 'profile_picture' in request.FILES:
				profile.profile_picture = request.FILES['profile_picture']

			profile.save()
			registered = True

		else:
			print member_form.errors, profile_form.errors

	else:
		member_form = MemberForm()
		profile_form = MemberProfileForm()
		
	return render(request, 'sharing/register.html', {'member_form': member_form,
				'profile_form': profile_form, 'registered': registered})

def add_item(request):

	item_added = False

	if request.method == "POST":
		print request.POST
		item_form = ItemForm(data=request.POST)

		if item_form.is_valid():
			item = item_form.save(commit=False) # .save(commit=False) ??
			item.save()

			if 'photo' in request.FILES:
				item.photo = request.FILES['photo']

			item.save()
			item_added = True

		else:
			print item_form.errors

	else:
		item_form = ItemForm()
		
	return render(request, 'sharing/add_item.html', {'item_form': item_form,
				'item_added': item_added})


