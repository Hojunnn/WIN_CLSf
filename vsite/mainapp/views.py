from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.views import generic
from .models import UploadDocument

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

def category(request):
    template = loader.get_template('mainapp/category.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def get(request):
        print("gooooooooooooooooooooooooooooo")
        template_name = 'mainapp/index.html'
        up_list = UploadDocument.objects.all()
        up_list_name=[]

        return render(request, template_name,{'up_list':up_list, 'up_list_name':up_list_name})




