from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. This is Polls index")
# Create your views here.
