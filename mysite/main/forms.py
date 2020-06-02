from tinymce.widgets import TinyMCE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EventRegistration,Event

class SignUpForm(UserCreationForm):
	formfield_overrides = {
        forms.CharField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	email = forms.EmailField(max_length=254,	required=True, help_text='Required')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
					
	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user

	def clean_email(self):
			from django.core.exceptions import ValidationError
			email = self.cleaned_data['email']
			if User.objects.filter(email=email).exists():
					raise ValidationError("Email already exists")
			return email
			
class EventRegistrationForm(forms.ModelForm):
	formfield_overrides = {
        forms.CharField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }
	class Meta:
		model = EventRegistration
		fields = ('team_name', 'team_members_id', 'team_members_age', 'team_size', )
		
	def save(self, commit=True):
		eve = super(EventRegistrationForm, self).save(commit=False)
		eve.event_id.id = 2
		if commit:
			eve.save()
		return eve
		
class EventCreationForm(forms.ModelForm):
	formfield_overrides = {
        forms.CharField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }
	class Meta:
		model = Event
		fields = ('event_title', 'event_description', 'event_brief', 'event_published','event_date','event_image','max_Team_size',)
	
	def save(self, commit=True):
		eve = super(EventRegistrationForm, self).save(commit=False)
		eve.event_id.id = 2
		if commit:
			eve.save()
		return eve