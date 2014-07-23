from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
	member = models.OneToOneField(User)
	profile_picture = models.ImageField(upload_to='profile_images', blank=True)
	zip_code = models.CharField(max_length=5)

	def __unicode__(self):
		return self.member.username


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
	photo = models.ImageField(upload_to='profile_images', blank=True)
	member = models.ManyToManyField(Member, related_name='item_owner')
	# loaned = ????

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Items"


class Group(models.Model):
	name = models.CharField(max_length=30)
	description= models.CharField(max_length=30)
	moderator= models.ForeignKey(Member)
	member_list = models.ManyToManyField(Member, related_name='group_members')
	item_list  = models.ManyToManyField(Item, related_name='group_items')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Groups"


