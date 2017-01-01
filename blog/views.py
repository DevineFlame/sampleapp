from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("<p>Hello my dear welcome to my blog</p>")
