# ****** Sharing Views.py ***********
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from sharing.forms import UserForm, MemberForm, ItemForm, GroupForm
from sharing.models import Member, Group, Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def index(request):
	return render(request, 'sharing/index.html')


def about(request):
    return render(request, 'sharing/about.html')


def register(request):
	registered = False

	if request.method == "POST":
		print request.POST
		user_form = UserForm(data=request.POST)
		member_form = MemberForm(data=request.POST)

		if user_form.is_valid() and member_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			member = member_form.save(commit=False)
			member.user = user

			if 'profile_picture' in request.FILES:
				member.profile_picture = request.FILES['profile_picture']

			member.save()
			registered = True

		else:
			print user_form.errors, member_form.errors

	else:
		user_form = UserForm()
		member_form = MemberForm()
		
	return render(request, 'sharing/register.html', {'user_form': user_form,
				'member_form': member_form, 'registered': registered})


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

@login_required
def add_item(request):

	item_added = False

	if request.method == "POST":
		print request.POST
		item_form = ItemForm(data=request.POST)

		if item_form.is_valid():
			# (commit=False) doesn't save data to database
			item = item_form.save(commit=False)
			item.member = request.user.member

			if 'photo' in request.FILES:
				item.photo = request.FILES['photo']

			item.save() # saves form data to database.
			item_added = True

		else:
			print item_form.errors

	else:
		item_form = ItemForm()
		
	return render(request, 'sharing/add_item.html', {'item_form': item_form,
				'item_added': item_added})

@login_required
def add_group(request):
	group_added = False

	if request.method == "POST":
		print request.POST
		group_form = GroupForm(data=request.POST)

		if group_form.is_valid():
			# (commit= False) doesn't save data to database 
			group = group_form.save(commit=False) 
			group.moderator = request.user.member

			if 'group_picture' in request.FILES:
				group.photo = request.FILES['group_picture']

			group.save() # saves form data to database.
			group_added = True

		else:
			print group_form.errors

	else:
		group_form = GroupForm()

	return render(request, 'sharing/add_group.html', {'group_form': group_form,
				 'group_added': group_added})

@login_required
def inventory(request):
	# Query for items.
	item_list = Item.objects.filter(member__user=request.user)
	print len(item_list)

	context_dict = {'items': item_list,}
	return render(request, 'sharing/inventory.html', context_dict)	

