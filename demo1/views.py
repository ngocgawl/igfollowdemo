from re import template
from django.http import HttpResponse
# from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('demo1/index.html')
    return HttpResponse(template.render())

def invite(request):
    template = loader.get_template('demo1/invite.html')
    return HttpResponse(template.render())