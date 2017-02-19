from django.http import HttpResponse
from django.shortcuts import render

def frontpage(request):
    return HttpResponse("FRONT PAGE IS HERE")

def callback(request):
    return HttpResponse("INSTAGRAM TOKEN HERE")

def rendering(request):
	data_list = [4, 8, 15, 16, 23, 42, 60, 120, 240, 450]
	return render(request, "base.html", {'data': data_list})


	