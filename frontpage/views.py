from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from frontpage.models import User, Photo

def index(request):
    template = loader.get_template('frontpage/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def blaimage(request, blaine_image):
    template = loader.get_template('frontpage/blaimage.json')
    context = {'img': Photo.objects.all().order_by('user')[blaine_image]}
    return HttpResponse(template.render(context, request))