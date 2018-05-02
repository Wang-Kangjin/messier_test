from django.http import Http404, HttpResponse
import datetime
from django.template import loader, Context

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def index(request):
    t = loader.get_template('name.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)

def name(request):
    t = loader.get_template('name.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)

def asteroid(request):
    t = loader.get_template('asteroid.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)

def galaxy(request):
    t = loader.get_template('galaxy.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)

def moon(request):
    t = loader.get_template('moon.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)

def pluto(request):
    t = loader.get_template('pluto.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)

def star(request):
    t = loader.get_template('star.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)

def year(request):
    t = loader.get_template('year.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)

def result(request):
    t = loader.get_template('result.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)