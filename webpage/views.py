from django.http import HttpResponse
from django.shortcuts import render
from forms import UsernameForm
from web_scrape import *

def frontpage(request):
    return HttpResponse("FRONT PAGE IS HERE")

def callback(request):
    return HttpResponse("INSTAGRAM TOKEN HERE")

def rendering(request):
	return render(request, "base.html")

def data_visualization(request):
	form = UsernameForm()
	if request.method == 'POST':
		form = UsernameForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			username = (form.cleaned_data).get('username')
			print "===================="
			print username

		# web_scrape(username)
	return render(request, "base.html")





	