from django.shortcuts import render, redirect
from .models import Event, EventCategory, Organizer, EventRegistration
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

from django.db.models import Q
from .forms import SignUpForm,EventRegistrationForm,EventCreationForm
from django.http import HttpResponse
# Create your views here.


def homepage(request):
		query = ""
		context = {}
		if request.GET:
			query = request.GET['q']
			context['query'] = str(query)
		categories = get_qset(query)
		context['categories'] = sorted(categories,key = Event.get_event_cat)
		context['events'] = Event.objects.all
		return render(request=request,
                  template_name='main/home.html',
									context=context)

def account(request):
	user_id = request.user
	context = {}
	events_participating = EventRegistration.objects.filter(Q(user_Id__username__exact=user_id.username))
	events_organizing = Event.objects.filter(Q(organizer_id_id__user_Id__username__exact=user_id.username))
	temp = []
	print(events_organizing)
	for evepart in events_participating:
		temp.append(evepart.event_id)
	events_participating = temp

	context['organized'] = events_organizing
	context['participating'] = events_participating
	return render(request=request,
	template_name='main/account.html',
	context = context)

def register(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New account created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")

		else:
			for msg in form.errors :
				messages.error(request, f"{msg}: {form.errors[msg].as_text()[5:]}")

			return render(request = request,
									template_name = "main/register.html",
									context={"form":form})

	form = SignUpForm
	return render(request = request,
										template_name = "main/register.html",
										context={"form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def get_qset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = Event.objects.filter(
			Q(event_brief__icontains=q)|
			Q(event_description__icontains=q)|
			Q(event_category__event_category__icontains=q)|
			Q(event_title__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)


	return list(set(queryset))

def EventCreate(request):
	if request.method == "POST":
		form = EventCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			event_title = form.cleaned_data.get('event_title')
			messages.success(request, f"Event {event_title} is created")
			return redirect("main:homepage")

		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

			return render(request = request,
									template_name = "main/EventCreate.html",
									context={"form":form})

	form = EventCreationForm
	return render(request = request,
										template_name = "main/EventCreate.html",
										context={"form":form})

def EventRegister(request):
	if request.method == "POST":
		form = EventRegistrationForm(request.POST)
		if form.is_valid():
			reg = form.save()
			team_name = form.cleaned_data.get('team_name')
			messages.success(request, f"Event Registered : {team_name}")
			return redirect("main:homepage")

		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

			return render(request = request,
								template_name = "main/EventRegister.html",
									context={"form":form})
	else:
		context = {}
		context['form'] = EventRegistrationForm
		return render(request = request,
										template_name = "main/EventRegister.html",
										context=context)
