from django.contrib import admin
from .models import Event, EventCategory, Organizer, EventRegistration
from tinymce.widgets import TinyMCE
from django.db import models


class EventAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["event_title", "event_published"]}),
        ("Content", {"fields": ["event_brief","event_description"]}),
		("Category", {"fields": ["event_category"]}),
        ("Event Date", {"fields": ["event_date"]}),
        ("Image", {"fields": ["event_image"]}),
        ("Max Team Strength",{"fields": ["max_Team_size"]}),
        ("Organizer", {"fields" : ["organizer_id"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }
				
class EventRegistrationAdmin(admin.ModelAdmin):
		fieldsets = [
        ("Title", {'fields': ["team_name"]}),
        ("Team Info", {"fields": ["team_size"]}),
        ("Registered User",{"fields": ["user_Id"]}),
        ("Event ID", {"fields" : ["event_id"]})
    ]
		
admin.site.register(Event,EventAdmin)
admin.site.register(EventCategory)
admin.site.register(EventRegistration,EventRegistrationAdmin)
admin.site.register(Organizer)
