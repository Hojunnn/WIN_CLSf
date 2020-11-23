from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import UploadDocument

def index(request):
    template = loader.get_template('mainapp/index.html')
    context = {
        'latest_question_list': "test",
    }
    print("111111",request.POST)
    return HttpResponse(template.render(context, request))


def new(request, area):
    template = loader.get_template('mainapp/new.html')
    upload_file = UploadDocument.objects.filter(name=area)
    context = {
        'latest_question_list': "test",
        'upload_file': upload_file
    }
    return HttpResponse(template.render(context, request))


def get(request):
        template_name = 'mainapp/index.html'
        up_list = UploadDocument.objects.all()

        return render(request, template_name,{'up_list':up_list})

