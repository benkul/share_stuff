from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
	user = models.OneToOneField(User)
	profile_picture = models.ImageField(upload_to='profile_images', blank=True)
	zip_code = models.CharField(max_length=5)

	def __unicode__(self):
		return self.user.username


class Item(models.Model):
	name = models.CharField(max_length=30)
	category_choices = (
		('Tools', 'Tools & Gardening'),
		('Home', 'Home & Appliances'), 
		('Sports', 'Sports & Outdoors'),
		('Electronics', 'Electronics'),
		('Arts_etc', 'Arts & Crafts'),
		('Movies_etc', 'Movies, Music, & Books'),
		('Other', 'Other')
	)
	category = models.CharField(max_length=30, choices=category_choices)
	description = models.TextField()
	photo = models.ImageField(upload_to='item_images', blank=True)
	member = models.ForeignKey(Member, related_name='item_owner')
	# loaned = ????

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Items"


class Group(models.Model):
	name = models.CharField(max_length=30)
	description= models.TextField()
	moderator= models.ForeignKey(Member, related_name="moderator")
	member_list = models.ManyToManyField(Member, related_name='group_members')
	item_list  = models.ManyToManyField(Item, related_name='group_items')
	group_picture = models.ImageField(upload_to='group_images', blank=True)


	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Groups"
