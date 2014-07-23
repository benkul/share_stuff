# ****** Sharing Views.py ***********
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from sharing.forms import MemberForm, MemberProfileForm, ItemForm
from sharing.models import Member, Group, Item
from django.contrib.auth import authenticate, login, logout



def index(request):
	return render(request, 'sharing/index.html')


def about(request):
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


def sign_in(request):
	
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		print request.POST

		member = authenticate(username = username, password = password)

		if member:
			if member.is_active:
				login(request, member)
				return HttpResponseRedirect('/sharing/')
			else:
                # An inactive account was used - no logging in!
				return HttpResponse("Your sharing account is disabled.")
		else:
        # Bad login details were provided. So we can't log the user in.
			print "Invalid login details: {0}, {1}".format(username, password)
			return render(request, 'sharing/sign_in.html', {'invalid': "Invalid username or password"})
	else:
		return render(request, 'sharing/sign_in.html',)

def sign_out(request):
	logout(request)
	return HttpResponseRedirect('/sharing/')




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


