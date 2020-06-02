from django.db.models import Q, Max
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import json

class EventCategory(models.Model):

		event_category = models.CharField(max_length=200,unique = True, default="Unknown")

		class Meta:
				# Gives the proper plural name for admin
				verbose_name_plural = "Categories"

		def __str__(self):
				return self.event_category

		def get_random3():
				max_id = EventCategory.objects.all().aggregate(max_id=Max("id"))['max_id']
				while True:
						pk = random.randint(1, max_id)
						category = EventCategory.objects.filter(pk=pk).first()
						if category:
							return category


class Organizer(models.Model):
		Organizer_name = models.CharField(max_length=200,unique = True)
		user_Id = models.ForeignKey(User, default=1, verbose_name="UserID", on_delete=models.SET_DEFAULT)
		def __str__(self):
				return self.Organizer_name

class Event(models.Model):
	event_title = models.CharField(max_length=200)
	event_description = models.TextField()
	event_brief = models.TextField()
	event_published = models.DateTimeField('date published')
	event_date = models.DateTimeField('Date of event')
	event_image = models.ImageField('Image',upload_to="gallery")

	organizer_id = models.ForeignKey(Organizer, default=1, verbose_name="Organizer", on_delete=models.CASCADE)
	event_category = models.ForeignKey(EventCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	max_Team_size = models.PositiveIntegerField(default = 1)

	def __str__(self):
		return self.event_title

	def get_event_cat(self):
		return self.event_category.event_category

class EventRegistration(models.Model):
	team_name = models.CharField(max_length=200)#Age, Occupation, Instution Name
	registration_time = models.DateTimeField(auto_now_add=True,verbose_name = 'Time Registered')
	team_members_id = models.TextField(blank=True,default = "")
	team_members_age = models.TextField(blank=True,default = "")
	user_Id = models.ForeignKey(User, default=1, verbose_name="UserID", on_delete=models.SET_DEFAULT)
	event_id = models.ForeignKey(Event, default=1, verbose_name="Event Id", on_delete=models.SET_DEFAULT)
	team_size = models.PositiveIntegerField(default = 1)

	def __str__(self):
		return self.team_name+str(self.event_id.id)

	def get_event_title(self):
		return self.event_id.event_title

	def set_ids(self,ids):
		if json.loads(ages).length < self.team_size	:
			team_members_id = ids

	def set_ages(self,ages):
		if json.loads(ages).length < self.team_size	:
			team_members_age = ages
