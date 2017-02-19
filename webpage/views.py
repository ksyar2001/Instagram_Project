from django.http import HttpResponse
from django.shortcuts import render

def frontpage(request):
    return HttpResponse("FRONT PAGE IS HERE")

def callback(request):
    return HttpResponse("INSTAGRAM TOKEN HERE")

def rendering(request):
	data_list = [100,200,300,400,500]
	return render(request, "base.html", {'data': data_list})


	