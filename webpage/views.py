from django.http import HttpResponse
from django.shortcuts import render

def frontpage(request):
    return HttpResponse("FRONT PAGE IS HERE")

def callback(request):
    return HttpResponse("INSTAGRAM TOKEN HERE")

def rendering(request):


	return render(request, "base.html")


	