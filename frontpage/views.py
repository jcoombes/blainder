from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('frontpage/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def blaimage(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed for this endpoint')

