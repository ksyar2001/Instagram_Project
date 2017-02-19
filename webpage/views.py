from django.http import HttpResponse
from django.shortcuts import render
from forms import UsernameForm
from web_scrape import *
from output import *

def frontpage(request):
    return HttpResponse("FRONT PAGE IS HERE")

def callback(request):
    return HttpResponse("INSTAGRAM TOKEN HERE")

def rendering(request):
	form = UsernameForm()
	return render(request, "base.html", {'form':form, 'login':True, 'csv':False})

def data_visualization(request):
	form = UsernameForm()
	csv_string = None
	if request.method == 'POST':
		form = UsernameForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			username = (form.cleaned_data).get('username')

		web_scrape(username)
		csv_string = generatePhotoCSV(username)

	return render(request, "base.html", {'csv':csv_string})





	