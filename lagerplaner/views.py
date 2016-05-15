from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('lagerplaner/index.html')
    context = RequestContext(request, {
            
        })
    return HttpResponse(template.render(context))
    
def todoo(request):
        template = loader.get_template('lagerplaner/todoo.html')
        context = RequestContext(request, {
            
            })
        return HttpResponse(template.render(context))
