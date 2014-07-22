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
	category = models.CharField(max_length=30)
	description = models.TextField()
	photo = models.ImageField(upload_to='profile_images', blank=True)
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
	items_list  = models.ManyToManyField(Item, related_name='group_items')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Groups"


