from django.shortcuts import render
from django.views.generic import TemplateView

# testregeltje nodig voor Hallo Wereld
# from django.http import HttpResponse
# Create your views here.

#Hallo Wereld even uitgezt
# def TestView(request, **kwargs):
# 	return HttpResponse("<h1>Hello Macje</h1>")

class SplashView(TemplateView):
    template_name = 'index.html'
