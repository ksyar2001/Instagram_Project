from django.http import HttpResponse

def frontpage(request):
    return HttpResponse("FRONT PAGE IS HERE")

def callback(request):
    return HttpResponse("INSTAGRAM TOKEN HERE")