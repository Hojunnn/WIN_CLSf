from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('mainapp/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def new(request):
    template = loader.get_template('mainapp/new.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def new(request):
    template = loader.get_template('mainapp/new.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def category(request):
    template = loader.get_template('mainapp/category.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))




